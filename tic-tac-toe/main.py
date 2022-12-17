import os


def blue(text):
    return "\033[34m" + text + "\033[0m"

def cyan(text):
    return "\033[36m" + text + "\033[0m"

def grey(text):
    return "\033[90m" + text + "\033[0m"

def color(text):
    if text.lower() == "x": return "\033[34m" + text + "\033[0m"
    if text.lower() == "o": return "\033[36m" + text + "\033[0m"
    return text

# for i in range(100):
#     print(f"\033[{i}m" + f"{i} : X O Lorem Ipsum" + "\033[0m")
# exit()


class TicTacToe:
    def __init__(self):
        self.field = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.score = {"x": 0, "o": 0}
        self.current_player = "x"


    def run(self):
        while True:
            self.print_board()
            self.handle_input()
            self.check()
            self.current_player = "x" if self.current_player == "o" else "o"

    def check(self):
        # win if all three in list the same
        # win if all first, second or third indecies are the same
        # win if indecies add up to 4 ()

        for index, row in enumerate(self.field):
            cols = [item[index] for item in self.field]
            if all(row) or all(cols):
                self.score[self.current_player] += 1
                return







    def handle_input(self):
        while True:
            try:
                player_choice = int(input(f"Player {color(self.current_player.upper())}, it's your turn: "))
            except ValueError:
                print("Your input must be a number between 1 and 9. Try again.")
                continue

            if not player_choice in range(1, 10):
                print("Your input must be in range from 1 to 9. Try again.")
                continue

            if not self.set_player_choice(player_choice):
                print("This slot is already taken.")
                continue

            break


    def set_player_choice(self, choice):
        x = (choice - 1) // 3
        y = (choice - 1) % 3

        slot = self.field[x][y]
        if slot: return False
        self.field[x][y] = self.current_player
        self.field[x][y]
        return True


    def print_board(self):
        os.system("cls")
        print(f" {blue('X')}: {self.score['x']} │ {cyan('O')}: {self.score['o']}")
        print("┌───┬───┬───┐")  # header

        counter = 1
        for i, row in enumerate(self.field, 1):
            print("│", end="")  # score row

            for item in row:
                print(f" {color(item) or grey(str(counter))} │", end="")
                counter += 1

            print()  # end of score row

            if len(self.field) == i:
                break

            print("├───┼───┼───┤")  # center piece

        print("└───┴───┴───┘")  # bottom


game = TicTacToe()
game.run()
