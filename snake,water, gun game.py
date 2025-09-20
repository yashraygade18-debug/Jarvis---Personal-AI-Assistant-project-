import random
'''
1 for Snake 
-1 for Water 
0 for Gun 
'''
computer= random.choice([-1,0,1])
youstr = input ("Enter a  your choice : ")
youDict={"S": 1,"W": -1,"G": 0}
reverseDict = {1: "Snake",-1: "Water", 0: "Gun"}

you = youDict[youstr]

# By now we have 2 numbers (varibles),you and computer  

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("its a draw")

if(computer==-1 and you==  1): 
    print("you win!")

elif(computer==-1 and you==  0 ): 
    print("you lose! ")

elif(computer==1 and you==  -1): 
    print("you lose! ")

elif(computer==1 and you==  0 ): 
    print("you win! ")

elif(computer==0 and you==  1): 
    print("you lose! ")

elif(computer==0 and you==  -1): 
    print("you win! ")

else:
    print("Somethings went Wrong!")




#these a shortuct it require the analysis 

#if((computer - you == -1 or computer - you == 2)):
    print("you lose")
    print("you lose!")
#else:
    print("you win!")
  


