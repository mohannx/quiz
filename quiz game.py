
from multiprocessing.connection import answer_challenge


print("welcome to my quiz game")

playing = input("do u want to play? ")
mark = 0

if playing.lower() != "yes" :
    quit()
print("okey lets play then")

que = input("what is abbreivation of HTML : ")
if que.upper() == "HYPERTEXT MARKUP LANGUAGE":
    print("Correct")
    mark += 1
else:
    print("incorrect")

que = input("what is abbreivation of CSS : ")
if que.upper() == "CASCADING STYLE SHEET":
    print("Correct")
    mark += 1
else:
    print("incorrect")

que = input("what is abbreivation of JS : ")
if que.upper() == "JAVASCRIPT":
    print("Correct")
    mark += 1
else:
    print("incorrect")

que = input("HTML IS A PROGRAMMING LANGUAGE? YES OR NO: ")
if que.upper() == "YES":
    print("Correct")
    mark += 1
else:
    print("incorrect")

print("you have scored " + str(mark) + "mark" )
