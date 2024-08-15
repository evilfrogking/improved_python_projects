a = int(input("Enter No.1"))
b = int(input("Enter No.2"))
r = a%b
q = int(a/b)

while(r!=0):

    a = b

    b = r

    q = int(a/b)

    r = a - (b * q)


print(b)


