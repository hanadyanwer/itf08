
def triangle_area(base:float,height:float):
    triangle_area = 0.5*base*height
    space_check(triangle_area)
def circle_area(radius:float):
    circle_area = 3.14 * (radius ** 2)
    space_check(circle_area)
def rectangle_area(length:float,width:float):
    rectangle_area= length * width
    space_check(rectangle_area)


def space_check(aera):
    print(f"area is {aera}")
    if aera >=10:
        print("aera is large")
    elif aera<10 and aera>0:
        print("aera is small")
    elif aera ==  0:
        print("invalid valuo")
    else:
        print("other")
triangle_area(4,5)
circle_area(6)
rectangle_area(2,3)