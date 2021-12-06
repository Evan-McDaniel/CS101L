import turtle

class Point(object):
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color = color
    def draw(self):
        turtle.penup()
        turtle.goto(self.x,self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()
    def draw_action(self):
        turtle.dot()

class Box(Point):
    def __init__(self,x1,y1,width,height,color):
        super().__init__(x1,y1,color)
        self.width = width
        self.height = height
    def draw_action(self):
        for i in range(2):
            turtle.forward(self.width)
            turtle.rt(90)
            turtle.forward(self.height)
            turtle.rt(90)


class BoxFilled(Box):
    def __init__(self,x1,y1,width,height,color,fillcolor):
        super().__init__(x1,y1,width,height,color)
        self.FillColor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.FillColor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self,x,y,color,radius):
        super().__init__(x,y,color)
        self.radius = radius
    def draw_action(self):
        turtle.circle(self.radius)

class CircleFilled(Circle):
    def __init__(self,x,y,color,radius,fillcolor):
        super().__init__(x,y,color,radius)
        self.FillColor = fillcolor
    def draw_action(self):
        turtle.fillcolor(self.FillColor)
        turtle.begin_fill()
        super().draw_action()
        turtle.end_fill()


b = Box(50,50,80,80,'orange')
b.draw()

bf = BoxFilled(135,135,80,80,'blue','orange')
bf.draw()

c = Circle(-120,-140, 'orange',150)
c.draw()

cf = CircleFilled(-100,180,'blue',50,'orange')
cf.draw()

num = input()





