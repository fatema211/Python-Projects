import turtle as t
import random

tim = t.Turtle()
#replace the color dic with a rgb method
t.colormode(255)
#create a method to generate random color
def Random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # tuple
    random_color = (r, g, b)
    return random_color

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#function to create shapes
def shape_num(num_side):
    angle = 360 / num_side
    for _ in range(num_side):

        tim.forward(120)
        tim.right(angle)

#define dynamic number side
'''for num_side in range(3, 11):
    tim.color(random.choice(colours))
    shape_num(num_side)'''
# add color
directions = [0, 90, 180, 270]
tim.width(10)
tim.speed("fastest")
for _ in range(200):
    tim.color(Random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))