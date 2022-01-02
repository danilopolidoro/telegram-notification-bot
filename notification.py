import telegram

class Notification:
    def __init__(self, telegram_token:str, chat_id:int):
        self.__BOT = telegram.Bot(token=telegram_token)
        self.__CHAT_ID = chat_id
        self.__msg_stack = []

    def __send_message(self, msg:str):
        self.__BOT.send_message(text=msg, chat_id=self.__CHAT_ID)

    def get_msg_stack(self):
        pass

    def edit_msg_stack(self):
        pass


class Elements:
    @staticmethod
    def completed(msg:str) -> str:
        return f"✅ {msg}"
    
    @staticmethod
    def green_light(msg:str) -> str:
        return f"🟢 {msg}"

    @staticmethod
    def red_light(msg:str) -> str:
        return f"🔴 {msg}"

class ProgressBar:
    def __init__(self, start:int, end:int) -> None:
        self.__START = start
        self.__END = end
        self.__pos = start

    def update(self, pos):
        self.__pos = pos

    def __render(self):
        pass

    def __str__(self) -> str:
        return self.__render()