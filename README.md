# Live Cryptocurrency Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey.svg)
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Lambda-orange.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0-green.svg)

A lightweight data-driven dashboard that tracks portfolio performance, fetches live cryptocurrency data, and stores it in AWS.
Built to practice ETL pipelines, data visualization, and web deployment.

---

## Features
- Real-time Data: Pulls live market prices from CoinGeckko API.
- Portfolio Tracking: Load mock investments or actual holdings and see gains/losses.
- ETL Pipeline: Extract, transform, and load raw JSON data into a clean database.
- Web App: Flask-based dashboard with simple, clean UI.

## Tech Stack
- Cloud/Infrastructure: AWS Lambda, API Gateway, AWS S3
- Backend: Python (Flask, Pandas, Boto3)
- Frontend: HTML, CSS, Bootstrap
- API: CoinGecko (crypto data)
- Tools: Git, Github, VSCode

## Project Structure
investment_dashboard_project/
|-- app.py                   # Flask app serving the dashboard
|-- etl.py                   # ETL pipeline - fetch, trasnform, clean data
|-- lambda_function.py       # AWS Lambda function for API integration
|-- mock_investments.json    # Example portfolio data
|-- requirements.txt         # Project dependencies
|-- .gitignore               # Ignore config
|
|-- data/                    # Sample + processed data
|    |-- raw_investments.json
|    |-- raw_live_data.json
|    |-- processed_investments.xlsx
|    |-- processed_live_data.csv
|
|-- function.zip             # Deployment package for AWS Lambda

---

## How to run locally
1. Clone repo:
  '''bash
  git clone https://github.com/rahulsrik22/crypto-dashboard.git
  cd crypto-dashboard
2. Install dependencies
  pip install -r requirements.txt
3. Config AWS credentials for S3
  aws configure
4. Run Flask app
  flask run (--port=5001 if 5000 is busy on Macbook)
5. Open in browser
  http://127.0.0.1:5000

## Deployment
This project is designed for cloud deployment. The ETL process runs as an AWS Lambda function, triggered via API Gateway, wirth results stored in S3. The Flask app can be hosted on an EC2 instance or containerized with Docker for production.
