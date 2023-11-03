def DDA(x1, y1, x2, y2) -> list:
    points = []
    if abs(x2 - x1) >= abs(y2 - y1):
        length = abs(x2 - x1)
    else:
        length = abs(y2 - y1)

    dx = (x2 - x1) / length
    dy = (y2 - y1) / length

    x = x1 + 0.5 * sign(dx)
    y = y1 + 0.5 * sign(dy)

    i = 1
    while i <= length:
        points.append((int(x), int(y)))
        x = x + dx
        y = y + dy
        i += 1

    return points


def sign(x):
    if (x > 0):
        return 1
    else:
        return -1
