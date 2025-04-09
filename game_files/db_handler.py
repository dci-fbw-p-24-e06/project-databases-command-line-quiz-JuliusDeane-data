import psycopg2 as psy
import json
from .config import config


# pandas???


class Db_handler:
    topics = {"General Python": "q_general", "Functions": "q_functions", "Classes": "q_classes", "File Handling": "q_file_handling"}

    answered_questions = {topics["General Python"]: [], topics["Functions"]: [], topics["Classes"]: [], topics["File Handling"]: []}

    def questions_to_dict(self, data):
        return {
            id: {
                "question": question,
                "answers": [corr, wr1, wr2, wr3],
                "difficulty": difficulty,
            }
            for id, question, corr, wr1, wr2, wr3, difficulty in data
        }

    def get_questions(self, topic, difficulty):
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(
            f"SELECT id, question, correct_answer, wrong_1, wrong_2, wrong_3, difficulty FROM {self.topics[topic]} WHERE difficulty={difficulty};"
        )
        questions = self.questions_to_dict(cursor.fetchall())
        conn.close()
        return questions

    def add_player(self, name: str, password) -> None:
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO player (name, password) VALUES ('{name}', '{password}');"
        )
        conn.commit()
        conn.close()

    def get_player_list(self) -> list:
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM player;")
        player_list = [x[0] for x in cursor.fetchall()]
        conn.close()
        return player_list

    def get_password(self, name: str) -> bytes:
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"SELECT password FROM player WHERE name='{name}';")
        password = cursor.fetchall()[0][0]
        conn.close()
        return password

    def get_answered_questions(self, name: str) -> dict:
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(f"SELECT answered_questions FROM player WHERE name='{name}';")
        answers = cursor.fetchall()[0][0]
        if answers:
            self.answered_questions = answers
        conn.close()
        return self.answered_questions

    def add_answered_questions(self, name: str, answered_questions: dict) -> None:
        answ_json = json.dumps(answered_questions)
        conn = psy.connect(**config)
        cursor = conn.cursor()
        cursor.execute(
            f"UPDATE player SET answered_questions='{answ_json}' WHERE name='{name}';"
        )
        conn.commit()
        conn.close()

    def add_new_question(self, player: str, question):
        pass


if __name__ == "__main__":
    db = Db_handler()
    print(db.get_password("Philip"))
