import random

random.seed()


class BlackJack:
    def __init__(self):
        self.deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'] * 4
        self.score = 0
        self.diler_score = 0
        self.step = 1

    def print_card(self, current, score, diler):
        if not diler:
            if self.step == 1:
                print('Вам попалась комбинация карт {} и {}. У вас {} очков.'.format(current[0], current[1], score))
            else:
                print('Вам попалась карта {}. У вас {} очков.'.format(current, score))

    def random_card(self, score, diler):
        current = []
        if self.step == 1:
            for card in range(2):
                card = self.deck.pop()
                if type(card) is int:
                    score += card
                elif card == 'Туз':
                    if score <= 10:
                        score += 11
                    else:
                        score += 1
                else:
                    score += 10
                current.append(card)

        else:
            card = self.deck.pop()
            if type(card) is int:
                score += card
            elif card == 'Туз':
                if score <= 10:
                    score += 11
                else:
                    score += 1
            else:
                score += 10
            current.append(card)
        self.print_card(current, score, diler)
        return score

    def choice(self):
        score = self.random_card(self.score, False)
        diler_score = self.random_card(self.diler_score, True)
        while True:
            self.step += 1
            choice = input('Будете брать карту? y/n\n')
            if choice == 'y':
                score = self.random_card(score, False)
                if diler_score < 17 and score <= 21:
                    diler_score = self.random_card(diler_score, True)
                elif score > 21 or diler_score == 21:
                    print('Вы проиграли, у вас {} очков - "это перебор", у крупье {} очков'.format(score, diler_score))
                    break
                elif score == diler_score:
                    print('ничья')
                elif score == 21 or diler_score > 21:
                    print('Вы победили, у вас {} очков, у крупье {} очков.'.format(score, diler_score))
                    break
            elif choice == 'n':
                if score > diler_score and diler_score < 17:
                    while diler_score < 17:
                        diler_score = self.random_card(diler_score, True)
                if score < diler_score <= 21:
                    print('Вы проиграли, у вас {} очков, у крупье {} очков.'.format(score, diler_score))
                else:
                    print('Вы победили, у вас {} очков, у крупье {} очков.'.format(score, diler_score))

                break

    def start(self):
        random.shuffle(self.deck)
        print('Игра в BlackJack')
        print('=' * 35)
        self.choice()

        print('\nЗаходите к нам еще!')


game = BlackJack()
game.start()
