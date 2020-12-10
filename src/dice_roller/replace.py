import re
from random import randrange


def replace_expression(line):
    replaced = ""
    previous_end = 0
    for match in re.finditer("{([^}]+)}", line):
        expression1, expression2 = replace_dice(match.group(1))
        replaced += (
            line[previous_end : match.start()] + f"{expression1} = {eval(expression2)}"
        )
        previous_end = match.end()
    replaced += line[previous_end:]
    return replaced


def replace_dice(expression):
    replaced1 = ""
    replaced2 = ""
    previous_end = 0
    print(expression)
    for match in re.finditer("<d([^>]+)>", expression):
        num_sides = int(match.group(1))
        replaced1 += (
            expression[previous_end : match.start()]
            + f"{randrange(num_sides)}(d{num_sides})"
        )
        replaced2 += (
            expression[previous_end : match.start()] + f"{randrange(num_sides)}"
        )
        previous_end = match.end()
    replaced1 += expression[previous_end:]
    replaced2 += expression[previous_end:]
    return replaced1, replaced2
