
#!/usr/bin/env python3

import random

moves = ("rock", "paper", "scissors")


class Player:

    def cls_name(self):
        return self.__class__.__name__

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

    def __repr__(self):
        # assigned by game object when game starts
        return self._name


class RockPlayer(Player):
    pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input('Type "Rock" "Paper" or "Scissors": ').lower()
        if move not in moves:
            print("Sorry I don't understand.")
            return self.move()
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = None

    def move(self):
        if self.last_move:
            return self.last_move
        else:
            return random.choice(moves)

    def learn(self, _, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.last_move = random.choice(moves)
        self.moves = {"rock": "paper", "paper": "scissors", "scissors": "rock"}

    def move(self):
        return self.last_move

    def learn(self, my_move, _):
        self.last_move = self.moves[my_move]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.scoreboard = {p1: 0, p2: 0}
        self.p1 = p1
        self.p2 = p2
        self.p1._name = "Player1"
        self.p2._name = "Player2"

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        round_winner = self.round_winner(move1, move2)
        if round_winner is self.p1:
            self.scoreboard[self.p1] += 1
            print("Round winner is Player1!")
        elif round_winner is self.p2:
            self.scoreboard[self.p2] += 1
            print("Round winner is Player2!")
        else:
            print("Round is a tie!")
        print("{PlayerOne:", self.scoreboard[self.p1], ", PlayerTwo: ",
              self.scoreboard[self.p2], "}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def winner(self):
        if self.scoreboard[self.p1] > self.scoreboard[self.p2]:
            return self.p1
        elif self.scoreboard[self.p1] < self.scoreboard[self.p2]:
            return self.p2
        else:
            return None

    def round_winner(self, move1, move2):
        if move1 == move2:
            return False
        elif beats(move1, move2):
            return self.p1
        else:
            return self.p2

    def play_again(self):
        again = input(
            "Would you like to play again? Please type yes or no: ").lower()
        if again == "yes":
            game.play_game()
        elif again == "no":
            print("Thanks for playing!")
        else:
            pass

    def reset_game(self):
        self.scoreboard = {self.p1: 0, self.p2: 0}

    def play_game(self):
        self.reset_game()
        print("Game start!")
        for round in range(1, 4):
            print(f"Round {round}:")
            self.play_round()
        winner = self.winner()
        if winner:
            print("The winner is ", self.winner())
        else:
            print("It's a tie!")
        print("Game over!")
        game.play_again()


if __name__ == '__main__':
    strategies = {
        "1": RockPlayer(),
        "2": RandomPlayer(),
        "3": CyclePlayer(),
        "4": ReflectPlayer()
    }

    user_input = input("Select the player strategy \n"
                       "you want to play against\n"
                       "1- Rock Player\n"
                       "2- Random Player\n"
                       "3- Cycle Player\n"
                       "4- Reflect Player\n")
    print(f"You selected {strategies[user_input].cls_name()} to be PlayerTwo")
    print("You are PlayerOne.")
    PlayerOne = HumanPlayer()
    PlayerTwo = strategies[user_input]
    game = Game(PlayerOne, PlayerTwo)
    game.play_game()
