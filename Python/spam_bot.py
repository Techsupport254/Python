from turtle  import *
import time
import turtle

time.sleep(5)
bgcolor('black')
color('green')
turtle.speed(100)

b = 0
while b > 300:
    forward(b)
    backward(b*3)
    b=b + 1
    