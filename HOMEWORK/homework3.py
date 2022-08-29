
print("стороны:")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b<=c or a+c<=b or b+c<=a:
    print("треугольник не существует")
elif a!=b and a!=c and b!=c:
    print("разносторонний")
elif a==b==c:
    print("равносторонний")
else:
    print("равнобедренный")
