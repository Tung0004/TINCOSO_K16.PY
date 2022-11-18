# invite mylove
from turtle import *

color('pink')

speed(45)
hideturtle()

def curve():
    for i in range (200):
        right(1)
        forward(1)
begin_fill()

left(140)
forward(113)

curve()

forward(112)
end_fill

up()
setpos(-50,95)
down()
color('red')
write('MYLOVE', font=('arial',13, 'bold'))

done()