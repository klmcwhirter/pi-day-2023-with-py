'''Test for select_strategy module'''

import pytest

from play_pi.phrases.klmcw import KlmcwPhrasesStrategy
from play_pi.phrases.select_strategy import (select_strategy,
                                             supported_strategies)
from play_pi.phrases.vihart import ViHartPhrasesStrategy


def test_supported_strategies_should_provide_sorted_list_keys():
    expected = sorted(supported_strategies())

    actual = supported_strategies()

    assert expected == actual


@pytest.mark.parametrize(
    'strategy_name,expected', [
        ('klmcw', KlmcwPhrasesStrategy),
        ('vihart', ViHartPhrasesStrategy)
    ]
)
def test_select_strategy_provides_correct_type_if_supprted(strategy_name, expected):
    strategy = select_strategy(strategy_name)

    assert expected == type(strategy)
