print("POSITIVE NUMBER OR NEGATIVE NUMBER:")
n=int(input("Enter a number:"))
if (n>=1):
    print("Postive Number")
else:
    print("Negative Number")
print("EVEN OR ODD")
if (n%2==0):
    print("Even")
else:
     print("Odd")
print("LARGEST NUMBER:")
a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))
if (a>b):
    print(a,"is largest")
else:
    print(b,"is largest")
a=int(input("Enter a number1:"))
b=int(input("Enter a number2:"))
c=int(input("Enter a number3:"))
print("LARGEST AMONG THREE NUMBERS:")
if (a>b):
    if(a>c):
        print(a,"is largest")
if(b>c):
    if(b>a):
            print(b,"is largest")

else:
     print(c,"is largest")
print("DIVISIBLITY CHECK:")
n=int(input("ENTER A NUMBER:"))
if(n%5==0 and n%11==0):
    print("NUMBER IS DIVISBLE BY BOTH NUMBER")
elif(n%5==0):
    print("NUMBER IS DIVISIBLE BY 5")
elif(n%11==0):
    print("NUMBER IS DIVISIBLE BY 11")
else:
    print("NOT DIVISIBLE BY BOTH NUMBERS")
print("DIVISIBLITY CHECK:")
n=int(input("ENTER A NUMBER:"))
if(n%3==0 and n%7==0):
    print("NUMBER IS DIVISBLE BY BOTH NUMBER")
elif(n%3==0):
    print("NUMBER IS DIVISIBLE BY 3")
elif(n%7==0):
    print("NUMBER IS DIVISIBLE BY 7")
else:
    print("NOT DIVISIBLE BY BOTH NUMBERS")
print("LEAP YEAR CHECK:")
n=int(input("ENTER YEAR:"))
if n%4==0:
    print("year is leap year")
else:
    print("year is not leap year")
print("VOWEL OR CONSONANT CHECK:")
character=str(input("Enter a character:"))
if(character=="a"or character=="A"or character=="e"or character=="E"or character=="i"or character=="I"or character=="u"or character=="U"or character =="o" or character=="O"):
    print("Vowel")
else:
    print("Consonant")
print("CHECK GIVEN NUMBER IS THREE DIGIT OR NOT:")
n=int(input("ENTER A NUMBER:"))
if(n>=100 and n<=999):
    print("THREE DIGIT NUMBER")
else:
    print("NOT A THREE DIGIT NUMBER")
print("CHECK NUMBER IS GREATER THAN 100")
n=int(input("ENTER A NUMBER:"))
if(n>100):
    print("GREATER THAN 100")
else:
    print("NOT A GREATER THAN 100")


















