# Write a program that be able to find all factors of the numbers in the list l
l = [52633, 8137, 1024, 999]
for j in l:
    for i in range(1, j+1):
        if j % i == 0:
            print(i)

