import random
from PemaPelbar_02240088_A2_PB import PokemonBinder  #  Import from Part B
class ScoreTracker:
    def __init__(self):
        self.scores = {
            "Guess Number": 0,
            "Rock Paper Scissors": 0,
            "Trivia Quiz": 0,
            "Pokemon Binder": 0
        }
    def update_score(self, game, score):
        self.scores[game] = score

    def display_scores(self):
        print("Current Scores")
        for game, score in self.scores.items():
            print(f"{game}: {score}")
        print(f"Total Score: {sum(self.scores.values())}")
class GuessNumber:
    def __init__(self, score_tracker):
        self.score_tracker = score_tracker
    def play(self):
        print("Guess the Number")
        secret = random.randint(1, 100)
        attempts = 0
        while True:
            guess = input("Guess a number between 1 and 100 (or 'q' to quit): ")
            if guess.lower() == 'q':
                print(f"The secret number was {secret}.")
                break
            try:
                guess = int(guess)
                attempts += 1
                if guess < secret:
                    print("Too low!")
                elif guess > secret:
                    print("Too high!")
                else:
                    print(f"Correct! You guessed it in {attempts} attempts.")
                    score = max(0, 10 - attempts)
                    self.score_tracker.update_score("Guess Number", score)
                    print(f"Score: {score}")
                    break
            except ValueError:
                print("Please enter a valid number.")
class RockPaperScissors:
    def __init__(self, score_tracker):
        self.score_tracker = score_tracker
    def play(self):
        print("Rock Paper Scissors")
        options = ["rock", "paper", "scissors"]
        player_wins = 0
        for round_num in range(1, 4):
            print(f"Round {round_num}")
            user = input("Choose rock, paper, or scissors: ").lower()
            if user not in options:
                print("Invalid input.")
                continue
            computer = random.choice(options)
            print(f"Computer chose: {computer}")
            if user == computer:
                print("It's a tie.")
            elif (user == "rock" and computer == "scissors") or \
                 (user == "paper" and computer == "rock") or \
                 (user == "scissors" and computer == "paper"):
                print("You win this round!")
                player_wins += 1
            else:
                print("Computer wins this round.")
        self.score_tracker.update_score("Rock Paper Scissors", player_wins)
        print(f"Your score: {player_wins}")
class TriviaQuiz:
    def __init__(self, score_tracker):
        self.score_tracker = score_tracker
    def play(self):
        print("Trivia Quiz")
        questions = [
            {"category": "Science", "question": "What is the chemical symbol for water?", "options": ["A. H2O", "B. O2", "C. CO2", "D. HO"], "answer": "A"},
            {"category": "Math", "question": "What is 2+2?", "options": ["A. 4", "B. 5", "C. 3", "D. 1"], "answer": "A"},      
        ]
        score = 0
        for q in questions:
            print(f"Category: {q['category']}")
            print(q["question"])
            for option in q["options"]:
                print(option)
            while True:
                answer = input("Your answer (A/B/C/D): ").upper()
                if answer in ['A', 'B', 'C', 'D']:
                    break
                else:
                    print("Invalid input.")
            if answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer was {q['answer']}.")

        self.score_tracker.update_score("Trivia Quiz", score)
        print(f"Trivia score: {score}/{len(questions)}")
class GameSuite:
    def __init__(self):
        self.score_tracker = ScoreTracker()
        self.games = {
            '1': GuessNumber(self.score_tracker),
            '2': RockPaperScissors(self.score_tracker),
            '3': TriviaQuiz(self.score_tracker),
            '4': PokemonBinder(self.score_tracker)  #  Imported version
        }
    def show_menu(self):
        print("GAME MENU")
        print("1. Guess the Number")
        print("2. Rock Paper Scissors")
        print("3. Trivia Pursuit Quiz")
        print("4. Pokemon Card Binder Manager")
        print("5. View Scores")
        print("0. Exit")
    def run(self):
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")
            if choice in self.games:
                self.games[choice].menu() if choice == '4' else self.games[choice].play()
            elif choice == '5':
                self.score_tracker.display_scores()
            elif choice == '0':
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Please enter a number between 0-5.")
# Run the main game suite
GameSuite().run()
