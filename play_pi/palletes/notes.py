'''Frequency of notes interesting to build a pallete of 10 notes

    From https://en.wikipedia.org/wiki/Piano_key_frequencies
'''

from dataclasses import dataclass


@dataclass
class MusicalNote:
    name: str
    midi_num: int
    freq_hz: float


MusicalNotes = {
    'E5':   MusicalNote('E5',   76, 659.2551),
    'D#5':  MusicalNote('D#5',  75, 622.2540),
    'D5':   MusicalNote('D5',   74, 587.3295),
    'C#5':  MusicalNote('C#5',  73, 554.3653),
    'C5':   MusicalNote('C5',   72, 523.2511),
    'B4':   MusicalNote('B4',   71, 493.8833),
    'A#4':  MusicalNote('A#4',  70, 466.1638),
    'A4':   MusicalNote('A4',   69, 440.0000),
    'G#4':  MusicalNote('G#4',  68, 415.3047),
    'G4':   MusicalNote('G4',   67, 391.9954),
    'F#4':  MusicalNote('F#4',  66, 369.9944),
    'F4':   MusicalNote('F4',   65, 349.2282),
    'E4':   MusicalNote('E4',   64, 329.6276),
    'D#4':  MusicalNote('D#4',  63, 311.1270),
    'D4':   MusicalNote('D4',   62, 293.6648),
    'C#4':  MusicalNote('C#4',  61, 277.1826),
    'C4':   MusicalNote('C4',   60, 261.6260),  # middle C
    'B3':   MusicalNote('B3',   59, 246.9417),
    'A#3':  MusicalNote('A#3',  58, 233.0819),
    'A3':   MusicalNote('A3',   57, 220.0000)
}
