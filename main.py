### The project idea was tech with tims, but the code is mine (I did not look at his repo)###
import random
import turtle


class racer:

    def __init__(self, color, starting):
    
        #defining other vars
        self.color = color
        
        #define the starting y position
        self.pos = -400
        self.starting = starting
        #creat a turtle instance and set color/shape
        self.turtle = turtle.Turtle()
        self.turtle.color(self.color)
        self.turtle.shape('turtle')
        
        #get the turtle oriented and at the starting position
        self.turtle.penup()
        self.turtle.left(90)
        self.turtle.goto(self.starting, self.pos)
        self.turtle.pendown()
    
    def move(self):
        self.pos += random.randint(1,20)
        self.turtle.goto(self.starting, self.pos)


def main():  
    winning_tutle = [0,'place']
    window =turtle.Screen()
    window.setup(1000,1000)

    my_turtles = ['blue','orange','red','black','purple', 'green']
    game = True

    for index,color in enumerate(my_turtles):
        my_turtles[index] = racer(color, index*140-350)

    while game:
        for t in my_turtles:
            t.move()
            if t.pos > 400 and t.pos > winning_tutle[0]:
                winning_tutle[0] = t.pos
                winning_tutle[1] = t.color
                game = False
    print(winning_tutle[1])
    

if __name__ == "__main__":
    main()


