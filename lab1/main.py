from rules import TOURIST_RULES
from src.production import forward_chain, backward_chain


TEST_DATA = (
    'John has a performant camera',
    'John films a lot',
    'John speaks loudly',
    'John doesn\'t take pictures',
    'John is rude'
)


def main():
    result = forward_chain(TOURIST_RULES, TEST_DATA, verbose=False)
    for item in result:
        if item not in TEST_DATA:
            print(item)


if __name__ == "__main__":
    main()
