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
    data = request.json
    task = data.get("task_type", "easy")

    env = DataCleanEnv(task)
    obs = env.reset()

    return jsonify({
        "observation": str(obs)
    })


@app.route("/step", methods=["POST"])
def step():
    global env
    data = request.json
    action = data.get("action")

    obs, reward, done, _ = env.step(action)

    return jsonify({
        "observation": str(obs),
        "reward": reward,
        "done": done
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)