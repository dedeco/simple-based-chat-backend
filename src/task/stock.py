import codecs
import csv
import json
from contextlib import closing

import requests
from firebase_admin import auth
from huey import RedisHuey
from matchbox import database

from src.chat.models import MessageService
from src.user.user_service import UserService, UserDuplicatedError

huey = RedisHuey('chat_bot', host='0.0.0.0')

UID_CHAT_BOT = "WhmylOoKgsT4zM8nKsJLTcnyA0v1"


@huey.on_startup()
def setup_db_connection():
    f = open('config-huey.json', )
    database.db_initialization(json.load(f))
    _create_user_chat_bot()


def _create_user_chat_bot():
    try:
        UserService({"user": auth.get_user(UID_CHAT_BOT)}).create()
    except UserDuplicatedError:
        pass


@huey.task(retries=2, retry_delay=60)
def get_stock_info(stock_code):
    quotation = None
    URL = 'https://stooq.com/q/l/?s={0}&f=sd2t2ohlcv&h&e=csv'.format(stock_code)
    with closing(requests.get(URL, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
        for i, row in enumerate(reader):
            if i == 1:
                print("row", row)
                quotation = row[6]
                break
    print('quotation: ', quotation)
    if quotation == 'N/D':
        MessageService.create(
            {"message": f"{stock_code} not found, try again, please!",
             "user": UserService({}).get({"uid": UID_CHAT_BOT})},
        )
    else:
        MessageService.create(
            {"message": f"{stock_code} quote is ${quotation} (close) per share",
             "user": UserService({}).get({"uid": UID_CHAT_BOT})},
        )
    return quotation
