'''Model of a musical phrase'''


from dataclasses import dataclass
from typing import Protocol

from play_pi.pallettes.notes import MusicalNote


@dataclass
class Phrase:
    length: int
    digits: list[int]
    pallete: list[MusicalNote]

    @property
    def notes(self) -> str:
        return ' '.join([self.pallete[d].name for d in self.digits])

    @property
    def notes_as_pitch(self) -> str:
        return ' '.join([str(self.pallete[d].midi_num) for d in self.digits])

    @property
    def notes_as_pitch_with_repeat(self) -> list[int]:
        return [self.pallete[d].midi_num for _ in range(self.repeat) for d in self.digits]

    @property
    def repeat(self) -> int:
        return self._repeat

    @repeat.setter
    def repeat(self, val: int) -> None:
        self._repeat = val


class PhrasesStrategy(Protocol):
    @property
    def digits(self) -> str:
        '''Returns digits used'''
        ...

    @property
    def phrases(self) -> list[Phrase]:
        '''Returns list of Phrase objects'''
        ...
