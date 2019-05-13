import random

class PlayerSearcher:
    def __init__(self, total_players):
        self.total_players = total_players

    def invite_players(self):
        joined_players = []
        for player_id in self.generate_player_ids():
            player = self.recruit_player(player_id)
            joined_players.append(player)
        return joined_players

    def generate_player_ids(self):
        starting_player_id = 1
        player_ids = range(starting_player_id, self.total_players+1)
        return player_ids

    def recruit_player(self, player_id):
        player_greeting_message = "Player {}, Please Enter your Name = ".format(player_id)
        player_name = input(player_greeting_message)
        player = Player(player_name)
        return player


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def increment_score(self):
        self.score += 1

    def play_turn(self):
        turn_message = "{}, Your turn!".format(self.name)
        print(turn_message)
        answer = input("What's the Answer? ")
        return answer

    def display_score(self):
        score_message = "{}, Your score is = {}".format(self.name, self.score)
        print(score_message)


class JumbleWordsGame:
    def __init__(self, players, words):
        self.players = players
        self.words = words

    def play(self, starting_turn):
        player = starting_turn
        while True:
            self.play_round(player)
            if self.willing_to_play_more():
                player = self.get_player_whose_turn_is_next(player)
            else:
                self.end_game()
                return

    def play_round(self, player):
        word = self.get_random_word()
        jumbled_word = self.jumble(word)
        print(jumbled_word)
        guessed_word = player.play_turn()
        correct_guess = self.guessed_correct_word(word, guessed_word)
        self.process_scores(player, correct_guess)

    def get_random_word(self):
        return random.choice(self.words)

    def jumble(self, word):
        jumbled_word = "".join(random.sample(word, len(word)))
        return jumbled_word

    def guessed_correct_word(self, expected_word, answer):
        return answer == expected_word

    def process_scores(self, player, correct_guess):
        if correct_guess:
            print("It's the Right answer!")
            player.increment_score()
        else:
            print("Better Luck, Next Time!")
        print("Your Score is = ", player.score)

    def willing_to_play_more(self):
        continue_message = "Press 1 to continue to next round and 0 to quit! "
        return int(input(continue_message))

    def get_player_whose_turn_is_next(self, last_player_to_play):
        player1_plays_the_turn = not (self.players[0] == last_player_to_play)
        return self.players[not player1_plays_the_turn]

    def end_game(self):
        self.display_scoreboard()
        self.display_thanks_message()

    def display_scoreboard(self):
        for player in self.players:
            player.display_score()

    def display_thanks_message(self):
        print("Thanks for Playing!")
        print("Have a nice day!")


if __name__ == '__main__':
    recruiter = PlayerSearcher(total_players=2)
    players = recruiter.invite_players()
    words = ('rainbow',
             'hello',
             'tom',
             'marvel',
             'thor',
             'ironman')
    game = JumbleWordsGame(players, words)
    game.play(starting_turn=players[0])
