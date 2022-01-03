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

    @staticmethod
    def yellow_light(msg:str) -> str:
        return f"🟡 {msg}"

    @staticmethod
    def white_light(msg:str) -> str:
        return f"⚪️ {msg}"

    @staticmethod
    def success_callout(msg:str) -> str:
        return f"🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩{msg}\n🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩🟩"

    @staticmethod
    def error_callout(msg:str) -> str:
        return f"🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥{msg}\n🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥🟥"

    

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
