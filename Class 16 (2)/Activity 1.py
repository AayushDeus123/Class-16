#Tip Percentage
total = 0
def t(tb,tp):
    total = tb + (tb/100) * tp
    total = round(total, 2)
    print('Please pay your bill of Rs',total)
    
b = int(input('Enter your bill : '))
i = (input('Do you wish to add a tip? Y/N :'))

if i == 'Y' or i == 'y':
    p = float(input('How much percentage of tip would you like to pay? : '))
    t(b,p) 
else:
    t(b,0) 
            