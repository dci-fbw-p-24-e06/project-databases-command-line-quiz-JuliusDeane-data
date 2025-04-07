from game_logic import Game
from db_handler import Db_handler
from input_handler import check_int_input, check_str_input_blacklist, check_str_input_whitelist

class CLI_Menu:
    def __init__(self, player):
        self.player = player
        self.status = True

        self.main_menu_choices = {
            1: "New Game",
            2: "See Highscores",
            3: "Add Question",
            4: "Quit Game"
        }

        self.difficulty_levels = {
            "It's all computer! (easy)": 1,
            "Vibe coder (medium)": 2,
            "1 c4n r34d th1s (advanced)": 3,
            "DCI Coach (hard)": 5
        }

        self.topics = {
            "General Python": 1,
            "Functions": 2,
            "Classes": 3,
            "File Handling": 4
        }
    
    def main_menu(self):
        while self.status:
            print("#__MAIN MENU__#")
            for key, value in self.main_menu_choices.items():
                print(f"{key}. {value}")
            menu_choice = check_int_input(
                "Make your choice: ",
                (1, len(self.main_menu_choices)+1)
                )
            if menu_choice == 1:
                self.new_game()
            elif menu_choice == 2:
                print("Highscores not available right now")
            elif menu_choice == 3:
                print("Not yet implemented")
            elif menu_choice == 4:
                print(f"Thank you for playing.\nSee you next time {self.player}!")
                self.status = False

    def new_game(self):
        print("__Setup New Game__")
        topic = self.set_topic()
        difficulty = self.set_difficulty()
        rounds = self.set_rounds()
        g = Game(player=self.player, total_rounds=rounds, topic=topic, difficulty=difficulty)
        g.game_round()

    def set_topic(self):
        print("Choose topic:")
        for key, value in self.topics.items():
            print(f"{value}. {key}")
        topic_choice = check_int_input(text="Your choice (1-4): ", int_range=(1, 5))
        return topic_choice

    def set_difficulty(self):
        print("Choose difficulty:")
        for key, value in self.difficulty_levels.items():
            print(f"{value}. {key}")
        diff_choice = check_int_input(text="Your choice (1-5): ", int_range=(1, 6), exclude=[4])
        return diff_choice
        
    def set_rounds(self):
        rounds = check_int_input(text="Enter number of rounds (1-20): ", int_range=(1, 21))
        return rounds
    

class Login(Db_handler):
    def __init__(self):
        self.player_list = self.get_player_list()
        self.player = ""
    
    def new_player(self):
        player_name = check_str_input_blacklist("Insert player name: ", self.player_list)
        password = input("Insert password: ")
        self.add_player(player_name, password)
        self.player = player_name
    
    def existing_player(self):
        player_name = check_str_input_whitelist("Insert player name: ", self.player_list, 'n')
        player_password = self.get_password(player_name)
        password = check_str_input_whitelist("Insert password: ", player_password, 'n')
        if password == player_password:
            self.player = player_name

    def login_screen(self):
        print("##__THE PYTHON QUIZ__##")
        print("1. Login existing player\n2. Add new player")
        choice = check_int_input("Your choice (1-2): ", (1,3))
        if choice == 1:
            self.existing_player()
        elif choice == 2:
            self.new_player()
        return self.player
        



if __name__ == '__main__':
    login = Login()
    player = login.login_screen()
    m = CLI_Menu(player)   
    m.main_menu()
    #print(login.player_list)