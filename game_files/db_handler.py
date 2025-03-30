import psycopg2 as psy
from config import config


# pandas???

class Db_handler:
  
    def to_dict(self, questions):
        return {id: {"question": question,
                     "answers": [corr, wr1, wr2, wr3],
                     "difficulty": difficulty} for id, question, corr, wr1, wr2, wr3, difficulty in questions}

    def easy_questions(self):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty FROM easy_difficulty;")
        questions = self.to_dict(cursor.fetchall())
        conn.close()
        return questions
    
    def advanced_questions(self):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty FROM advanced_difficulty;")
        questions = self.to_dict(cursor.fetchall())
        conn.close()
        return questions
    
    def add_player(self, name, password):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO player (name, password) VALUES ('{name}', '{password}');")
        conn.commit()
        conn.close()
    

db = Db_handler()
db.add_player('Peter', '1234')
