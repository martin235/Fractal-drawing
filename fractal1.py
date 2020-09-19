import turtle as t
t.speed(100)
def Triangles(longueur,n):
    if n==0:
        t.color("black")
        t.begin_fill()
        for i in range(3):
            t.forward(longueur)
            t.left(120)
        t.end_fill()

    else:
        Triangles(longueur//2,n-1)
        t.forward(longueur//2)
        Triangles(longueur//2,n-1)
        t.left(120)
        t.forward(longueur//2)
        t.right(120)
        Triangles(longueur//2,n-1)
        t.right(120)
        t.forward(longueur//2)
        t.left(120)
        
def DessinFlocon():
    t.up()
    t.goto(-300,100)
    t.down()
    for i in range(3):
        flocon(500,3)
        t.right(120)

t.up()
t.goto(-300,-100)
t.down()
Triangles(500,4)
t.exitonclick()