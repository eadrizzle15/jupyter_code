class Candidate:
    def __init__(self, name, id, votes = 0):
        self.id = id
        self.name = name
        self.votes = votes

    def addVote(self):
        self.votes += 1