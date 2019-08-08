Python 3.7.2 (v3.7.2:9a3ffc0492, Dec 24 2018, 02:44:43) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Turtle Graphics Game – Space Turtle Chomp

>>> import turtle
>>> turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('navy')
SyntaxError: multiple statements found while compiling a single statement
>>> wn =  turtle.Screen()
>>> wn.bgcolor('navy')
>>> #wn is the name we are calling the screen
>>> #bgcolor allows us to set the background colour
>>> # Create player turtle
player = turtle.Turtle()
player.color('darkorange')
player.shape('turtle')
player.penup()
SyntaxError: multiple statements found while compiling a single statement
>>> player = turtle.Turtle()
>>> player.color('darkorange')
>>> player.shape('turtle')
>>> player.penup()
>>> #Penup means that the turtle shape
>>> # Set speed variable
speed = 1
>>> speed = 1
>>> while True:
    player.forward(speed)


=============================== RESTART: Shell ===============================
>>> import turtle
>>> turtle.setup(650,650)
>>> wn = turtle.Screen()
>>> wn.bgcolor('navy')
>>> player = turtle.Turtle()
>>> player.color('darkorange')
>>> player.shape('turtle')
>>> player.penup()
>>> player = turtle.Turtle()
>>> player.color('darkorange')
>>> player.shape('turtle')
>>> player.penup()
>>> speed = 1
>>> while True:
	player.forward(speed)
	
