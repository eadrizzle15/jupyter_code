class Person:
    def __init__(self, name, birthyear, area, id):
        self.name = name
        self.birthyear = birthyear
        self.area = area
        self.age = 2022 - birthyear
        self.id = id

    # display data
    def displayInfo(self):
        profile = f'''    VOTER'S PROFILE
Voter's name:              {self.name}
Voter's birth year:        {self.birthyear}
Voter's area of residence: {self.area}
Voter's age:               {self.age}
Voter's ID number:         {self.id}'''


def search():
    number = int(input("Enter the number: "))
    array_1 = range(101)
    if number in array_1:
        print("Number found!")
        print(f": {number}")
    else:
        array_2 = array_1[:0.5*array_1[-1]]
        if number in array_2:
            print
