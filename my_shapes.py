from shapes import Triangle, Rectangle, Oval
rect1 = Rectangle()
rect1.set_width(200)
rect1.set_height(100)
rect1.set_color("blue")
rect1.draw()
rect2 = Rectangle()
rect2.set_width(50)
rect2.set_height(150)
rect2.set_color("yellow")
rect2.set_x(150)
rect2.set_y(100)
rect2.draw()
tri = Triangle(5, 5, 100, 5, 100, 200)
tri.set_color("red")
tri.draw()
egg = Oval()
egg.set_color("tan")
egg.set_height(200)
egg.set_width(150)
egg.set_x(250)
egg.set_y(10)
egg.draw()
star1 = Triangle(5,300,55,350,105,300,'black')
star1.draw()
star2 = Triangle(5,325,55,275,105,325,'black')
star2.draw()
cir = Oval()
cir.set_color("green")
cir.set_height(50)
cir.set_width(50)
cir.set_x(150)
cir.draw()