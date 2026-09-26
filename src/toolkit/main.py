import sys

import typer

from .calculator import calculator_function
from .converter import converter_function

toolkit = typer.Typer()

@toolkit.command('calc', context_settings={"ignore_unknown_options": True})
def calc(calc_argument):
    answer = calculator_function(calc_argument)
    if type(answer) is list:
        print(answer[1], file=sys.stderr)
        raise SystemExit(answer[0])
    else:
        print(answer)

@toolkit.command('convert', context_settings={"ignore_unknown_options": True})
def convert(value, unit_from = typer.Option(...,'--from'), unit_to = typer.Option(...,'--to')):
    answer = converter_function(value,unit_from,unit_to)
    if type(answer) is list:
        print(answer[1], file=sys.stderr)
        raise SystemExit(answer[0])
    else:
        print(answer)


def main():
    toolkit()

if __name__ == "__main__":
    main()