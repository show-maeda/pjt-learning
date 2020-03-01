# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), 'sendgrid.env')
load_dotenv(dotenv_path)
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

from sendgrid import SendGridAPIClient
sg = SendGridAPIClient(SENDGRID_API_KEY)

if __name__ == '__main__':
    data = {
        "address": "3-9-3",
        "address_2": "Meguro",
        "city": "Meguroeguro",
        "country": "Japan",
        "from": {
            "email": "s.maeda.kobe@gmail.com",
            "name": "s.maeda.kobe"
        },
        "nickname": "kobe address",
        "reply_to": {
            "email": "s.maeda.kobe@gmail.com",
            "name": "s.maeda.kobe"
        },
        "state": "Tokyo",
        "zip": "1530063"
    }

    response = sg.client.senders.post(request_body=data)
    print(response.status_code)
    print(response.body)
    print(response.headers)
