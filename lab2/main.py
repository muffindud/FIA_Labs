from pacman import main as pacman
import sys


def main(args):
    match args[1]:
        case '1':
            pacman("-p MinimaxAgent -a depth=4,evalFn=customEval --frameTime=0 -n 1".split(' '))
        case '2':
            pacman("-p AlphaBetaAgent -a depth=3 --frameTime=0 -n 1".split(' '))
        case '3':
            pacman("-p MinimaxAgent -a depth=3,evalFn=customImprovedEval --frameTime=0 -n 1".split(' '))
        case '4':
            ...
        case '5':
            ...
        case '6':
            ...
        case '7':
            ...


if __name__ == '__main__':
    main(sys.argv)
