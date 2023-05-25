a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
if (a + b < c or a + b == c) or (a + c < b or a + c == b) or (b + c < a or b + c == a):
    print("Não é um triângulo")
else:
    if a == b and b == c and c == a:
        print("Equilátero")
    if (a == b and b != c) or (a != b and b == c) or (a == c and c != b):
        print("Isósceles")
    if  (a != b and b != c and c != a):
        print("Escaleno")


#a + b > c
#a + c > b
#b + c > a