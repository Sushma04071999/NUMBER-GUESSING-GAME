import random
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#enter the name bu using the input function
name=input('Enter your name: ') 
print("Hello ",name,", lets predict the number you are thinking of using binary search... \n\nPlease guess any number between 1 to 100.")

result="n"

min=1
max=100

#generating the random numbers
randomnumber=random.randint(min,max)

#intial guess count 
Guesscount=1

#using the while loop
while result!="y":
    
    #checking the random number correct or not 
    print(f"{bcolors.OKBLUE}\n{randomnumber}{bcolors.ENDC}")
    print("Is it correct? (y/n)")
    #give input yes or no
    result=input()
    
    #if your result is equal to yes if condition executes and program execution starts 
    if result=='y':
        #after how many iterations we arre gussing thw number
        print(f"{bcolors.OKGREEN}MAZEL TOV!!{bcolors.ENDC}")
        print("Well... it only took us {} iterations :D".format(Guesscount))
    
    #if your result==no else condtion will excute 
    elif result=='n':
        Guesscount=Guesscount+1
        print("Is the number greater than {}? (y/n)".format(randomnumber))
        greaterorless=input()
        
        #if your guessed number is greater than generated random number then enter G then if condition starts executes
        if greaterorless=="y":
            #number should be between random number and max number (randomnumber,100)
            #for ex randnumber=30,if it is greater than 30,then minimum number will be 31
            min=randomnumber+1
            print("number between ",min,"and",max)
            #generates the another random number
            randomnumber=random.randint(min,max)
            
        #if your guessed number is less than generated random number then enter L then if condition starts executes
        elif greaterorless=="n":
            #for ex randnumber=30,if it is less than 30, then max number will be 29
            max=randomnumber-1
            print("number between ",min,"and",max)
            #generates the another random number
            randomnumber=random.randint(min,max)
        else:
            print(f"{bcolors.WARNING}Please enter the valid input.{bcolors.ENDC}")
    else:
        print(f"{bcolors.WARNING}Please enter the valid input.{bcolors.ENDC}")
