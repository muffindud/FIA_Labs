#!./venv/bin/python3

from rules import TOURIST_RULES
from src.production import *
from json import dumps
import random


def main():
    while True:
        print("\033[H\033[J")
        print("Select the type of reasoning you want to use:")
        print("[1] Forward chaining")
        print("[2] Backward chaining")
        print("[0] Exit")

        try:
            choice = int(input("Enter your choice: \n>"))
        except ValueError:
            print("\033[H\033[J")
            print("Invalid choice. Please enter a number.")
            input()
            continue
        else:
            print("\033[H\033[J")
            if choice == 0:
                break

            elif choice == 1:
                print("Forward chaining")
                print("What's the tourist's name?")
                tourist_name = input(">")

                # Get possible initial facts
                initial_facts = list(get_possible_initial_facts(TOURIST_RULES))
                true_facts = []
                false_fact = []
                fact_count = len(initial_facts)
                fact_index = 0

                # Shuffle the fact list for different question order and grouping
                random.shuffle(initial_facts)

                # Multiple choice questions
                print("Which of the following facts do you agree with?")
                while fact_index < int(fact_count / 3):
                    print(f"[{fact_index+1}] {initial_facts[fact_index].replace('(?x)', tourist_name)}")
                    fact_index += 1
                answer = input(">").split(" ")

                for i in range(int(fact_count / 3)):
                    if str(i+1) in answer:
                        true_facts.append(initial_facts[i])
                    else:
                        false_fact.append(initial_facts[i])

                linked_facts = get_linked_facts(TOURIST_RULES, true_facts)

                for fact in linked_facts:
                    if not fact in true_facts:
                        question_type = random.choice([1, 2])
                        if question_type == 1:
                            print(f"Do you agree that {fact.replace('(?x)', tourist_name)}? [y/n]")
                            answer = input("[y/n] >").lower()
                            if answer == "y":
                                true_facts.append(fact)
                            else:
                                false_fact.append(fact)
                        elif question_type == 2:
                            print(f"On a scale of 1-10, how much do you agree that {fact.replace('(?x)', tourist_name)}?")
                            answer = int(input("[1-10]>"))
                            if answer > 5:
                                true_facts.append(fact)
                            else:
                                false_fact.append(fact)

                print("Conclusion: " + forward_chain(TOURIST_RULES, true_facts)["conclusion"].replace('(?x)', tourist_name))

            elif choice == 2:
                print("Backward chaining")
                print("Hypothesis:")
                hypothesis = input(">")
                facts = backward_chain(TOURIST_RULES, hypothesis)
                for fact in facts:
                    if isinstance(fact, OR):
                        for i in range(len(fact)):
                            print(fact[i], end="")
                            if i < len(fact) - 1:
                                print(" OR ", end="")
                        else:
                            print()
                    else:
                        print(fact)

            else:
                print("Invalid choice. Please enter a valid option.")

            input()


if __name__ == "__main__":
    main()
