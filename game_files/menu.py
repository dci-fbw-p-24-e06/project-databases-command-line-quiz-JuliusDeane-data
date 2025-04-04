from game_logic import Game
from input_handler import check_int_input

class CLI_Menu:
    def __init__(self):
        self.main_menu_choices = {
            1: "New Game",
            2: "See Highscores",
            3: "Add Question",
            4: "Quit Game"
        }
        self.difficulty_levels = {
            1: "It's all computer! (easy)",
            2: "Vibe coder (medium)",
            3: "1 c4n r34d th1s (advanced)",
            4: "DCI Coach (hard)",
            5: "Mix it up (all levels)"}
    
    def main_menu(self):
        print("#__MAIN MENU__#")
        for key, value in self.main_menu_choices.items():
            print(f"{key}. {value}")
        menu_choice = check_int_input("Make your choice: ", (1, len(self.main_menu_choices)+1))
        if menu_choice == 1:
            self.new_game()

    def new_game(self):
        print("__Setup New Game__")
        difficulty = self.set_difficulty()
        rounds = self.set_rounds()
        g = Game(rounds, difficulty)
        g.game_round()

    def set_difficulty(self):
        print("Choose difficulty:")
        for key, value in self.difficulty_levels.items():
            print(f"{key}. {value}")
        diff_choice = check_int_input(text="Your choice (1-5): ", int_range=(1, 6))
        return self.difficulty_levels[diff_choice]
        
    def set_rounds(self):
        rounds = check_int_input(text="Enter number of rounds (1-20): ", int_range=(1, 21))
        return rounds
    



if __name__ == '__main__':
    m = CLI_Menu()

    while True:
        m.main_menu()