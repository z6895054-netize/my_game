from rich.console import Console 
console=Console()
question = [
("what is your name?",
["A:sara", "B:zizi", "C:ali", "D:abas"], "B"),
("how old are you?",
["A:20", "B:21", "C:22", "D:23"], "A"),
("what is your favorite color?",
["A:black", "B:blue", "C:pink", "D:red"], "C")
]

def show_menu():
    choice = input("Do you want to start the game? (yes or No?): " ).strip().lower()
    if choice == "no":
        print("Goodbye! See you later.")
        exit()
    elif choice == "yes":
        return True
    else:
        print("Please enter yes or no.")
def play_quiz():
    score = 0
    BONUS = 10
    PENALTY = 3
    correct = 0
    for qu, opt, ans in question:
        print(qu)
    for op in opt:
        print(op)
    useranswer = input("Your choice: ").strip().upper()
    if useranswer == ans:
        Console.print("Correct!!",style="white on red")
        score += BONUS
        correct += 1
    else:
        Console.print("Incorrect",style=" red on blue")
        score -= PENALTY
    return score,correct
def show_results(score,correct):
    print(f"Your final score: {score}")
    print(f"Your answered correctly: {correct}")
    print(f"Percentage: {correct / len(question)*100}")
while True:
    if show_menu():
        break
play_quiz()
score, correct = play_quiz()
show_results(score, correct)

print("hi")
