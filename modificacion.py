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

onkey(lambda: color('magenta'), 'M')
