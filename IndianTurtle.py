try:
    try:
        print('''   Notice:
        The following program is made by Devik.
        ''')

        def draw():

            # Phase 1: Settings
            proportion = input('''What is the size of the flag? Enter a value greater than 53. This value is going to be 
        the height of the flag. Press enter to get a default number, 131. ''')
            if proportion == '':
                proportion = int(131)
            else:
                proportion = int(proportion)
            if proportion > 53:
                import tutrle
                t = tutrle.Pen()
                tu = tutrle.Pen()
                tur = tutrle.Pen()
                t.pensize(2)
                tutrle.bgcolor("silver")
                t.shape('turtle')
                t.hideturtle()
                tu.hideturtle()
                tur.hideturtle()

                # Phase 2: Flag, -chakra
                t.fillcolor('orange')
                t.begin_fill()
                t.forward(3 * proportion/2)
                t.right(90)
                t.forward(proportion/3)
                t.right(90)
                t.forward(3 * proportion/2)
                t.right(90)
                t.forward(proportion/3)
                t.left(180)
                t.end_fill()
                t.forward(proportion/3)
                t.left(90)

                t.fillcolor('white')
                t.begin_fill()
                t.forward(3 * proportion/2)
                t.right(90)
                t.forward(proportion/3)
                t.right(90)
                t.forward(3 * proportion/2)
                t.right(90)
                t.forward(proportion/3)
                t.left(180)
                t.end_fill()
                t.forward(proportion/3)
                t.left(90)

                t.fillcolor('green')
                t.begin_fill()
                t.forward(3 * proportion/2)
                t.right(90)
                t.forward(proportion/3)
                t.right(90)
                t.forward(3 * proportion/2)
                t.right(90)
                t.forward(proportion/3)
                t.left(180)
                t.end_fill()
                t.forward(proportion/3)
                t.left(90)

                # Phase 3: Flag, +chakra
                t.penup()
                t.forward(3 * proportion/4)
                t.left(90)
                t.forward(proportion/2)
                t.pendown()
                t.pensize(2)
                t.color('blue')
                i = 0
                while i < 24:
                    i += 1
                    t.left(15)
                    t.forward(proportion/6)
                    t.backward(proportion/6)
                t.forward(proportion/6)
                t.left(90)
                t.circle(proportion/6)

                # Phase 4: flag.txt
                t.penup()
                t.left(90)
                t.forward(proportion * 1.25)
                t.right(90)
                t.forward(3 * proportion/6)
                t.pendown()
                t.write("Happy", font=("Arial", int(proportion/4), "normal"))
                t.penup()
                t.left(90)
                t.forward(proportion/4)
                t.pendown()
                t.write("Independence", font=("Arial", int(proportion/4), "normal"))
                t.penup()
                t.forward(proportion/4)
                t.pendown()
                t.write("Day!", font=("Arial", int(proportion / 4), "normal"))
                t.penup()
                t.forward(proportion/4)
                t.pendown()
                t.write("August 15th", font=("Arial", int(proportion / 4), "normal"))

                # Phase 5: Fireworks! 100% optional.
                t.pensize(1)
                TemporaryVar = int(3 * proportion/2)
                t.speed('fastest')
                tu.speed('fastest')
                tur.speed('fastest')
                import random
                while True:
                    colorList = ['crimson', 'yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple',
                                 'navy', 'blue', 'skyblue', 'cyan', 'turquoise', 'lightgreen', 'green', 'darkgreen',
                                 'chocolate', 'brown', 'black', 'gray', 'white', 'hotpink', 'beige', 'tomato',
                                 'palevioletred']
                    randomI = random.randint(1, len(colorList))
                    t.pencolor(colorList[randomI - 1])
                    tu.pencolor(colorList[randomI - 1])
                    tur.pencolor(colorList[randomI - 1])
                    spikeNum = random.randint(3, 90)
                    t.penup()
                    tu.penup()
                    tur.penup()
                    if random.randint(0, 1):
                        x1 = random.randint(0, 250)
                        y = random.randint(50, 250)
                        t.goto(x1, y)
                        x1 = random.randint(0, 250)
                        y = random.randint(50, 250)
                        tu.goto(x1, y)
                        x1 = random.randint(0, 250)
                        y = random.randint(50, 250)
                        tur.goto(x1, y)
                    else:
                        x2 = random.randint(TemporaryVar, 250)
                        y = random.randint(50, 250)
                        t.goto(x2, y)
                        x2 = random.randint(TemporaryVar, 250)
                        y = random.randint(50, 250)
                        tu.goto(x2, y)
                        x2 = random.randint(TemporaryVar, 250)
                        y = random.randint(50, 250)
                        tur.goto(x2, y)
                    t.pendown()
                    tu.pendown()
                    tur.pendown()
                    i = 0
                    while i < spikeNum * 2:
                        i += 1
                        t.pencolor(colorList[randomI - 1])
                        tspikesize = random.randint(20, 100)
                        t.left(180 / spikeNum)
                        t.forward(tspikesize)
                        t.backward(tspikesize)

                        tu.pencolor(colorList[randomI - 1])
                        uspikeSize = random.randint(20, 100)
                        tu.left(180/spikeNum)
                        tu.forward(uspikeSize)
                        tu.backward(uspikeSize)

                        tur.pencolor(colorList[randomI - 1])
                        rspikeSize = random.randint(20, 100)
                        tur.left(180 / spikeNum)
                        tur.forward(rspikeSize)
                        tur.backward(rspikeSize)

            else:
                print('The value that you entered is less than 53.')
                draw()
        draw()
        raise Exception('Why did you place a break? The loop is supposed to run forever')
        # Just for fun! Or if a break statement occurs.
        # One of my best friends who has no programming experience: That's it? All that code for that?
        # At that time I only had the flag, but hey, it is complicated.
        # There is a possibility of 4 more improvements on this:
        # 1: Add stick figure kids at the bottom
        # 2: Make the kids more human
        # 3: Add a pole to the flag
        # 4: Make flowers fall from the flag
    except 'Terminator':
        print()
except TypeError:
    print()

