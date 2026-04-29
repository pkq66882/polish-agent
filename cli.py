from app.agent import PolishAgent

def main():
    agent = PolishAgent()
    while True:
        text = input("输入内容（exit退出）：\n")
        if text.lower() == "exit":
            break

        result = agent.polish(text)

        print("\nFormal:", result["formal"])
        print("\nNeutral:", result["neutral"])
        print("\nFriendly:", result["friendly"])

if __name__ == "__main__":
    main()
