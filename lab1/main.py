from rules import TOURIST_RULES
from src.production import *
from json import dumps
from random import shuffle


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
                shuffle(initial_facts)

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
                
                possible_concusions = get_possible_conclusion_from_facts(TOURIST_RULES, set(true_facts))
                possible_facts = get_initial_facts_for_conclusions(TOURIST_RULES, possible_concusions)
                unanswared_facts = list(set(possible_facts) - set(true_facts))
                print(possible_concusions)

                # unanswared_facts_count = len(unanswared_facts)

                # while len(possible_concusions) > 1:
                #     print(possible_concusions)
                #     print("Do you agree that " + unanswared_facts[0].replace('(?x)', tourist_name) + "? [y/n]")
                #     answer = input(">").lower()
                #     if answer == "y":
                #         true_facts.append(unanswared_facts[0])
                #     else:
                #         false_fact.append(unanswared_facts[0])
                #     unanswared_facts.pop(0)
                #     unanswared_facts_count -= 1
                #     possible_concusions = get_possible_conclusion_from_facts(TOURIST_RULES, set(true_facts))

                # print(possible_concusions)

                # print(forward_chain(TOURIST_RULES, true_facts, false_fact, tourist_name))

            elif choice == 2:
                print("Backward chaining")
                # backward_chain(TOURIST_RULES, TEST_DATA, HYPOTHESIS)
            
            else:
                print("Invalid choice. Please enter a valid option.")

            input()


if __name__ == "__main__":
    main()
