import random
import string as s

def generate_password(minLen,num=True, specialChars=True):
    # print(minLen,num,specialChars)
    letters=s.ascii_letters
    special=s.punctuation
    numbers=s.digits
    
    chooseFrom=letters
    if num:
        chooseFrom+=numbers
    if specialChars:
        chooseFrom+=special
    
    pwd=""
    meetCriteria=False
    has_number=False
    has_special=False

    while not meetCriteria or len(pwd)<minLen:
        newChar=random.choice(chooseFrom)
        pwd+=newChar

        if newChar in numbers:
            has_number=True
        if newChar in special:
            has_special=True
        
        meetCriteria=True
        if num:
            meetCriteria=has_number
        if specialChars:
            meetCriteria=meetCriteria and has_special
    return pwd

length_of_password=int(input("enter length of password: "))
includeNumbers=input("include numbers? (yes/no): ")
if includeNumbers=="yes":
    includeNumbers=True
else:
    includeNumbers=False
includeSpecialChars=input("include special characters (yes/no): ")
if includeSpecialChars=="yes":
    includeSpecialChars=True
else:
    includeSpecialChars=False

result=generate_password(length_of_password,includeNumbers,includeSpecialChars)

print(result)