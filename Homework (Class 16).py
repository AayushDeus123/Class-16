def shutdown(input):
    
    if input == 'Yes' or input == 'yes':
        return 'Shutting down'
    elif input == 'No' or input == 'no':
        return 'Abort shut down'
    else:
        return 'Sorry'

i = input("Do you want to shut down? (Yes/No): ")
print(shutdown(i))