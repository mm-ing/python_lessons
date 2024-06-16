
# calculate the area of a triangle given the length of its sides
# If a, b and c are three sides of a triangle. Then,
# s = (a+b+c)/2
# area = √(s(s-a)(s-b)(s-c))
def areaOfTriangle(a, b, c):
    # calculate the semi-perimeter
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area
