class Buddhist:
    def __init__(self):
        self.__karma = 0
        self.__day = 1

    def get_karma(self):
        return self.__karma

    def get_day(self):
        return self.__day

    def set_karma(self, karma):
        self.__karma = karma

    def set_day(self, day):
        self.__day = day
