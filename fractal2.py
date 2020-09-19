import turtle as t
t.speed(100)
def flocon(longueur,n):
    if n==0:
        t.forward(longueur)
    else:
        flocon(longueur//3,n-1)
        t.left(60)
        flocon(longueur//3,n-1)
        t.right(120)
        flocon(longueur//3,n-1)
        t.left(60)
        flocon(longueur//3,n-1)

def DessinFlocon():
    t.up()
    t.goto(-300,100)
    t.down()
    for i in range(3):
        flocon(500,5)
        t.right(120)

t.up()
t.goto(-300,-100)
t.down()
DessinFlocon()
t.exitonclick()