import telegram

class Notification:
    def __init__(self, telegram_token:str, chat_id:int):
        self.__BOT = telegram.Bot(token=telegram_token)
        self.__CHAT_ID = chat_id
        self.__msg_stack = []
        self.__msg_id = self.__send_message("Initiating Notification").message_id

    def __send_message(self, msg:str):
        return self.__BOT.send_message(text=msg, chat_id=self.__CHAT_ID)

    def __update_message(self):
        rendered_message = self.__render()
        self.__BOT.edit_message_text(
            text=rendered_message,
            chat_id=self.__CHAT_ID,
            message_id = self.__msg_id
        )

    def __render(self):
        '''Render message stack as a string'''
        base_str = ""

        if len(self.__msg_stack) == 0:
            return "Empty Notification"

        for el in self.__msg_stack:
            base_str += str(el)
            base_str += "\n"
        
        return base_str

    def __getitem__(self, item):
        return self.__msg_stack[item]

    def __setitem__(self, key, value):
        self.__msg_stack[key] = value
        self.__update_message()
    
    def __delitem__(self, key):
        del self.__msg_stack[key]
        self.__update_message()

    def __iter__(self):
        for el in self.__msg_stack:
            yield el
    
    def add(self, content):
        self.__msg_stack.append(content)
        self.__update_message()

    def __str__(self) -> str:
        return self.__render()



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