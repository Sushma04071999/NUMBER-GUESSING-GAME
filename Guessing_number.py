import random

#enter the name bu using the input function
name=input('enter your name') 
print(name,"please guess any number between 1 to 100","i will find that number",sep='\n')

result="no"

min=1
max=100

#generating the random numbers
randomnumber=random.randint(min,max)

#intial guess count 
Guesscount=0

print(randomnumber)

#using the while loop
while result=="no":
    
    #checking the random number correct or not 
    print("{}- is correct? type yes or no".format(randomnumber))
    #give input yes or no
    result=input()
    
    #if your result is equal to yes if condition executes and program execution starts 
    if result=='yes':
        print("Holla, i guessed number")
    
    #if your result==no else condtion will excute 
    else:
        Guesscount=Guesscount+1
        print("The number is greater than or less that {}".format(randomnumber))
        print("If greater type G,or If less type L")
        greaterorless=input()
        
        #if your guessed number is greater than generated random number then enter G then if condition starts executes
        if greaterorless=="G":
            #number should be between random number and max number (randomnumber,100)
            #for ex randnumber=30,if it is greater than 30,then minimum number will be 31
            min=randomnumber+1
            print("number between ",min,"and",max)
            #generates the another random number
            randomnumber=random.randint(min,max)
            
        #if your guessed number is less than generated random number then enter L then if condition starts executes
        else:
            #for ex randnumber=30,if it is less than 30, then max number will be 29
            max=randomnumber-1
            print("number between ",min,"and",max)
            #generates the another random number
            randomnumber=random.randint(min,max)
    
    #after how many iterations we arre gussing thw number     
    print("Guessed in {} number of times".format(Guesscount))
