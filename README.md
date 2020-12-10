dice_roller
==========

Simple utility to help keep rule logs from dnd sessions.

    echo "{<d20> + 1} > battle_log.txt
    dice_roller battle_log.txt
        rolling d20 on line 1: landet on 13
    cat battle_log.txt
    13(d20) + 1 = 14

## building

    pip install .

## testing

    pytest
