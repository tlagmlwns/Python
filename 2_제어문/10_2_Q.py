A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
for score in A:
    if score >= 50:
        sum += score
print(sum)

B = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
sum = 0
while B:
 score = B.pop()
 if score >= 50:
    sum += score