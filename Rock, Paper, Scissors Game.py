import random;

characters = ["S", "W", "G"];
compSocre = 0;
userScore = 0;

print("\n\t\t\t!!!... Welcome to Snake Water Gun Game ...!!!")
print("\n\t\t\t\t  Match will be of 10 Rounds");
print("\n\t\t\t\t      Choose S for Snake\n\t\t\t\t      Choose W for Water\n\t\t\t\t      Choose G for Gun\n");

name = input("\n\tEnter your name : ");
iterator = 1;

def score(compScore , userScore) :
    print("\n\t"+ name +" score :", userScore);
    print("\tComputer score :", compScore);

while iterator <= 3 : 
    print("\n\t\t\t\tRound", iterator);

    compInput = random.choice(characters);
    userInput = input("\n\tEnter your input : ");
    userInput.capitalize();

    print("\n\t"+ name +" chooses : "+ userInput);
    print("\tComputer chooses : "+ compInput);

    if (userInput == "G" and compInput == "S") or (userInput == "W" and compInput == "G") or (userInput == "S" and compInput == "W") :
        print("\n\t"+ name +" wins the round");
        userScore += 1;
    elif userInput == compInput:
        print("\n\tDraw");
    else :
        print("\n\tComputer wins the round");
        compSocre += 1;

    score(compSocre, userScore);    
    iterator += 1;

if userScore < compSocre :
    print("\n\n\t\t\t\t"+"Computer wins the game ...!!");
elif userScore == compSocre :
    print("\n\n\t\t\t\tDraw ...!!");
else :
    print("\n\n\t\t\t\t"+ name +"wins the game ...!!");
