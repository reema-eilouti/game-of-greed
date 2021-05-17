from tests.flow.flo import Flo

def test_quitter():
    Flo.test('flow/quitter.txt')

def test_wanna_play_yes_then_quit():
    Flo.test('flow/do_wanna_play_then_quit.txt')
