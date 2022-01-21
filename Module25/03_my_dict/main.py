from typing import Dict  # TODO это класс только для нотификации, а нам нужен dict


class MyDict(Dict):  # TODO тут укажите базовый класс dict
    def get(self, key, default=0):  # TODO согласно заданию возможности выбирать что возвращать при отсутствии ключа нет,
                                    #  значить параметр default убираем
        super().get(key, default)  # TODO а тут вместо default указываем число 0

