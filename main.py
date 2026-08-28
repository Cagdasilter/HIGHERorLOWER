import random
from art import logo, vs
from game_data import data

final_score = 0
is_game_over = False

def choose_first_person():
    choose_a_person = random.choice(data)
    return choose_a_person


def choose_second_person():
    choose_a_person = random.choice(data)
    return choose_a_person


def calculate_answer():
    answer = ""
    if first_person["follower_count"] > second_person["follower_count"]:
        answer = "a"
    elif first_person["follower_count"] < second_person["follower_count"]:
        answer = "b"
    return answer

def question_part():
    player_guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    global is_game_over
    global final_score

    if correct_answer == player_guess:
        final_score += 1
        print(f"You are right! Current score: {final_score}.")
    elif correct_answer != player_guess:
        print(f"Sorry, that's wrong. Final score: {final_score}")
        is_game_over = True


first_person = choose_first_person()

def print_person_a(person_in):
    person_name = person_in["name"]
    person_description = person_in["description"]
    person_country = person_in["country"]
    print(f"Compare A: {person_name}, a {person_description}, from {person_country}")

def print_person_b(person_in):
    person_name = person_in["name"]
    person_description = person_in["description"]
    person_country = person_in["country"]
    print(f"Against B: {person_name}, a {person_description}, from {person_country}")


while not is_game_over:
    print(logo)
    print_person_a(first_person)
    second_person = choose_second_person()
    while first_person == second_person:
        second_person = choose_second_person()
    print(vs)
    print_person_b(second_person)
    correct_answer = calculate_answer()
    question_part()
    first_person = second_person
