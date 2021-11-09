class stats:
    wins = 0
    losses = 0
    ties = 0
    def __init__(self, wins, losses, ties):
        self.wins = 0
        self.losses = 0
        self.ties = 0

    def stattrack(self):
        print("You have ", self.wins, " wins, ", self.ties, " tied games, and ", self.losses, " losses.")
    def incrementwins(self):
        self.wins += 1
        self.stattrack()
    def incrementlosses(self):
        self.losses += 1
        self.stattrack()
    def incrementties(self):
        self.ties += 1
        self.stattrack()