'''Model of a musical phrase'''


from dataclasses import dataclass
from typing import Protocol

from play_pi.palletes.notes import MusicalNote


@dataclass
class Phrase:
    length: int
    digits: list[int]
    pallete: list[MusicalNote]

    @property
    def notes(self) -> str:
        return ' '.join([self.pallete[d].name for d in self.digits])


class PhrasesStrategy(Protocol):
    @property
    def digits(self) -> str:
        '''Returns digits used'''
        ...

    @property
    def phrases(self) -> list[Phrase]:
        '''Returns list of Phrase objects'''
        ...
