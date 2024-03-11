def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1


    for key in questions:
        print("-----------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter a, b, or c:   ")
        guess = guess.upper()
        guesses. append(guess)

        correct_guesses += check_answer(questions.get (key), guess)
        question_num +=1

    display_score(correct_guesses, guesses)
    
def check_answer(answer, guess):
    if answer == guess:
        print("Correct")
        return 1 
    else:
        print("Wrong! Why would you think that?")
        return 0
    
def display_score(correct_guesses, guesses):
    print("--------------------")
    print("RESULTS")
    print("--------------------")

    print("Answers: ", end= "")
    for i in questions:
        print(questions.get(i), end ="")
        print()

        print("Guesses: ", end= "")
    for i in guesses:
        print(i, end ="")
        print()

    score = int((correct_guesses/len(questions))* 100)
    print ("Your score is: " + str(score) + "%")
def play_again():
    
    response = input("Do you want to play again?: (yes or no)")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

questions = {
    "Who sang Wasted Eyes?: ": "A",
    "Who played KC in KC undercover?: ": "C",
    "Who released an album called 'Hope' in April 2023?: ": "A",
    "When did Kanye release 'Vultures?: ": "B",
    "Who had the best verse on Kanye's last album?: ": "B",
    "What is the smallest country in the world?: " : "B",
    "Which country gifted the Statue of Liberty to the United States?: " : "A",
    "What is the national flower of Japan?: " :"A",
    "What is the highest-grossing film of all time (as of 2022)?:" :"A",
    "Which bird is known for its ability to mimic human speech?: " :"C"
}

options = [["A.Amaarae", "B.Ariana Grande", "C.Celine Dion" ],
            ["A.Yara Shahidi", "B.Viola Davis", "C.Zendaya"],
            ["A.NF", "B.Eminem", "C.The Weekend"],
            ["A.December,2023", "B.He never dropped the album", "C.January,2024"],
            ["A.TY Dolla", "B.North West", "C.Taylor Swift"],
            ["A. Monaco", "B. Vatican City", "C. Liechtenstein"],
            ["A. France", "B. Italy", "C. United Kingdom"],
            ["A. Sakura (Cherry Blossom)", "B. Lotus", "C. Rose"],
            ["A. Avengers: Endgame", "B. Avatar", "C. Titanic"],
            ["A. Crow", "B. Owl", "C.Parrot"]
]

new_game()

while play_again():
    new_game()

print("Adios!  ")