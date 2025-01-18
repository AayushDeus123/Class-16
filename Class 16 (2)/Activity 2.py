#Cube of a number divisible by 3
def inp(num):
    return num**3

def div3(num):
    if num % 3 == 0:
        return inp(num)
    else:
        return False

i = int(input('Enter your number : '))
print(div3(i))