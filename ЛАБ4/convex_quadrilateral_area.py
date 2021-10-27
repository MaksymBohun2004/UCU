def four_lines_area(koef1, c1, koef2, c2, koef3, c3, koef4, c4):
    """ Function returns the area of a quadrangle
    """
    x1, y1 = lines_intersection(koef1,c1,koef2,c2)
    x2, y2 = lines_intersection(koef2,c2,koef3,c3)
    x3, y3 = lines_intersection(koef3,c3,koef4,c4)
    x4, y4 = lines_intersection(koef1,c1,koef4,c4)
    side_a = distance(x1,y1,x2,y2)
    side_b = distance(x2,y2,x3,y3)
    side_c = distance(x3,y3,x4,y4)
    side_d = distance(x1,y1,x4,y4)
    diagonal1 = distance(x1,y1,x3,y3)
    diagonal2 = distance(x2,y2,x4,y4)
    area = quadrangle_area(side_a,side_b,side_c,side_d,diagonal1,
    diagonal2)
    return area
def lines_intersection(koef1, c1, koef2, c2):
    """ Function returns coordinates where two
    lines meet
    """
    if koef1 == koef2:
        return None
    else:
        x = (c2 - c1) / (koef1 - koef2)
        y = round(koef1 * x + c1,2)
        x = round(x,2)

        return x , y

def distance(x1, y1, x2, y2):
    """Function returns the distance between two points
    """
    try :
        side = round(((y1 - y2)**2 + (x1 - x2)**2)**0.5,2)
    except TypeError:
        return None
    return side

def quadrangle_area(side_a, side_b, side_c, side_d, diagonal1, \
    diagonal2):
    try:
        area = round(((4 * diagonal1**2 * diagonal2**2 - (side_b**2 +
    side_d**2 - side_a**2 -side_c**2)**2)/16)**0.5, 2)
    except TypeError:
        return None
    return area
print(four_lines_area(0,20,3,-0.3,0.1,10,-5,3))
