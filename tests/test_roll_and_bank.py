from tests.flow.flo import Flo


def test_bank_one_roll_then_quit():
    Flo.test('tests/flow/bank_one_roll_then_quit.txt')

def test_bank_first_for_two_rounds():
    Flo.test('tests/flow/bank_first_for_two_rounds.txt')
