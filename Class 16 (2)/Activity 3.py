#Calculating Factorials
def fact(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

i = int(input('Enter a number to calculate its factorial : '))
print('The factorial of',i,'is :', fact(i)) 