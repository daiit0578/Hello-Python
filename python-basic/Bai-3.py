String_a = input("nhap chuoi: ")
String_new = String_a.split(' ')
a = sorted(list(set(String_new)))
print(a)