import turtle as t

t.speed(100)  # drawing speed
t.bgcolor("black")  # sets background colour to black
t.pensize(3)


def tree(branchLen, t):  # make function for branches
    if branchLen > 4:
        t.forward(branchLen)  # first go to forward
        t.right(20)  # 20 steps right
        tree(branchLen-15, t)  # goes to backwards -15
        t.left(40)  # goes to the left 40 steps
        tree(branchLen-15, t)  # goes backwards -15
        t.right(20)  # 20 steps to the right
        t.backward(branchLen)
# 20 steps right


def main():
    myWin = t.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.colour("green")
    tree(105, t)
    myWin.exitonclick()


main()
