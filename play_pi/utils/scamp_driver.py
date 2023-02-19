'''Driver that provides and integration with the scamp library.'''

from random import choice, uniform

from scamp import Session, wait


def flip() -> bool:
    return choice([True, False, True, True, False, True, True, True, False, True])


class ScampDriver:
    def __init__(self, tempo: int) -> None:
        self.session = Session()
        self.session.tempo = tempo
        self.piano = self.session.new_part('grand piano')
        self.strings = self.session.new_part('strings')

    def _chords_experiment(self, pitch: int, volume: float, duration: float, want_chords: bool = True) -> None:
        if flip():
            self.piano.play_note(pitch, volume, duration, blocking=False)

        if want_chords:
            if flip():
                self.piano.play_note(pitch + 3, volume, duration, blocking=False)
            elif flip():
                self.piano.play_note(pitch - 3, volume, duration, blocking=False)
            if flip():
                self.piano.play_note(pitch + 5, volume, duration, blocking=False)
            elif flip():
                self.piano.play_note(pitch - 5, volume, duration, blocking=False)

        if flip():
            self.strings.play_note(pitch, volume, duration, blocking=False)
        if want_chords:
            if flip():
                self.strings.play_note(pitch + 3, volume, duration, blocking=False)
            elif flip():
                self.strings.play_note(pitch - 3, volume, duration, blocking=False)
            if flip():
                self.strings.play_note(pitch + 5, volume, duration, blocking=False)
            elif flip():
                self.strings.play_note(pitch - 5, volume, duration, blocking=False)

        self.strings.play_note(pitch - 12, volume + 0.2, duration)

    def _default_playback(self, pitch: int, volume: float, duration: float) -> None:
        self.piano.play_note(pitch, volume, duration, blocking=False)
        self.strings.play_note(pitch, volume, duration, blocking=False)
        self.strings.play_note(pitch - 12, volume + 0.2, duration)

    def play(self, notes: list[int]):
        for pitch in notes:
            volume = uniform(0.5, 1.5)
            duration = uniform(0.3, 1.0)

            # playback_strategy = choice([
            #     self._chords_experiment,
            #     self._default_playback,
            #     self._default_playback,
            #     self._default_playback,
            #     self._chords_experiment,
            #     self._default_playback,
            #     self._chords_experiment,
            #     self._default_playback,
            #     self._default_playback,
            # ])
            # playback_strategy = self._chords_experiment

            playback_strategy = self._default_playback

            playback_strategy(pitch=pitch, volume=volume, duration=duration)

    def stop(self) -> None:

        for pitch in (60, 57, 64):
            self.piano.play_note(pitch, 1.0, 2.0, blocking=False)

        wait(2.5)
