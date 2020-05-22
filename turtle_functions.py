import turtle
def main():
    window = turtle.Screen()
    Juan = turtle.Turtle()

    make_square(Juan)
    turtle.mainloop()


def make_square(juan):
    length = int(input('Digite el tamaño del lado del cuadrado: '))

    for i in range (4):
        make_line_and_turn(juan, length)


def make_line_and_turn(juan, length):
    juan.forward(length)
    juan.left(90)



if __name__ == "__main__":
    main()