import random


class GameMatrix():

    def __int__(self, number):
        self.mat = None
        self.number = number
    def start_game(self):
        self.mat = []
        for i in range(self.number):
            self.mat.append([0] * self.number)

        print("Commands are as follows : ")
        print("'W' or 'w' : Move Up")
        print("'S' or 's' : Move Down")
        print("'A' or 'a' : Move Left")
        print("'D' or 'd' : Move Right")

        # calling the function to add
        # a new 2 in grid after every step
        self.add_new()
        print(self.mat)
    def add_new(self):

        row = random.randint(0,self.number)
        col = random.randint(0,self.number)
        # print(row,col)
        # print(self.mat[row][col])
        while (self.mat[row][col] != 0):
            row = random.randint(0, self.number)
            col = random.randint(0, self.number)

        self.mat[row][col] = 2
        print(self.mat)


a = GameMatrix()
a.number = 4
a.start_game()