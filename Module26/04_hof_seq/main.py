from typing import Iterable


class Q_Hofstadter: # TODO Аналогично предыдущему
    def __init__(self, numbers: list) -> None:
        self.sequence = numbers[:]

    def __iter__(self):
        return self

    def __next__(self) -> Iterable[int]:
        try:
            n = len(self.sequence)
            if self.sequence[0] + self.sequence[1] != 3:  # TODO 1) проверку делайте в __init__
                                                          #  2) проверка не верная, надо сраввнить self.sequerns c [1, 1]
                q = self.sequence[n - self.sequence[n - 1]] + self.sequence[n - self.sequence[n - 2]]
                self.sequence.append(q)
                return q
            else:
                raise StopIteration

        except IndexError:
            raise StopIteration


Q = Q_Hofstadter([1, 2])
print([next(Q) for _ in range(20)])
