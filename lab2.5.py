#Student ID: 1201201695
#Student Name: Peong Khay Zhien

PRICE =  0.15
print("Natural Mineral Water Dispenser")
print("----------------------------------\n")
litre = int(input("Enter amount of litres: "))
total = litre * PRICE
print("Price per litre RM{:.2f}".format(PRICE))
print("Number of liters: {:.0f}".format(litre))
print("Total: RM{:.2f}".format(total))