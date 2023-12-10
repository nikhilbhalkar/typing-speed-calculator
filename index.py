from time import *
import random as r

def mistack(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!=usertest[i]:
                error = error+1
        except:
            error = error+1
    return error
def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
    
while True:
    ck=input("Ready to Test: yes/no:")
    if ck=="yes":
        
        test=[ "Multiple applications: Multiprogramming was invented to allow processing time to be dynamically shared among a number of active applications.","Operating system structure: The same structuring advantages apply to systems programs", 
                "and we have seen that operating systems are themselves often implemented as a set of processes or threads.","I Am chetan Dhangar","I am fro chopada","I have currently purchising BTECH Degree","I have good prson for every work"]
        test1=r.choice(test)
        print("      ****Typing Speed****       ")
        
        print(test1)
        print()
        print()
        time_1 = time()
        testinput=input("Enter: ")
        time_2 = time()

        print('Speed : ',speed_time(time_1,time_2,testinput),"w/sec")
        print("Error : ",mistack(test1,testinput))
    elif ck=="no":
        print("Thank You")
        break
    else:
        print("Wrong input")