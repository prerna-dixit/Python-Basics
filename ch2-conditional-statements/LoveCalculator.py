#PROJECT 8
#Takes two names as an input and checks if they have letters of TRUE LOVE using count() function
#lower() function converts it to all lowercase
#then gives score as an output as 10*TRUE+LOVE, eg true=3 and love=3, the score is 33

#for love scores less than 100 and greater than 85, message should be- "Your score is ..... you go together like coke and mentos" 
#for scores bw 40 and 70, message should be- "Your score is ..... you are alright together"
#for scores other than that, message should be- "Your score is .... What are the chances?!"

name1=input("Your Name: ")
name2=input("Partner's Name: ")
lwr1=name1.lower()
lwr2=name2.lower()
c1=lwr1.count("t")+lwr2.count("t")
c2=lwr1.count("r")+lwr2.count("r")
c3=lwr1.count("u")+lwr2.count("u")
c4=lwr1.count("e")+lwr2.count("e")
c5=lwr1.count("l")+lwr2.count("l")
c6=lwr1.count("o")+lwr2.count("o")
c7=lwr1.count("v")+lwr2.count("v")
c8=lwr1.count("e")+lwr2.count("e")
true=c1+c2+c3+c4
love=c5+c6+c7+c8
score=10*true+love
if score<100 and score>85:
    print(f"Your score is {score}. You go together like coke and mentos~")
elif score<=70 and score>=40:
    print(f"Your score is {score}. You go alright together.")
else:
    print(f"Your score is {score}. What are the chances?!")