from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        result = {
            "easy": 1.0,
            "medium": 1.0,
            "hard": 1.0
        }

        return str(result)

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)