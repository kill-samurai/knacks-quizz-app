import datetime as dt
import time
import requests
from html import unescape
import json

# date now
DATE = dt.datetime.now()
# formatted date as per knack's object
knack_date = DATE.strftime("%m/%d/%Y")
KNACK_BASE_URL = "https://api.knack.com/v1/objects/object_1/records"
HEADERS = {
    "X-Knack-Application-Id": "",
    "X-Knack-REST-API-KEY": "",
    "content-type": "application/json"
}

def knack_post(date, category, question, correct_answer):
    body = json.dumps({
        "field_2": date,
        "field_3": category,
        "field_4": question,
        "field_7": correct_answer
    })

    response = requests.post(url=KNACK_BASE_URL, headers=HEADERS, data=body)
    print(response.text)
    print(response)

category = ""
question = ""
correct_answer = ""

# request for the quiz data
BASE_URL = "https://opentdb.com/api.php?"
PARAMETER = {
    "amount": 5,
    "type": "boolean",
    "encode": ""
}

request = requests.get(url=BASE_URL, params=PARAMETER)


data = request.json()["results"]

for item in range(0, len(data)):
    date_loop = knack_date
    category = unescape(data[item]["category"]).replace('"', "'")
    question = unescape(data[item]["question"]).replace('"', "'")
    correct_answer = unescape(data[item]["correct_answer"])
    knack_post(date=date_loop, category=category, question=question, correct_answer=correct_answer)
    time.sleep(1)
