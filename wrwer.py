class P():
    n = 10

p = P()

class C(P):
    k = 10

c = C()

print(issubclass(C,P))