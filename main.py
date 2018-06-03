from compare import Compare
from longpolling import LongPoll
import time
import config

clever = LongPoll(config.VK_TOKEN)

if __name__ == "__main__":
    while True:
        question = clever.check_question()
        if question:
            c = Compare(question.question, question.answers)
            c.check()
            time.sleep(10)
