class Menu:
    def __init__(self):
        self.main_menu_choices = {
            1: "New Game",
            2: "Add Player",
            3: "See Highscores",
            4: "Add Question",
            5: "Quit Game"
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
        menu_choice = self.check_int_input("Make your choice: ", (1, 6))
        return menu_choice

    def check_int_input(self, text, int_range=(1, 999999)):
        choice = ""
        while not choice:    
            try:
                choice = int(input(text))
            except ValueError:
                print("Wrong input. Please only input a number.")
                choice = ""
            if choice not in range(*int_range) and isinstance(choice, int):
                print("Number out of range. Please choose a valid number.")
                choice = ""
        else:
            return choice

    def set_difficulty(self):
        print("Choose difficulty:")
        for key, value in self.difficulty_levels.items():
            print(f"{key}. {value}")
        diff_choice = self.check_int_input(text="Your choice (1-5): ", int_range=(1,6))
        return diff_choice
        
    def set_rounds(self):
        rounds = self.check_int_input(text="Enter number of rounds (1-20): ", int_range=(1,21))
        return rounds
    




m = Menu()

print(m.main_menu())