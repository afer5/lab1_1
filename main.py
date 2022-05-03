import cmath
a = int(input("Input coefficient a: "))
b = int(input("Input coefficient b: "))
c = int(input("Input coefficient c: "))
def equation(q, w, e):
    d = w * w - 4 * q * e
    x1 = (-w + cmath.sqrt(d)) / 2 * q
    x2 = (-w - cmath.sqrt(d)) / 2 * q
    print(x1,x2)

equation(a,b,c)
