# 1) Write a definition for a class named Circle with attributes center and
# radius,where center is a Point tuple and radius is a number
class Circle:
    def(self,center,radius)
    self.center = center
    self.radius = radius
    

# 2) Instantiate a Circle object that represents a circle with
# its center at (150, 100) and radius 75
circ = Circle((150,100), 75)


# 3) Write a function named point_in_circle that takes a
# Circle and a Point and returns True if the
# Point lies in or on the boundary of the circle.
# DOCS: https://stackoverflow.com/questions/481144/equation-for-testing-if-a-point-is-inside-a-circle
def point_in_circle(circle, point):
    def in_circle(center_x, center_y, radius, x, y):
    square_dist = (center_x - x) ** 2 + (center_y - y) ** 2
    return square_dist < radius ** 2
    
    