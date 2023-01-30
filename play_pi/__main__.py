'''Pi day 2023 with Py

Usage: play_pi play --strategy STRATEGY [--verbose] [--version] [--help]
       play_pi list [--verbose] [--version] [--help]

Options:
    --strategy STRATEGY     The strategy to use

    --verbose               DEBUG logging verbosity
    --version               The package version
    --help                  This help text
'''

import logging
import math
from pprint import pformat

from docopt import docopt

from play_pi.phrases.select_strategy import (select_strategy,
                                             supported_strategies)
from play_pi.utils.log import config_logging


def list(_: dict[str, any]):
    for s in supported_strategies():
        logging.info(s)


def play(opts: dict[str, any]):
    strategy_name = opts['--strategy']

    try:
        strategy = select_strategy(strategy_name)
        logging.debug(strategy)

        logging.debug(pformat(strategy.digits, width=110))
        logging.debug(pformat(strategy.phrases, width=110))

        for i, phrase in enumerate(strategy.phrases):
            print(f'Phrase {i + 1}')
            print(phrase.notes)
            print('')

    except ValueError as err:
        logging.error(err)


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
