import json
import urllib.request
import boto3
import datetime

s3 = boto3.client('s3')
bucket_name = 'investment-data-rs20250630'

def lambda_handler(event, context):
    api_url = (
        "https://api.coingecko.com/api/v3/simple/price"
        "?ids=bitcoin,ethereum,dogecoin,cardano,avalanche-2"
        "&vs_currencies=usd"
        "&include_market_cap=true"
        "&include_24hr_vol=true"
        "&include_24hr_change=true"
        "&include_last_updated_at=true"
    )

    with urllib.request.urlopen(api_url) as response:
        data = json.loads(response.read().decode())

    print("DEBUG: Raw API response JSON:")
    print(json.dumps(data, indent=2))

    timestamp = datetime.datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    file_key = f'raw_data/crypto_prices_{timestamp}.json'

    s3.put_object(
        Bucket=bucket_name,
        Key=file_key,
        Body=json.dumps(data).encode('utf-8')
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': f'Live data saved to S3 at {file_key}'})
    }