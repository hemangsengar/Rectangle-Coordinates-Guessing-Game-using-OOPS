"""

class House:

    def __init__(self, wall_area):
        self.wall_area = wall_area

class Paint:
    def __intit__(self,buckets, color):
        self.buckets = buckets
        self.color = color


"""
import math


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def falls_in_rectangle(self, lower_left, upper_right):
        if lower_left[0] < self.x < upper_right[0] \
        and lower_left[1] < self.x < upper_right[1]:
            return True
        else:
            return False
    
    class Rectangle:
        def __init__(self, lower_left, upper_right):
            self.lower_left=lower_left
            self.upper_right=upper_right

pointx = Point(6,7)
    

