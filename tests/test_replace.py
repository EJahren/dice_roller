from dice_roller.replace import replace_expression


def test_replace_expression_just_math():
    assert replace_expression("{1 + 1}") == "1 + 1 = 2"


def test_replace_expression_just_two_math():
    assert replace_expression("{1 + 1} and {1 + 2}") == "1 + 1 = 2 and 1 + 2 = 3"


def test_replace_expression_not_match():
    assert replace_expression("Hello world") == "Hello world"


def test_replace_expression_d20():
    assert "(d20) + 1 = " in replace_expression("{<d20> + 1}")
