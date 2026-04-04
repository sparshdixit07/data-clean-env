from client import Client


def main():
    task_types = ["easy", "medium", "hard"]
    scores = {}
    
    for task_type in task_types:
        client = Client(task_type)
        score, df = client.run(max_steps=10)
        scores[task_type] = score
    
    print("Final Scores:", scores)


if __name__ == "__main__":
    main()
