def triangle(base:float,height:float,length:float):
    triangle_area = 0.5*base*height
    triangle_ocean= base+height+length
    return triangle_area ,triangle_ocean
def square(length):
    square_area=length**2
    square_ocean=length*4
    return square_area,square_ocean

print(triangle(3,2,4))
print(square(5))