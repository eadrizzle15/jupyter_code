from person import Person
from candidate import Candidate

class Election:
    voter_ids = []
    voters_register = []
    candidates = [
        Candidate('AMEYAW EVANS', 1),
        Candidate('WIKIREH HAKEEM', 2),
        Candidate('MARSH ROBERT', 3),
        Candidate('USSHER OTHNIEL', 4),
    ]

    def registerPeople(self, numberOfPeople):
        i = 0
        while i < numberOfPeople:
            voter_name = input("Please enter your name: ")
            voter_birthyear = int(input("Please enter your birth year: "))
            voter_area = input("Please enter your area of residence: ")
            voter_age = 2022 - voter_birthyear
            voter_number = int(input("Enter your four-digit voter's id number here: "))
            voter_profile = Person(voter_name, voter_birthyear, voter_area, voter_number)

            voter_profile.displayInfo()
        
            if voter_age < 18 :
                print("Please you are not eligible to vote!")
            else:
                self.voters_register.append(voter_profile)
                self.voter_ids.append(voter_profile.id)
        
            i += 1

    def vote(self):
        voted = []
        total_vote = 0
        while total_vote < len(self.voters_register):
            ID = int(input("Please enter your voter's id number: "))
            if ID in self.voter_ids:
                if ID in voted:
                    print(f"Voter with voter's id number {ID} has voted already") 
                else:
                    print('CANDIDATES')
                    print('-' * 20)
                    
                    i = 0
                    while i < len(self.candidates):
                        print(f'{i + 1}.' + ' ' * 15 + self.candidates[i].name)
                        i += 1

                    vote = int(input("Enter your candidate's number: "))

                    voted.append(ID)

                    if vote == 1:
                        self.candidates[0].addVote()
                    elif vote == 2:
                        self.candidates[1].addVote()
                    elif vote == 3:
                        self.candidates[2].addVote()
                    elif vote == 4:        
                        self.candidates[3].addVote()

                    print("You have voted successfully!")
            
            total_vote += 1
        
        # calculate total votes after no more voters are available
        self.calculateVotes()

    def calculateVotes(self):
        i = 0
        totalvotes = 0
        candidate1Votes = self.candidates[0].votes
        candidate2Votes = self.candidates[1].votes
        candidate3Votes = self.candidates[2].votes
        candidate4Votes = self.candidates[3].votes

        while i < 4:
            totalvotes += self.candidates[i].votes
            i += 1
        i = 0
        candidatesvotes = []
        while i < 4:
            percentage = (self.candidates[i].votes/totalvotes) * 100
            print(f'{i + 1}.' + ' ' * 15 + self.candidates[i].name + ' ' * 10 + str(self.candidates[i].votes) + {''*10} + f"{percentage}%")
            candidatesvotes.append(self.candidates[i].votes)
            i += 1
        if max(candidatesvotes) == self.candidates[0].votes:
            print(f"{self.candidates[0].name} is the winner with {candidate1Votes}.")
        if max(candidatesvotes) == self.candidates[1].votes:
            print(f"{self.candidates[1].name} is the winner with {candidate2Votes}.")
        if max(candidatesvotes) == self.candidates[2].votes:
            print(f"{self.candidates[2].name} is the winner with {candidate3Votes}.")
        if max(candidatesvotes) == self.candidates[3].votes:
            print(f"{self.candidates[3].name} is the winner with {candidate4Votes}.")