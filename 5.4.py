#StudentID: 1201201695
#StudentName: Peong Khay Zhien

def rectangle(width, length):
    area=width*length
    print("Rectangle area : {:.2f}".format(area))
def triangle(width, length):
    area=1/2*width*length
    print("Triangle area : {:.2f}".format(area))
count = 0
while(count<2):
    width=float(input("Enter width : "))
    length=float(input("Enter length :"))
    rectangle(width, length)
    triangle(width,length)
    count=count+1