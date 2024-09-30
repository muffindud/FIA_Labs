from rules import TOURIST_RULES
from src.production import forward_chain, backward_chain
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
    data = forward_chain(TOURIST_RULES, TEST_DATA)
    print(dumps(data, indent=4))


if __name__ == "__main__":
    main()
