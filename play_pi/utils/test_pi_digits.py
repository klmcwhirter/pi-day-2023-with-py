

from play_pi.utils.pi_digits import pi_digit_generator


def test_pi_digit_generator_should_have_1st_digit_of_3():
    digits = [d for d in pi_digit_generator(1)]

    assert 1 == len(digits)
    assert 3 == digits[0]


def test_pi_digit_generator_should_have_1st_70_digits():
    expected = '3141592653589793238462643383279502884197169399375105820974944592307816'
    digits = ''.join([str(d) for d in pi_digit_generator(70)])

    assert 70 == len(digits)
    assert expected == digits
