numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
nagy = numbers [0]
kicsi = numbers [0]
avg = 0
for i in range(0,len(numbers),1):
    if nagy < numbers [i]:
        nagy = numbers [i]
    elif kicsi > numbers [i]:
        kicsi = numbers [i]
    avg += numbers [i]
    i += 1
print(nagy)
print(kicsi)
print(avg/8)
