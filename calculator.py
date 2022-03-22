#project Calculator!

#Created by "Hellaire!"


#This main() function is for repeating it again!
def main():
       
 #This is math module which importing all mathematical operations.
    
    import math as m

    #This gonna say "Hey" to user with name given by user.
    print()
    print("Hello user!","\U0001F600")
    print()

    print("Welcome to calculator.")
    print()

    #These variables is for giving all the operators to user!

    c="1:Addition = + "
    d="2:Subtraction = - "
    e="3:Multiple = * "
    f="4:Division = / "
    g="5:Power = ** "
    h="6:Sqrt = ^ "
    i="7:Sine = s"
    j="8:Degrees = 0"
    k="9:Cosine = c "
    l="10:Logrithm = l "

    #This is gonna print all operators we can perform.
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)
    print(h)
    print(i)
    print(j)
    print(k)
    print(l)
    print()
#This is for assinging value to perform with any number.
    a=0
    b=0
    c=0

#This is for getting numbers from user.
    print("How many numbers you want to use?")
    
    #This is for taking input from user , that how many numbers he or she want to use!
    nop=int(input("Numbers:"))
    
    #This is only for one number.
    if nop==1:
        a=int(input("Enter 1st number:"))
        
    #This is only for 2nd number.
    elif nop==2:
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        
    #This is only for 3rd number.    
    elif nop==3:
        a=int(input("Enter 1st number:"))
        b=int(input("Enter 2nd number:"))
        c=int(input("Enter 3rd number:"))
        
    #This will gonna for any other case.    
    else:
                                               
        print("It will gonna continue the calculator but answer be gonna zero!\nplease enter number upto three only.")      
        
    #This is input function for getting values from user!

    op=input("choose any one operator:")

#This is calulator class containing all the functions.
    class cal:
        
        #This is add function,it will add two numbers.
        
        def add(a,b,c): 
            result=a+b+c
            print("The addition of two numbers is :",result) 
            
        #This is mul function, it will multiple two numbers.
            
        def mul(a,b):
            result=a*b
            print("The Multiplication of two numbers is :",result)
            
        #This is div function,it will divide two numbers.
        
        def div(a,b):
            result=(a/b)
            print("The division of two numbers is :",result)
            
        #This is sub function , it will subtract two numbers.
        def sub(a,b,c):
            result=a-b-c
            print("The subtraction of two numbers is : ",result)
            
        #This is pow function , it will going to give a power of a given number.
            
        def pow(a,b):
            result=a**b
            print("The power of 1st number with respect to 2nd number is :",result)
            
        #This is sqrt function , it will gonna give a square root of only one number.

        def sqrt(a):
            result=m.sqrt(a)   
            print("The square root of 1st number is:",result)
            
        #This is sine function,it will gonna give sine of only one number.    
        def sin(a):
            result=m.sin(a)
            print("The sine of 1st number is :",result)
            
        #This is Degr. function ,it will gonna give degrees of only one number.
        def Degrees(a):
            result=m.degrees(a)
            print("The degrees of 1st number is :",result)
            
        #This is a cos. function , it will gonna give you cosine of only one number.
        def cos(a):
            result=m.cos(a)
            print("The cosine of 1st number is :",result)
            
         #This is a log. function , it will gonna give you log of only one number.   
        def log(a):
            result=m.log(a)
            print("The log of 1st number is :",result)

    
    #This is for checking the given operator and performing the functions from operator.
    if op=="+":
        cal.add(a,b,c)
        
    elif op=="-":
        cal.sub(a,b,c)
        
    elif op =="*":
        cal.mul(a,b)
        
    elif op=="/":
        cal.div(a,b)
        
    elif op=="**":
        cal.pow(a,b)

    elif op=="^":
        cal.sqrt(a)
        
    elif op=="s":
        cal.sin(a)
        
    elif op=="0":
        cal.Degrees(a)
        
    elif op=="c":
        cal.cos(a)
    
    elif op=="l":
        cal.log(a)

    else:
        print("Invalid operator!")
    
    
    #This statement gonna print,Thank you for using it.
        
    print("Thank you.")
    print()
    
    #This is for printing yes or no for user.
    print("Please write yes  or y ,\n And no or n.")
    print()
    
    #This will gonna take input from user for using it again or not.
    R = input("Would you like to use it again ?\n")
    
    #This statement is for repeating it .
    if R == "yes" or R=="y" or R=="YES":
        main()
        
    elif R=="no" or R == "n":
        exit()
        
    else:
        print("Bye!")
    

#This is main() is calling a defined function.
main()
