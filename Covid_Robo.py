class Robo:
    def __init__(self):
        self.dir_list=['N','E','S','W']
    def move(self):
        if self.dir=='N':
            self.y=self.y+1
        elif self.dir=='W':
            self.x=self.x-1
        elif self.dir=='S':
            self.y=self.y-1
        elif self.dir=='E':
            self.x=self.x+1

        assert (self.x<=self.max_x and self.x>=0 or
                self.y <=self.max_y and self.y>=0
                ),'x, y Movement Out of Bound'

    def process(self):

        self.max_x,self.max_y=map(int,input().split())
        self.x,self.y,self.dir=input().split(' ')
        self.x=int(self.x)
        self.y=int(self.y)
        self.position=self.dir_list.index(self.dir)
        instructions=input()
        for i in instructions:
            if i=='M':
                self.move()
            elif i=='L':
                self.position=(self.position -1)%4
            elif i=='R':
                self.position=(self.position +1)%4
            self.dir=self.dir_list[self.position]
        print(self.x,self.y,self.dir)
if __name__ == '__main__':

    a=Robo()
    a.process()
