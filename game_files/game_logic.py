import db_handler
import random


db = db_handler.Db_handler()

class Game:
    def __init__(self):
        self.questions = {}
        self.player = "Anon"
        self.score = 0
        self.rounds = 0
        self.total_rounds = 5
        self.id_list = []
        self.corr_answer_letter = ""
        self.corr_answers_list = []

    def load_questions(self, difficulty):
        """Loads the questions from the database and stores them in self.questions"""
        if difficulty == "easy":
            questions = db.easy_questions()
        else:
            questions = db.advanced_questions()
        self.questions = questions

    def show_question(self, id):
        """Retuns the question to the id."""
        return self.questions[id]["question"]
    
    def show_answers(self, id):
        """Returns a formatted string with the answers options."""
        answers = self.questions[id]["answers"]
        corr_answer = answers[0]
        random.shuffle(answers)
        self.corr_answer_letter = "abcd"[answers.index(corr_answer)]        
        return f"a: {answers[0]}\nb: {answers[1]}\nc: {answers[2]}\nd: {answers[3]}"

    def check_answer(self, id, answer):
        """Returns a formatted string with a message, if the given answer was correct.
        Updates the score and and the list of correct answers."""
        if answer == self.corr_answer_letter:
            self.score += self.questions[id]['difficulty']
            self.corr_answers_list.append(id)
            return f"Correct! New score: {self.score}"
        else:
            return f"False! Your score: {self.score}"
        
    def make_id_list(self):
        """Creates id_list for game round from question list minus list of already answered question (feature not yet implemented)"""
        self.id_list = [key for key in self.questions.keys() if key not in self.corr_answers_list]
        
    def pick_question(self):
        """Returns the id of a randomly picked question"""
        id = random.choice(self.id_list)
        self.id_list.remove(id)
        return id

    def question_round(self):
        """One question round. This will pick and show one question, and check the answer."""        
        print(f"Round {self.rounds} of {self.total_rounds}:")
        id = self.pick_question()
        print(self.show_question(id))
        print(self.show_answers(id))
        answer = input("Your answer: ")
        print(self.check_answer(id, answer))

    def game_round(self, difficulty):
        """One quiz round. Load the questions and play a certain number of question rounds"""
        self.load_questions(difficulty)
        self.make_id_list()
        while self.rounds < self.total_rounds:
            self.rounds += 1
            self.question_round()
        else:
            print(f"Game over. Your total score is: {self.score}.")
        




        

game = Game()

game.game_round("advanced")


# key, value = questions[1].items()
# print(key, "\n", value)


