'''Vi Hart phraseology'''


from itertools import islice

from play_pi.palletes import A_MINOR
from play_pi.phrases.phrase import Phrase
from play_pi.utils.pi_digits import pi_digit_generator


class KlmcwPhrasesStrategy:
    # 3141592653589793238462643383279502884197169399375105820974944592307816 - 70 digits
    DIGITS_TO_USE = 70
    PHRASE_LENS = [5, 3, 4, 3, 4, 5, 4, 8, 3, 4, 21, 6]
    PHRASE_KEYS = [A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR, A_MINOR]

    def __init__(self) -> None:
        self._digits_used = list(pi_digit_generator(KlmcwPhrasesStrategy.DIGITS_TO_USE))
        digits_used_iter = iter(self._digits_used)
        self._phrases = [
            Phrase(pl, list(islice(digits_used_iter, pl)), pk)
            for (pl, pk) in zip(KlmcwPhrasesStrategy.PHRASE_LENS, KlmcwPhrasesStrategy.PHRASE_KEYS)
        ]

    @property
    def digits(self) -> str:
        '''Returns digits used'''
        return ''.join([str(d) for d in self._digits_used])

    @property
    def phrases(self) -> list[Phrase]:
        '''Returns list of Phrase objects'''
        return self._phrases.copy()

    def __repr__(self) -> str:
        return f'KlmcwPhrasesStrategy(digits={self.digits}, phrases={self.phrases})'
