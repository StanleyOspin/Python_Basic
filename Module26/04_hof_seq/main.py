from typing import Iterable


class QHofstadter:
    def __init__(self, numbers: list) -> None:
        self.sequence = numbers[:]
        if self.sequence == [1, 2]:  # TODO точнее толькой [1, 1] верная последовательность, это надо проверить
            raise StopIteration  # TODO Добавьте поясняющее сообщение в круглых скобках: "Невалидная исходная
                                 #  последовательность"

    def __iter__(self):
        return self

    def __next__(self) -> Iterable[int]:
        try:
            n = len(self.sequence)
            q = self.sequence[n - self.sequence[n - 1]] + self.sequence[n - self.sequence[n - 2]]
            self.sequence.append(q)
            return q

        except IndexError:
            raise StopIteration


Q = QHofstadter([1, 1])
print([next(Q) for _ in range(20)])
