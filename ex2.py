# Write a function that prints all factors of the given parameter x
def print_factor(x):
    for i in range(1, x+1):
        if x % i == 0:
            print(i)

x = 52633
print_factor(x)