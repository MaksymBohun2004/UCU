# ****************************************
# Problem 19
# ****************************************
def polygon_area(vertices):
    """
    Calculates the area of a 3 or 4-angled figure 
    using the locations of it's points.
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    """
    if len(vertices) == 3:
          a1 = 0
          a2 = 0
          b1 = 0
          b2 = 0
          c1 = 0
          c2 = 0
          for point in vertices:
                if point == vertices[0]:
                  a1 = point[0]
                  a2 = point[1]
                elif point == vertices[1]:
                  b1 = point[0]
                  b2 = point[1]
                elif point == vertices[2]:
                  c1 = point[0]
                  c2 = point[1]
          print(a1,a2,b1,b2,c1,c2)
          lengthAB = ((b1 - a1)**2 + (b2 - a2)**2)**0.5
          lengthBC = ((c1 - b1)**2 + (c2 - b2)**2)**0.5
          lengthAC = ((c1 - a1)**2 + (c2 - a2)**2)**0.5
          p = (lengthAB + lengthBC + lengthAC)/2
          s = (p*(p - lengthAB)*(p - lengthBC)*(p - lengthAC))**0.5
          return s
          
    elif len(vertices) == 4:
      x1 = 0
      y1 = 0
      x2 = 0
      y2 = 0
      x3 = 0
      y3 = 0
      x4 = 0
      y4 = 0
    
      for i in range(0,len(vertices)):
        if i == 0:
          x1 = vertices[i][0]
          y1 = vertices[i][1]
        elif i == 1:
          x2 = vertices[i][0]
          y2 = vertices[i][1]
        elif i == 2:
          x3 = vertices[i][0]
          y3 = vertices[i][1]
        elif i == 3:
          x4 = vertices[i][0]
          y4 = vertices[i][1]
    print(x1,y1,x2,y2,x3,y3,x4,y4)
    s = (abs(((x1 * y2) - (x2 * y1)) + ((x2 * y3) - (x3 * y2)) + ((x3 * y4) - (x4 * y3)) + ((x4 * y1) - (x1 * y4))))/2
    return s

