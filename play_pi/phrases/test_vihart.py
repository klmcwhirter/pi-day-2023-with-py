
from play_pi.phrases.vihart import ViHartPhrasesStrategy


digits_as_str = '3141592653589793238462643383279502884197169399375105820974944592307816'


def test_digits_is_len_70():
    strategy = ViHartPhrasesStrategy()

    digits = strategy.digits

    assert 70 == len(digits)


def test_digits_is_correct_70():
    strategy = ViHartPhrasesStrategy()

    digits = strategy.digits

    assert digits_as_str == digits
