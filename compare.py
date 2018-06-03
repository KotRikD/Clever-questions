### ANSWERS DICT LIKE THIS
### ('Мыши', 'Пчёлы', 'Мухи') # 3 ELEMENTS!!!
import difflib
import yandex_search
import config

yandex = yandex_search.Yandex(api_user=config.API_USER, api_key=config.API_KEY)

replacement = {'x': 'х', 'o': 'о', 'у': 'у', 'e': 'е', 'a': 'а'}

class Compare():

    def __init__(self, question: str, answers: list):
        self.question = question.lower()
        self.answers = answers

        if not self.question or \
           not self.answers:
            raise Exception("Question or answers is not defined")

        if len(answers) < 3 or len(answers) > 3:
            raise Exception("Answers list is not correct") 

        for (k, v) in replacement.items():
            self.question.replace(k, v)
            
            for x in answers:
                x.replace(k, v)

    def check(self):
        r = self.search()

        counters = {0: 0, 1: 0, 2: 0}

        for x in r:

            s_r = x['snippet'].lower()

            if self.answers[0].lower() in s_r:
                counters[0]+=1
            
            if self.answers[1].lower() in s_r:
                counters[1]+=1

            if self.answers[2].lower() in s_r:
                counters[2]+=1

        
        for x in r[:3]:
            print(x['snippet'] + "\n--------------------")

        print(f"1. {counters[0]}\n"
              f"2. {counters[1]}\n"
              f"3. {counters[2]}\n")

    def search(self):
        r = yandex.search(self.question).items
        return r


        



