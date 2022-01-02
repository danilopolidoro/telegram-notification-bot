import telegram

class Notification:
    def __init__(self, telegram_token:str) -> None:
        self.__BOT = telegram.Bot(token=telegram_token)

    def send_message(self, msg:str, chat_id:int):
        self.__BOT.send_message(text=msg, chat_id=chat_id)
    