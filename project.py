"""Play JEOPARDY!!!
Select number of rounds,
questions per rounds,
and calculate score in
single, double, and final Jeopardy"""

import csv
import random


def main():
    """Main Function - run game"""
    print("Welcome to Jeopardy!")
    file = "JEOPARDY_CSV.csv"
    shows = []
    with open(file) as file:
        reader = csv.DictReader(file)
        for line in reader:
            category = line[" Category"]
            question = line[" Question"]
            answer = line[" Answer"]
            shows.append(
                {
                    "Category": category,
                    "Question": question,
                    "Answer": answer,
                }
            )

        rounds = get_rounds()
        Qs = get_Qs()
        score = 0
        if rounds in [1, 2]:
            print("\n")
            print("Welcome to Jeapordy! Questions are worth $200")
            for _ in range(Qs):
                print("\n")
                correct, answer = get_QA(shows)
                if correct == 1:
                    score += 200
                    print("Correct")
                    print("Score:", score)

                if correct == 0:
                    print(f"Incorrect, the answer is {answer}")
                    print("Score:", score)
        if rounds == 2:
            print("\n")
            print("Welcome to Double Jeapordy! All questions are now worth $400")
            for _ in range(Qs):
                print("\n")
                correct, answer = get_QA(shows)
                if correct == 1:
                    score += 400
                    print("Correct")
                    print("Score:", score)

                if correct == 0:
                    print(f"Incorrect, the answer is {answer}")
                    print("Score:", score)

        print("Final Score:", score)
        print("\n")
        print(
            "Welcome to Final Jeapordy. Please decide how much you would like to wager."
        )
        for _ in range(1):
            print("\n")
            wager = get_wager(score)
            correct, answer = get_QA(shows)
            if correct == 1:
                score += wager
                print("Correct")

            if correct == 0:
                score -= wager
                print(f"Incorrect, the answer is {answer}")
        print("Final Score:", score)


def get_rounds():
    """Get number of rounds"""
    while True:
        try:
            rounds = int(input("How many rounds would you like to play, 1 or 2? "))
            if rounds not in [1, 2]:
                print("Please enter 1 or 2")
                raise ValueError
            return rounds
        except ValueError:
            pass


def get_Qs():
    """Get number of Qs per round"""
    while True:
        try:
            questions = int(
                input(
                    "How many questions per round would you like? Answer a number 1-6: "
                )
            )
            if questions not in [1, 2, 3, 4, 5, 6]:
                print("Please enter a number 1-6")
                raise ValueError
            return questions
        except ValueError:
            pass


def get_QA(s):
    """Get random question, answer category,
    see if user input matches answer or is included in answer"""
    show = random.choice(s)
    question = show["Question"]
    answer = show["Answer"]
    answer = answer.title()
    category = show["Category"]
    print(f"The category is {category}")
    user_answer = input(f"{question}: ").title().strip()
    if user_answer == answer or user_answer in answer and user_answer != "":
        return 1, answer
    else:
        return 0, answer


def get_wager(s):
    """Get wager for final score calculation ie final Jeopardy"""
    while True:
        try:
            print("How much would you like to wager?")
            wager = int(input(f"You can wager any amount between $0 and {s}. "))
            if wager > s:
                print("Wager cannot be greater than your score")
                raise ValueError
            if wager < 0:
                print("Wager cannot be less than 0")
                raise ValueError
            return wager
        except ValueError:
            pass


if __name__ == "__main__":
    main()
