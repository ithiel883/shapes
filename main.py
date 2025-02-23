import shapes

rectangle = shapes.rectangle(16, 18)
print("perimeter_rectangle: ",rectangle.perimeter)
print("area_rectangle: ", rectangle.area)

square = shapes.square(2)
print("area_square: ",square.area)
print("perimeter_square: ",square.perimeter)

circle = shapes.circle(7)
print("circle_area: ", circle.area)
print("circle_perimeter", circle.perimeter)

tangle = shapes.triangle(A=2, B=3, C=3)
print(tangle.perimeter)