from graphics import*
import math

def arrows (p, hoop):
    x= p.getX()- hoop.getCenter().getX()
    y= p.getY()- hoop.getCenter().getY()
    distance= math.sqrt(x**2 + y**2)
    return distance <= hoop.getRadius()

def main():
    win = GraphWin("Archery", 400, 400)
    white= Circle(Point(200, 100), 100)
    white.setFill("white")
    white.draw(win)
    black= Circle(Point(200, 100), 80)
    black.setFill("black")
    black.draw(win)
    blue= Circle(Point(200, 100), 60)
    blue.setFill("blue")
    blue.draw(win)
    red= Circle(Point(200, 100), 40)
    red.setFill("red")
    red.draw(win)
    yellow= Circle(Point(200, 100), 20)
    yellow.setFill("yellow")
    yellow.draw(win)
    message= Text(Point(80, 20), "Total Score : 0")
    message.draw(win)
    message2= Text(Point(80, 40), "")
    message2.draw(win)
    
    totalscore = 0

    for i in range (0,5):
        p = win.getMouse()
        arrow= Circle(p, 5)
        arrow.setFill ("orange")
        arrow.setOutline("orange")
        arrow.draw(win)
        if (arrows(p, yellow)):
            totalscore = totalscore + 9
            score=9
        elif (arrows(p, red)):
            totalscore = totalscore + 7
            score=7
        elif (arrows(p, blue)):
            totalscore = totalscore + 5
            score=5
        elif (arrows(p, black)):
            totalscore = totalscore + 3
            score=3
        elif (arrows(p, white)):
            totalscore = totalscore + 1
            score=1
        else:
            totalscore = totalscore + 0
            score=0
        totalscore= totalscore
        
    message.setText("Total Score : " + str(totalscore))
    message2.setText("Score : " + str(score))
    win.getMouse()
    win.close()

main()
