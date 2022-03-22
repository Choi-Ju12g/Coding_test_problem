n = input()
length = len(n)
sum =0
for i in range(length//2):
   sum += int(n[i])

for i in range(length//2, length):
    sum -= int(n[i])

print("LUCKY") if sum ==0 else print("READY")
