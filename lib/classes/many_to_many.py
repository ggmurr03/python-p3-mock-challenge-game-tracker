class Game:
    def __init__(self, title):
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value) > 0 and not hasattr(self, "title"):
            self._title = value

    def results(self):
        return [result for result in Result.all if self == result.game]

    def players(self):
        return list(
            set([result.player for result in self.results() if self == result.game])
        )

    def average_score(self, player):
        pass


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if isinstance(value, str) and 2 < len(value) < 16:
            self._title = value

    def results(self):
        return [result for result in Result.all if self == result.player]

    def games_played(self):
        return list(
            set([result.game for result in self.results() if self == result.player])
        )

    def played_game(self, game):
        return any(innergame == game for innergame in self.games_played())

    def num_times_played(self, game):
        pass


class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.__class__.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if isinstance(value, int) and 1 < value > 5000 and not hasattr(self, "score"):
            self._score = value

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, value):
        if type(value) == Player:
            self._player = value


game = Game("Skribbl.io")
game2 = Game("Skribbl.i22222o")
player_1 = Player("Saaammmm")
player_2 = Player("ActuallyTopher")
result_1 = Result(player_1, game, 2000)
result_2 = Result(player_1, game, 3500)
result_3 = Result(player_2, game, 190)

print(result_3.all)
player_1.results()
print(player_1.played_game(game2))
