import re


def replace_expression(line):
    replaced = ""
    previous_end = 0
    for match in re.finditer("{([^}]+)}", line):
        expression = match.group(1)
        replaced += (
            line[previous_end : match.start()] + f"{expression} = {eval(expression)}"
        )
        previous_end = match.end()
    replaced += line[previous_end:]
    return replaced
