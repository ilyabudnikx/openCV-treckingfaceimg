mydr = [5,2,2002]
pr = 5 * 2
for i in mydr:
    a = i
    a = bin(a)
    print(f"Двоичная система: {a}")
for i in mydr:
    i = hex(i)
    print(f"16-и ричная система: {i} \b")
print(f"Произведение дня на месяц: {bin(pr)} - двоичная система | {hex(pr)} - 16-и ричная система")


