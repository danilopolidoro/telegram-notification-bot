class Elements:
    @staticmethod
    def completed(msg:str) -> str:
        return f"ā {msg}"
    
    @staticmethod
    def green_light(msg:str) -> str:
        return f"š¢ {msg}"

    @staticmethod
    def red_light(msg:str) -> str:
        return f"š“ {msg}"

    @staticmethod
    def yellow_light(msg:str) -> str:
        return f"š” {msg}"

    @staticmethod
    def white_light(msg:str) -> str:
        return f"āŖļø {msg}"

    @staticmethod
    def success_callout(msg:str) -> str:
        return f"š©š©š©š©š©š©š©š©š©š©š©š©{msg}\nš©š©š©š©š©š©š©š©š©š©š©š©"

    @staticmethod
    def error_callout(msg:str) -> str:
        return f"š„š„š„š„š„š„š„š„š„š„š„š„{msg}\nš„š„š„š„š„š„š„š„š„š„š„š„"

    

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
