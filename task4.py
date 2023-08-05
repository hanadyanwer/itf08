
def triangle_area(base:float,height:float):
    triangle_area = 0.5*base*height
    return triangle_area
def circle_area(radius:float):
    retcircle_area = 3.14 * (radius ** 2)
    return retcircle_area
def rectangle_area(length:float,width:float):
    rectangle_area= length * width
    return rectangle_area

aera = -1
def space_check(aera):
    if aera >=10:
        print("aera is large")
    elif aera<10 and aera>0:
        print("aera is small")
    elif aera ==  0:
        print("invalid valuo")
    else:
        print("other")
arae = space_check(aera)