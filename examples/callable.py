from pprint import pprint

from PyInquirer import prompt


# This is a workaround for using callables to avoid redundant code,
# such as parsing/type-checking, during validation.


def int_validator(*func_args):
    func = func_args[0]
    def wrapper(*args):
        try:
            value = (int(args[0]), )
        except ValueError:
            return "Please enter a valid integer"
        else:
            return func(*value)
    return wrapper


def sum_validator(value):
    return value == 4 or "That is not the answer"


questions = [
    {
        'type': 'input',
        'name': 'sum',
        'message': 'What\'s 2 + 2?',
        'validate': int_validator(sum_validator),
        'filter': lambda val: int(val)
    },
    {
        'type': 'input',
        'name': 'subtract',
        'message': 'What\'s 3 - 1?',
        'validate': int_validator(lambda val: val == 2 or "That is not the answer"),
        'filter': lambda val: int(val)
    }
]

answers = prompt(questions)
pprint(answers)
