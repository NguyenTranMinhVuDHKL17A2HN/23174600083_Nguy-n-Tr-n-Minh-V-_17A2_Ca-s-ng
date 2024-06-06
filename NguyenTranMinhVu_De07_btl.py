import random
import csv

def roll_dice():
    return random.randint(1, 6)

def calculate_total(dice):
    return sum(dice)

def check_guess(guess, total):
    return guess == total

def calculate_probabilities(results):
    total_rolls = len(results)
    probability_dict = {}
    for total in results:
        if total in probability_dict:
            probability_dict[total] += 1
        else:
            probability_dict[total] = 1
    for total in probability_dict:
        probability_dict[total] = probability_dict[total] / total_rolls
    return probability_dict

results = []
totals_set = set()
probability_dict = {}

def play_game():
    global probability_dict

    number_of_rolls = int(input("Enter the number of dice rolls: "))
    guesses = []
    for i in range(number_of_rolls):
        dice = [roll_dice(), roll_dice(), roll_dice()]
        total = calculate_total(dice)
        results.append(total)
        totals_set.add(total)
        guess = int(input(f"Roll {i + 1}: Guess the total of the three dice: "))
        guesses.append(guess)
        result = check_guess(guess, total)
        print(f"Roll result: {dice} -> Total: {total} -> Guess {'correct' if result else 'incorrect'}")
    
    probability_dict = calculate_probabilities(results)
    print("Probability of each total:")
    for total, prob in probability_dict.items():
        print(f"Total: {total}, Probability: {prob:.2%}")
    
    with open('dice_results.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Roll number', 'Total of three dice', 'Guess', 'Result (correct/incorrect)', 'Probability of total']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, total in enumerate(results):
            guess = guesses[i]
            guess_result = "correct" if check_guess(guess, total) else "incorrect"
            probability = calculate_probabilities(results[:i+1])[total]
            writer.writerow({'Roll number': i + 1, 'Total of three dice': total, 'Guess': guess, 'Result (correct/incorrect)': guess_result, 'Probability of total': f"{probability:.2%}"})

play_game()
