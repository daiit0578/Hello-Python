#nhan chuoi va tach chuoi

myList = [x for x in input("nhap day chu: \n").split(',')]
myList.sort()
print(','.join(myList))
