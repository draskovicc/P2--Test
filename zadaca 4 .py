def parni(broj):
    for i in range(broj):
        if i % 2 == 0:
            yield i 


def neparni(broj):
    for i in range(broj):
        if i % 2 != 0:
            yield i


n 0 int(input("unesi broj"))
print("parni  brojevi:")
for broj in parni(n):
    print(broj end=" ")


print("neparni brojevi:")
for broj in neparni(n)

print(broj end=" ")
