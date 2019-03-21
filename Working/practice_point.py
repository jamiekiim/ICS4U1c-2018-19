class Point():

    def __init__(self, px, py):
        self.x = px
        self.y = py

    def get_distance(self, other_point):
        distance = math.sqrt((other_point.x - self.x)**2 + (other_point.y - self.y)**2)
        return distance

def main():
    p1 = Point(5, 10)
    p2 = Point(3, 4)

    dist = p1.get_distance(p2)
    print("The distance between the points is" + str(dist))

main()
