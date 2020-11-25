#nhap vao cac dong
lines=[]
while True:
    s= input("")
    if s:
        lines.append(s.upper())
    else:
        break

for y in lines:
    print(y)
