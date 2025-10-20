import turtle as t
#zoomIn is the size of the graph, zoomIn == 10 will output a 10x10 grid
zoomIn = t.textinput("Graph size","Enter graph size (1 is 1x2, 2 is 2x2 and so on): ")
t.speed(0)
t.penup()
t.goto(-200,-200)
t.pendown()
#calculates the size of each box in the graph. Every graph is 400x400 pixels
boxSize = 400/int(zoomIn)
#draws the graph. There is some inefficiency as the turtle draws a full square for each box
for i in range(int(zoomIn)):
    for j in range(int(zoomIn)):
        t.forward(boxSize)
        t.left(90)
        t.forward(boxSize)
        t.left(90)
        t.forward(boxSize)
        t.left(90)
        t.forward(boxSize)
        t.left(90)
        t.forward(boxSize)
    t.left(180)
    t.forward(400)
    t.right(90)
    t.forward(boxSize)
    t.right(90)
#draws the x and y axis on the graph, intersecting at (0,0)
t.penup()
t.goto(0,-200)
t.pendown()
t.width(4)
t.goto(0,200)
t.penup()
t.goto(-200,0)
t.pendown()
t.goto(200,0)
t.width(1)

#graphNum keeps track of how many graphs have been written
graphNum = 0
#textY is the y-coordinate of where the graph equations will be written
textY = 200
while True:
    graphNum += 1
    #text input field for the graph
    graphIn = t.textinput("Graph " + str(graphNum), "Graph in: y = ")
    t.penup()
    x = -200
    #uses the exec function to turn the graphIn input string into a working equation
    exec("y = " + graphIn)
    t.goto(x, int(y))
    x+=boxSize
    t.pendown()
    while x <= 200:
        #Because of how this was coded, I have to scale x down, calculate y, then scale them both back
        x = x/boxSize
        exec("y = " + graphIn)
        x = x*boxSize
        t.goto(x, int(y*boxSize))
        print(x)
        x+=boxSize
    t.penup()
    t.goto(250,textY)
    t.pendown()
    #writes the number of the graph that has just been plotted
    t.write("Graph " + str(graphNum) + ":", align="left", font=("Courier", 12, "normal"))
    textY -= 20
    t.penup()
    t.goto(250,textY)
    t.pendown()
    #writes the equation of the graph that has just been plotted
    t.write("y=" + graphIn, align="left", font=("Courier", 12, "normal"))
    textY -= 20
    t.penup()
