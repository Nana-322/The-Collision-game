from graphics import *
from random import randint

def Flash(circ1,circ2):
    '''Generate a random color for circ1 and paint circ2 with its complimentary color'''
    r = randint( 0, 255 )
    g = randint( 0, 255 )
    b = randint( 0, 255 )
    color1 = color_rgb( r, g, b )
    color_comp = color_rgb(255-r,255-g,255-b)
    circ1.setFill(color1)
    circ2.setFill(color_comp)

def DoCircsCollide( circ1, circ2 ):
    '''Boolean function: returns True only if
    the two circles collide/overlap.
    circ1 and circ2 are circle objects.'''
    
    #Extract data from two circle objects:
    p1 = circ1.getCenter()
    r1 = circ1.getRadius()
    x1 = p1.getX()
    y1 = p1.getY()
    
    p2 = circ2.getCenter()
    r2 = circ2.getRadius()
    x2 = p2.getX()
    y2 = p2.getY()

    # Square of center-to-center distance:
    centdist2 = (x1-x2)**2 + (y1-y2)**2
    
    if centdist2 < (r1+r2)**2:
        # Collide/overlap:
        return True
    else:
        return False
        # Note: Returns False if just tangent.
        
def main():
    win = GraphWin("Collide", 500,500)
    win.setCoords(-100,-100,100,100)
    win.setBackground("purple")

    p1 = Point(randint(90,100),randint(-100,-95))
    r1 = 5
    circ1 = Circle(p1,r1)
    circ1.setFill("pink")
    circ1.draw(win)

    p2 = Point(randint(-100,90),randint(-90,100))
    r2 = 40
    circ2 = Circle(p2,r2)
    circ2.setFill("black")
    circ2.draw(win)

    while True:
        key = win.getKey()
        print("key=",key)
        dx=0
        dy=0
        if key == "Right":
            dx=5
        elif key == "Left":
            dx=-5
        elif key == "Up":
            dy=5
        elif key == "Down":
            dy=-5
        circ1.move(dx,dy)
        
        if key == "period":
            break
            print("Out of loop")
        elif DoCircsCollide(circ1,circ2):
            print("Collission!!!")
            for i in range(100):
                Flash(circ1,circ2)
            
    win.getMouse()
    win.close()
main()


                   
                   
    
