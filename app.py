from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CSI2113 DevOps Application</title>
    </head>
    <body>
        <h1>CSI2113 DevOps Web Application</h1>
        <p>Containerized Web Application with CI/CD</p>
        <p>Application is running successfully.</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)