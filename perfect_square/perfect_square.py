def perfect_square(number):
    if number<0:
        return False
    if number==0 or number==1:
        return True
    result=1
    while result*result<=number:
        if result*result==number:
            return True
        result+=1
    return False
    

number=int(input("Enter the Number : "))
print(perfect_square(number))