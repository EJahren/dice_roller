import pytest
from dice_roller.__main__ import parse_args_and_run


def test_help_message(capsys):
    with pytest.raises(SystemExit) as system_exit:
        parse_args_and_run(["dice_roller", "-h"])
        assert system_exit.code == 0
    assert "dice_roller" in capsys.readouterr().out


def test_simple_replace(tmpdir):
    battlelog = tmpdir.join("battlelog.txt")
    battlelog.write("{<d20> + 1}")

    parse_args_and_run(["dice_roller", str(battlelog)])
    assert "(d20) + 1 = " in battlelog.read()
