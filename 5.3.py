#StudentID: 1201201695
#StudentName: Peong Khay Zhien
def get_cm():
    cm=float(input("Please enter a value for centimeter :"))
    m=cm_to_meter(cm)
    print("{:.2f} cm is {:.2f} meter".format(cm,m))
def get_meter():
    m=int(input("Please enter a value for meter : "))
    cm=meter_to_cm(m)
    print("{:.2f} m is {:.2f} centimeter".format(m,cm))
def cm_to_meter(centimeter):
    meter = centimeter / 100
    return meter
def meter_to_cm(meter):
    centimeter = meter * 100
    return centimeter
print("=========================")
print("\t\t     MENU")
option = int(input("Enter option 1 or 2: "))
if(option == 1):
    get_cm()
elif(option == 2):
    get_meter()
else:
    print("Invalid choice")
