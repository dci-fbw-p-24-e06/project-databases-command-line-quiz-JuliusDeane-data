import psycopg2 as psy
from config import config


# pandas???

class Db_handler:
    topics = {1: 'q_general',
              2: 'q_functions',
              3: 'q_classes',
              4: 'q_file_handling'}
  
    def questions_to_dict(self, data):        
        return {id: {"question": question,
                        "answers": [corr, wr1, wr2, wr3],
                        "difficulty": difficulty} for id, question, corr, wr1, wr2, wr3, difficulty in data
                        }

    def get_questions(self, topic, difficulty):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"SELECT id, question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty FROM {self.topics[topic]} WHERE difficulty={difficulty};")
        questions = self.questions_to_dict(cursor.fetchall())
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
        password = [cursor.fetchall()[0][0]]
        conn.close()
        return password
    
    def get_answered_questions(self, name, topic):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"SELECT answered_questions FROM player WHERE name='{name}';")
        try:
            answered_questions = cursor.fetchall()[0][0]
        except IndexError:
            answered_questions = {f"{self.topics[topic]}": []}
        conn.close()
        return answered_questions[self.topics[topic]]
    
    def add_answered_questions(self, name, topic, ):
        pass
    
    def add_answered_questions(self, name, answered_questions):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE player SET answered_questions= '{answered_questions}' WHERE name='{name}';")
        conn.commit()
        conn.close()
    

if __name__ == '__main__':
    db = Db_handler()
    print(db.get_answered_questions('Jeff')['q_general'])



