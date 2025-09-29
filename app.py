from flask import Flask, render_template_string
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    df = pd.read_csv('processed_live_data.csv')
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template_string("""
    <html>
    <head>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <title>Investment Dashboard</title>
    </head>
    <body>
        <div class="container">
            <h1 class="mt-5 mb-4">Investment Dashboard</h1>
            {{table | safe}}
        </div>
    </body>
    </html>
    """, table=table_html)

if __name__ == "__main__":
    app.run(debug=True, port=5000)