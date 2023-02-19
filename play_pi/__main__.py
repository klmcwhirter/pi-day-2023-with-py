'''Pi day 2023 with Py

Usage: play_pi play --strategy STRATEGY [--repeat REPEAT] [--tempo TEMPO]
                    [--dry-run] [--verbose] [--version] [--help]
       play_pi list [--verbose] [--version] [--help]

Options:
    --strategy STRATEGY     The strategy to use
    --repeat REPEAT         The number of times to repeat each phrase or the string 'random' [default: 3]
    --tempo TEMPO           Tempo in beats per minute [default: 120]

    --dry-run               Show what would be done
    --verbose               DEBUG logging verbosity
    --version               The package version
    --help                  This help text
'''

import logging
import math
from pprint import pformat
from random import randrange

from docopt import docopt

from play_pi.phrases.select_strategy import (select_strategy,
                                             supported_strategies)
from play_pi.utils.log import config_logging
from play_pi.utils.scamp_driver import ScampDriver


def list(_: dict[str, any]):
    for s in supported_strategies():
        logging.info(s)


def repeat(val: str) -> int:
    if val == 'random':
        return randrange(2, 5)
    return int(val)


def play(opts: dict[str, any]):
    strategy_name = opts['--strategy']
    dry_run = opts['--dry-run']

    try:
        strategy = select_strategy(strategy_name)
        logging.debug(strategy)

        logging.debug(pformat(strategy.digits, width=110))
        logging.debug(pformat(strategy.phrases, width=110))

        if not dry_run:
            driver = ScampDriver(int(opts['--tempo']))

        print('')

        for i, phrase in enumerate(strategy.phrases):
            phrase.repeat = repeat(opts['--repeat'])

            print(f'Phrase {i + 1} - repeated {phrase.repeat} times')
            print(phrase.notes)
            # print(phrase.notes_as_pitch_with_repeat)
            print('')

            if not dry_run:
                driver.play(phrase.notes_as_pitch_with_repeat)

    except ValueError as err:
        logging.error(err)

    finally:
        if not dry_run:
            driver.stop()


commands = {
    'list': list,
    'play': play
}


def main():
    opts = docopt(__doc__, version=str(math.pi))
    config_logging(opts['--verbose'])
    logging.debug(opts)

    cmd = [v for k, v in commands.items() if k in opts and opts[k]][0]
    cmd(opts)


if __name__ == '__main__':
    main()
