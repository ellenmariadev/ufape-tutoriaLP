A = True
B = False
C = True

a = A and (B or C)

b = (A and B) or C

c = not (A and B) or C

d = not A or (not B and C)

print("\n[QUESTÃO 01]\n")

print(f"a) A ^ (B v C): {a}\n")
print(f"b) (A ^ B) v C: {b}\n")
print(f"c) (A ^ B)' v C: {c}\n")
print(f"d) A' V (B' ^ C): {d}")