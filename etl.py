import boto3
import json
import pandas as pd

s3 = boto3.client('s3')
bucket_name = 'investment-data-rs20250630'

# Get latest file
response = s3.list_objects_v2(Bucket=bucket_name, Prefix='raw_data/')
files = [obj['Key'] for obj in response.get('Contents', [])]
live_files = [f for f in files if f.startswith('raw_data/crypto_prices_')]

if not live_files:
    raise ValueError("No live data files found in raw_data/ folder.")

latest_file = sorted(live_files)[-1]
print("DEBUG: ETL processing live file:", latest_file)
                                                                            #latest_file = sorted(files)[-1]

# Download latest raw data
s3.download_file(bucket_name, latest_file, 'raw_live_data.json')

with open('raw_live_data.json') as f:
    raw_data = json.load(f)

# print type and contents of raw data
print("DEBUG: raw_data type =", type(raw_data))
print("DEBUG: raw_data contents =", json.dumps(raw_data, indent=2))

records = []
for coin, info in raw_data.items():
    records.append({
        "coin": coin,
        "price_usd": info["usd"],
        "market_cap_usd": info.get("usd_market_cap"),
        "volume_24h_usd": info.get("usd_24h_vol"),
        "change_24h_pct": info.get("usd_24h_change"),
        "last_updated_at": info.get("last_updated_at")
    })

df = pd.DataFrame(records)

# Convert timestamp to readable datetime
df['last_updated_at'] = pd.to_datetime(df['last_updated_at'], unit='s')
df['last_updated_at'] = df['last_updated_at'].dt.strftime('%Y-%m-%d %H:%M')

# Round and format price with dollar sign
df['price_usd'] = df['price_usd'].apply(lambda x: f"${x:.2f}" if pd.notnull(x) else None)

# Round and format 24h change with percent sign
df['change_24h_pct'] = df['change_24h_pct'].apply(lambda x: f"{x:.2f}%" if pd.notnull(x) else None)

# Round and format market cap to nearest million with dollar sign
df['market_cap_usd'] = df['market_cap_usd'].apply(
    lambda x: f"${round(x/1_000_000):,}M" if pd.notnull(x) else None
)

# Round and format 24h volume to nearest million with dollar sign
df['volume_24h_usd'] = df['volume_24h_usd'].apply(
    lambda x: f"${round(x/1_000_000):,}M" if pd.notnull(x) else None
)

print("Processed DataFrame with formatted metrics:\n", df.head())

df.to_csv('processed_live_data.csv', index=False)
s3.upload_file('processed_live_data.csv', bucket_name, 'processed_data/processed_live_data.csv')
print("Processed data with formatted metrics saved to CSV and uploaded to S3.")

