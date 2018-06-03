import requests
import time

class CleverQuestion():

    __slots__ = ('question', 'answers')

    def __init__(self, question, answers: list):
        self.question = question
        self.answers = answers

class LongPoll():

    def __init__(self, token):
        if not token or token is "":
            print("Token is empty. Exiting...")
            exit()
        self.base_uri = "https://api.vk.com/method/execute."
        self.start_data = "getStartData"
        self.get_question = "getLastQuestion"

        self.wait = 10
        self.values = {
            'access_token': token,
            'v': '5.73'
        }
    
    def check_question(self):
        response = requests.get(
            self.base_uri+self.get_question,
            params=self.values,
            timeout=self.wait
        ).json()
        time.sleep(2)

        if not response['response']:
            return None
        else:
            q = response['response']['text']
            a1 = response['response']['answers'][0]['text']
            a2 = response['response']['answers'][1]['text']
            a3 = response['response']['answers'][2]['text']

            clever = CleverQuestion(q, (a1, a2, a3))

        return clever

    def check_start_data(self):
        response = requests.get(
            self.base_uri+self.start_data,
            params=self.values
        ).json()
        return response