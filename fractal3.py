import turtle as t
t.speed(0)


def tapis(n,longueur):
    
    if n==1:
        t.fillcolor ("black")
        t.begin_fill ()
        t.up()
        t.forward(longueur/3)
        t.left(90)
        t.forward(longueur/3)
        t.down()
        for i in range(4):
            t.forward(longueur/3)
            t.right(90)
        t.up()
        t.right(180)
        t.forward(longueur/3)
        t.right(90)
        t.forward(longueur/3)
        t.right(90)
        t.end_fill()
        
    else:
        for i in range(3):
            tapis(n-1,longueur/3)
            t.forward(longueur/3)
            t.right(90)
        t.right(90)
        t.forward(longueur/3)
        t.left(90)
        t.forward(longueur/3)
        for i in range(2):
            tapis(n-1,longueur/3)
            t.right(90)
            t.forward(longueur/3)
        t.right(180)
        t.forward(longueur/3)
        t.left(90)
        for i in range(2):
            tapis(n-1,longueur/3)
            t.right(90)
            t.forward(longueur/3)
        t.right(90)
        t.forward(longueur/3)
        t.right(180)
        tapis(n-1, longueur/3)
        t.left(90)
        t.forward(longueur/3)
        t.left(180)
        tapis(n-1,longueur)
        
        


t.up()
t.goto(-300,-100)
t.down()
for i in range(4):
    t.forward(300)
    t.left(90)
tapis(3,300)

t.exitonclick()