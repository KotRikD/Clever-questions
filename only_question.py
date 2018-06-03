from longpolling import LongPoll
import time
import config

clever = LongPoll(config.VK_TOKEN)

if __name__ == "__main__":
    while True:
        question = clever.check_question()
        if question:
            print("------------------")
            print(question.question + "\n")
            print(question.answers[0])
            print(question.answers[1])
            print(question.answers[2])
            print("------------------")
            time.sleep(25)