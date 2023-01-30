# Vi Hart composition with Pi

## Overview
Phrase analysis from [Pi Day 3/14 1:59AM - Spring Ahead](https://www.youtube.com/watch?v=AHrth9lOfzo&ab_channel=Vihart).

## Phrases

```python
# 3.1415 926 5358 979 3238 46264 3383 27950288 419 7169 399375105820974944592 307816 ...
phrases = [
    '31415',
    '926',
    '5358',
    '979',
    '3238',
    '46264',
    '3383',
    '27950288',
    '419',
    '7169',
    '399375105820974944592',
    '307816'
]

for phrase in phrases:
    print(f'phrase={phrase}, len={len(phrase)}')
print()

for phrase in phrases:
    print(len(phrase), end=', ')
print()
```
