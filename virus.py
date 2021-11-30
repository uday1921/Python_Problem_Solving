from turtle import *
import turtle


win = turtle.Screen()
speed(100)
color('cyan')
bgcolor('black')
b=200
while b > 0:
    left(b)
    forward(b*3)
    b = b - 1
while True:
    win.update()


