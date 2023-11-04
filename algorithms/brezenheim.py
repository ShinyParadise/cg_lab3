def brezenheim(beginX, beginY, endX, endY) -> list:
    points = []
    x = beginX
    y = beginY
    deltaX = (endX - beginX) * 2
    deltaY = (endY - beginY) * 2
    delta = - deltaX

    while x <= endX:
        points.append((int(x), int(y)))
        x += 1
        delta += deltaY
        if delta >= 0:
            y += 1
            delta -= deltaX

    return points
