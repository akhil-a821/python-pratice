question=("1.What is the capital of France?",
          "2.What is 2 + 2?",
          "3.What is the capital of Japan?",
          "4.What is 5 * 6?")
option=(("A. Paris", "B. London", "C. Berlin", "D. Madrid"),
       ("A. 3", "B. 4", "C. 5", "D. 6"),
       ("A. Tokyo", "B. Beijing", "C. Seoul", "D. Bangkok"),
       ("A. 28", "B. 30", "C. 32", "D. 34"))
answer=("A","B","A","B")
guess=[]
score=0
question_num=0
for questions in question:
    print("---------------------")
    print(questions)
    for options in option[question_num]:
        print(options)
    guesses=input("Enter your answer(A,B,C,D): ").upper()
    guess.append(guesses)
    if guesses==answer[question_num]:
            print("Correct")
            score+=1
    else:
            print("Wrong")

    question_num+=1
print("---------------------")
print("       RESULT        ")
print("---------------------")
print("answers: ",end="")
for answers in answer:
      print(answers,end=" ")
print()
print("guess: ",end="")
for guesses in guess:
      print(guesses,end=" ")
print()
percentage=(score/len(question)*100)
print(f"your score is {score}")
print(f"your percentage is {percentage}%")
if percentage>=75:
        print("You are awesome......^_^")
else:
        print("next time try hard :(")


