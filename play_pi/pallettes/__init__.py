'''Pallets of notes for use to map to digits 0-9'''


__all__ = [
    'MusicalNote',
    'A_MINOR',
    'C_MAJOR'
]

from play_pi.pallettes.notes import MusicalNote, MusicalNotes

A_MINOR = [
    MusicalNotes['C5'],  # 0
    MusicalNotes['A3'],  # 1
    MusicalNotes['B3'],  # 2
    MusicalNotes['C4'],  # 3
    MusicalNotes['D4'],  # 4
    MusicalNotes['E4'],  # 5
    MusicalNotes['F4'],  # 6
    MusicalNotes['G4'],  # 7
    MusicalNotes['A4'],  # 8
    MusicalNotes['B4'],  # 9
]

C_MAJOR = [
    MusicalNotes['E5'],  # 0
    MusicalNotes['C4'],  # 1
    MusicalNotes['D4'],  # 2
    MusicalNotes['E4'],  # 3
    MusicalNotes['F4'],  # 4
    MusicalNotes['G4'],  # 5
    MusicalNotes['A4'],  # 6
    MusicalNotes['B4'],  # 7
    MusicalNotes['C5'],  # 8
    MusicalNotes['D5'],  # 9
]
