from rules import TOURIST_RULES
from src.production import *
from json import dumps
from random import shuffle


TEST_DATA = (
    'John has a performant camera',
    'John films a lot',
    'John speaks loudly',
    'John doesn\'t take pictures',
    'John is rude'
)

HYPOTHESIS = 'John is a vlogger'


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
                        true_facts.append(initial_facts[i].replace("(?x)", tourist_name))
                    else:
                        false_fact.append(initial_facts[i].replace("(?x)", tourist_name))

                # Yes/No questions
                while fact_index < int(fact_count / 3) * 2:
                    print(f"Do you agree that {initial_facts[fact_index].replace('(?x)', tourist_name)}? [Y]es - [N]o")
                    answer = input(">")
                    if answer.lower() == "y":
                        true_facts.append(initial_facts[fact_index].replace("(?x)", tourist_name))
                    fact_index += 1

                for fact in answer:
                    true_facts.append(initial_facts[int(fact)-1].replace("(?x)", tourist_name))
                
                # Score questions
                while fact_index < fact_count:
                    print(f"How much do you agree that {initial_facts[fact_index].replace('(?x)', tourist_name)}? [1-10]")
                    answer = input(">")
                    if int(answer) > 5:
                        true_facts.append(initial_facts[fact_index].replace("(?x)", tourist_name))
                    fact_index += 1

                print("True facts: ", true_facts)
                print(forward_chain(TOURIST_RULES, set(true_facts)))

                # for fact in initial_facts:
                #     print("Do you agree that " + fact.replace("(?x)", tourist_name) + "? [Y]es - [N]o - [U]nsure")
                #     answer = input(">")
                #     if answer.lower() == "y":
                #         true_facts.append(fact.replace("(?x)", tourist_name))
                #     elif answer.lower() == "n":
                #         pass
                
                print("True facts: ", true_facts)
                print(forward_chain(TOURIST_RULES, set(true_facts)))

                # print("Do you agree that " + initial_facts[0].replace("(?x)", tourist_name) + "? [Y]es - [N]o - [U]nsure")
                # answer = input(">")
                # if answer.lower() == "y":
                #     true_facts.append(initial_facts[0].replace("(?x)", tourist_name))
                # elif answer.lower() == "n":
                #     pass
                    
                

            elif choice == 2:
                print("Backward chaining")
                # backward_chain(TOURIST_RULES, TEST_DATA, HYPOTHESIS)
            
            else:
                print("Invalid choice. Please enter a valid option.")

            input()


if __name__ == "__main__":
    # main()
    # print(forward_chain(TOURIST_RULES, ("Bob has weird claims",)))
    print(get_possible_conclusion_from_facts(TOURIST_RULES, ("Bob speaks Stellarian", "Bob has a performant camera")))
