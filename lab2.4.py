#Student ID: 1201201695
#Student Name: Peong Khay Zhien


banana = 1.50
grape = 5.60
print("Invoice for Fruits Purchase")
print("------------------------------")
qty1 = int(input("Enter the quantity (comb) of bananas bought: "))
qty2 = int(input("Enter the amount (kg) of grapes bought: "))
sum1 = qty1 * banana
sum2 = qty2 * grape
total = sum1 + sum2
print("Item             Qty      Price       Total")
print("Banana (combs)   {:.0f}    RM{:.2f}    RM{:.2f}".format(qty1, banana, sum1))
print("Grapes (kg)      {:.0f}    RM{:.2f}    RM{:.2f}".format(qty2, grape, sum2))
print("Total: RM{:.2f}".format(total))