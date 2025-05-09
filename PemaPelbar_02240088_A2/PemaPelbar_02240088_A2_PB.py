# pokemon_binder.py
MAX_POKEDEX = 1025
CARDS_PER_PAGE = 64
GRID_ROWS = 8
GRID_COLS = 8

class PokemonBinder:
    def __init__(self, score_tracker=None):
        self.binder = {}
        self.score_tracker = score_tracker

    def calculate_position(self, pokedex_number):
        index = pokedex_number - 1
        page = index // CARDS_PER_PAGE + 1
        position = index % CARDS_PER_PAGE
        row = position // GRID_COLS + 1
        col = position % GRID_COLS + 1
        return page, row, col

    def add_card(self):
        try:
            number = int(input("Enter a Pokedex number (1 to 1025): "))
            if number < 1 or number > MAX_POKEDEX:
                print("That's not a valid number. Try something between 1 and 1025.")
                return

            if number in self.binder:
                page, row, col = self.binder[number]
                print(f" That card is already in your binder! Page {page}, Row {row}, Column {col}")
            else:
                page, row, col = self.calculate_position(number)
                self.binder[number] = (page, row, col)
                print(f"Added Pokemon #{number} to Page {page}, Row {row}, Column {col}!")

                if self.score_tracker:
                    self.score_tracker.update_score("Pokemon Binder", len(self.binder))

                if len(self.binder) == MAX_POKEDEX:
                    print("Incredible! You've caught them ALL!")
        except ValueError:
            print("Oops! That wasn't a number. Please type a number between 1 and 1025.")

    def view_binder(self):
        if not self.binder:
            print("Your binder is empty. Time to catch some Pokemon!")
        else:
            print("Here are the cards you've added:")
            for number in sorted(self.binder):
                page, row, col = self.binder[number]
                print(f" Pokemon #{number}: Page {page}, Row {row}, Column {col}")

    def reset_binder(self):
        confirm = input("Are you sure you want to clear your binder? Type 'CONFIRM' to continue: ")
        if confirm.upper() == 'CONFIRM':
            self.binder.clear()
            print("Binder has been reset. Time for a fresh start!")
            if self.score_tracker:
                self.score_tracker.update_score("Pokemon Binder", 0)
        else:
            print("ohh! That was close.")

    def menu(self):
        while True:
            print("Pokemon Binder Menu")
            print("1. Add a card")
            print("2. View binder")
            print("3. Reset binder")
            print("4. Return to main menu")
            choice = input("What would you like to do? (1-4): ")

            if choice == '1':
                self.add_card()
            elif choice == '2':
                self.view_binder()
            elif choice == '3':
                self.reset_binder()
            elif choice == '4':
                break
            else:
                print("Ohh, that's not a valid choice. Please pick 1, 2, 3, or 4.")
