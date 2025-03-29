# The Quiz Game

""" 
- Player inputs name
- Player answers between 1 and 20 questions
- player gets score
"""
from game_files import db_handler

db = db_handler.Db_handler()

print(db.get_easy_questions())


questions = {
    1: {
        "question": "What is the standard file extension for Python files?",
        "options": ["a) .py", "b) .python", "c) .pyt", "d) .txt"],
        "answer": "a"
    }}




player = input("What's your name? ")
rounds = int(input("How many rounds do you want to play? (1-20) "))
score = 0 
questions_picked = []




def show_score(player_name = 'Unknown', points = 0):
    """Shows the final score to the player"""
    if points == rounds:
        return f'Amazing job {player_name}! A perfect {points}/{rounds} score, are you Linus Torwalds or Chris Sawyer?'
    elif points < rounds and points >= (rounds/2):
        return f'Good job {player_name}! A {points}/{rounds} score is nothing to sneeze at.'
    elif points < (rounds/2) and points >= 1:
        return f'You can do better {player_name}! With a {points}/{rounds} score you have a lot of room for improvement.'       
    else:
        return f'Are you okay {player_name}? A {points}/{rounds} score is not so good. Please see a doctor.'




def show_question(number_of_question):
    """returns the question and answer options to the user"""
    print(f'\n\n{questions[number_of_question]["question"]}\n\n{"  ".join(questions[number_of_question]["options"])}')
    



def check_answer(player_answer, number_of_question):
    """checks if given answer is correct"""
    if player_answer == questions[number_of_question]['answer']:
        print(f'\nCorrect! You get +1 point')
        return 1
    else:
        print(f"\nSorry, you're wrong. The correct answer is {questions[number_of_question]['answer']}")
        return 0




def pick_question():
    """Let's player choose a question. If question was chosen before, it makes them choose another question"""
    number = int(input(f"\n{player} pick a number betweeen 1 - 20 to get your next question: "))
    if number in questions_picked:
        print(f'You already answered question {number}. Please pick a different question.')
        number = pick_question()
    else:
        questions_picked.append(number)
        show_question(number)
    return number





def main_quiz(name, score):
    """present questions to the player, check answers, track score"""
    print(f"Your current score is {score}.")
    question_number = pick_question()
    #question_number = int(input(f"{name} pick a number betweeen 1 - 20 to get your next question: "))
    #show_question(question_number)
    answer_choice = input(f"\nPlease choose your answer (a, b, c, d): ")
    score = check_answer(answer_choice, question_number)
    return score




n = 0
while n < rounds:
    score += main_quiz(player, score)
    n += 1

print(f'\n {show_score(player, score)}')