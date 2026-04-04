import os
import requests
from openai import OpenAI

# Environment variables
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:7860")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-3.5-turbo")
HF_TOKEN = os.getenv("HF_TOKEN")  # no default

client = OpenAI()

def run_task(task_type):
    print("START")

    # Reset environment
    response = requests.post(
        f"{API_BASE_URL}/reset",
        json={"task_type": task_type}
    )
    data = response.json()
    obs = data.get("observation")

    done = False
    step_count = 0

    while not done and step_count < 5:
        # Dummy decision (rule-based)
        action = "clean"

        print(f"STEP {step_count}: action={action}")

        response = requests.post(
            f"{API_BASE_URL}/step",
            json={"action": action}
        )
        data = response.json()

        obs = data.get("observation")
        reward = data.get("reward")
        done = data.get("done")

        step_count += 1

    print("END")


def main():
    for task in ["easy", "medium", "hard"]:
        run_task(task)


if __name__ == "__main__":
    main()