from rules import TOURIST_RULES
from src.production import *
from json import dumps


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

                initial_facts = list(get_possible_initial_facts(TOURIST_RULES))
                true_facts = []
                # print(initial_facts)

                for fact in initial_facts:
                    print("Do you agree that " + fact.replace("(?x)", tourist_name) + "? [Y]es - [N]o - [U]nsure")
                    answer = input(">")
                    if answer.lower() == "y":
                        true_facts.append(fact.replace("(?x)", tourist_name))
                    elif answer.lower() == "n":
                        pass
                
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
    main()
    # print(forward_chain(TOURIST_RULES, ("Bob has weird claims",)))
