from flask import Flask, request, jsonify
from env import DataCleanEnv

app = Flask(__name__)

env = None


@app.route("/")
def home():
    return "OpenEnv is running"


@app.route("/reset", methods=["POST"])
def reset():
    global env

    try:
        data = request.get_json(force=True)  # Fix for 415 error

        task = data.get("task_type", "easy")

        env = DataCleanEnv(task)
        obs = env.reset()

        return jsonify({
            "observation": str(obs)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/step", methods=["POST"])
def step():
    global env

    try:
        data = request.get_json(force=True)  # Fix for 415 error

        action = data.get("action")

        if env is None:
            return jsonify({"error": "Environment not initialized"}), 400

        obs, reward, done, _ = env.step(action)

        return jsonify({
            "observation": str(obs),
            "reward": reward,
            "done": done
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)