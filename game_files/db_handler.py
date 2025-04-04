import psycopg2 as psy
from config import config


# pandas???

class Db_handler:
  
    def to_dict(self, data, type):
        if type == "questions":
            return {id: {"question": question,
                         "answers": [corr, wr1, wr2, wr3],
                         "difficulty": difficulty} for id, question, corr, wr1, wr2, wr3, difficulty in data
                         }
        elif type == "player":
            pass

    def get_questions(self):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT id, question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty FROM easy_difficulty;")
        questions = self.to_dict(cursor.fetchall(), "questions")
        conn.close()
        return questions
    
    
    def add_player(self, name, password):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO player (name, password) VALUES ('{name}', '{password}');")
        conn.commit()
        conn.close()

    def get_player_list(self):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM player;")
        player_list = [x[0] for x in cursor.fetchall()]
        conn.close()
        return player_list
    
    def get_password(self, name):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"SELECT password FROM player WHERE name='{name}';")
        password = cursor.fetchall()[0][0]
        conn.close()
        return password
    





