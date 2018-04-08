class Line:

    __slots__ = 'slope','yIntercept','x1','y1','x2','y2'


    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.slope = (y2-y1)/(x2-x1)
        self.intercept()

    def intercept(self):
        self.yIntercept = self.y1 - (self.slope * self.x1)


    def __str__(self):
        return "Intercept " + str(self.yIntercept) + " With slope " + str(self.slope)
        # print( "Intercept " + str(self.yIntercept) + "With slope " + str(self.slope))


def test():
    # n = int(input())
    points =[[2,1],[1,2]]
    lines = Line(1,2,2,1)
    print(lines)


if __name__ == '__main__':
    test()

# if __name__ == '__main__':
#     n = int(input())
#     points = []
#     for i in range(n):
#         coordinate = [int(x) for x in input().split(" ") ]
#         points.append(coordinate)
#     print(points)
