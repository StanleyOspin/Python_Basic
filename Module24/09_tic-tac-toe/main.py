class Tic_tac_toe:

    def __init__(self):
        self.board = list(range(1, 10))
        self.winning_coordinates = (
            (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def draw_board(self):
        print('-------------')
        for i in range(3):
            print('|', self.board[0 + i * 3], '|', self.board[1 + i * 3], '|', self.board[2 + i * 3], '|')
            print('-------------')

    def take_input(self, player_token):
        valid = False
        while not valid:
            player_answer = input('Куда поставим ' + player_token + '? ')
            try:
                player_answer = int(player_answer)
            except:
                print('Некорректный ввод. Вы уверены, что ввели число?')
                continue
            if 1 <= player_answer <= 9:
                if str(self.board[player_answer - 1]) not in 'XO':
                    self.board[player_answer - 1] = player_token
                    valid = True
                else:
                    print("Эта клетка уже занята!")
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")

    def check_win(self):
        for coordinate in self.winning_coordinates:
            if self.board[coordinate[0]] == self.board[coordinate[1]] == self.board[coordinate[2]]:
                return self.board[coordinate[0]]
        return False

    def main(self):
        counter = 0
        win = False
        while not win:
            self.draw_board()
            if counter % 2 == 0:
                self.take_input('X')
            else:
                self.take_input('O')
            counter += 1
            if counter > 4:
                tmp = self.check_win()
                if tmp:
                    print(tmp, "выиграл!")
                    win = True
                    break
            if counter == 9:
                print("Ничья!")
                break
        self.draw_board()


play = Tic_tac_toe()
play.main()
