def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    for count in range(4):
        forward(end.x - start.x)
        left(120)
    end_fill()
    
def circle_(start, end):
    "Draw circle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    x_c=int(start.x)
    y_c=int(start.y)
    
    for count in range(1):
        circle(start.x-end.x)

    end_fill()

onkey(lambda: color('magenta'), 'M')
