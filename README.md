# pi-day-2023-with-py
Pi day 2023 project using Python

## Overview
Output digits of Pi as phrases of a musical composition.

## Setup
_This assumes a bash shell on Fedora 37._

Install the python dependencies: ```./create_venv```

Install the system dependencies: ```sudo dnf install fluidsynth lilypond```

## Output
You can listen to the output with these links:
* [notes_with_pi_in_a_minor.mp3](./clips/notes_with_pi_in%20a_minor.mp3) - don't expect too much - _pi is randomly irrational after all_
* [power_chords_with_pi.mp3](./clips/power_chords_with_pi.mp3) - _appropriate for such an irrational number_ ;)

```
python -m play_pi play --strategy klmcw --repeat random --tempo 60 2>/dev/null
Using preset Piano Merlin for grand piano
Using preset Strings SP1 for strings

Phrase 1 - repeated 3 times
C4 A3 D4 A3 E4

Phrase 2 - repeated 4 times
B4 B3 F4

Phrase 3 - repeated 2 times
E4 C4 E4 A4

Phrase 4 - repeated 2 times
B4 G4 B4

Phrase 5 - repeated 3 times
C4 B3 C4 A4

Phrase 6 - repeated 3 times
D4 F4 B3 F4 D4

Phrase 7 - repeated 3 times
C4 C4 A4 C4

Phrase 8 - repeated 3 times
B3 G4 B4 E4 C5 B3 A4 A4

Phrase 9 - repeated 2 times
D4 A3 B4

Phrase 10 - repeated 2 times
G4 A3 F4 B4

Phrase 11 - repeated 3 times
C4 B4 B4 C4 G4 E4 A3 C5 E4 A4 B3 C5 B4 G4 D4 B4 D4 D4 E4 B4 B3

Phrase 12 - repeated 2 times
C4 C5 G4 A4 A3 F4
```


## Credit where credit is due ...
The inspiration for this project was taken partially from Vi Hart - [Pi Day 3/14 1:59AM - Spring Ahead](https://www.youtube.com/watch?v=AHrth9lOfzo&ab_channel=Vihart).

I was especially intrigued by her usage of segments of the digits of PI as repeating, arpeggiatic phrases of the piece.

I was also inspired by Marc Evanstein's work - [The Making of the Rhythm of the Primes](https://youtu.be/GzrTmukxUxA) through which I was introduced to ...

The [SCAMP library](http://scamp.marcevanstein.com/).
