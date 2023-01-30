'''Select strategy impl to use'''


from play_pi.phrases.klmcw import KlmcwPhrasesStrategy
from play_pi.phrases.phrase import PhrasesStrategy
from play_pi.phrases.vihart import ViHartPhrasesStrategy

supported: dict[str, PhrasesStrategy] = {
    'klmcw': KlmcwPhrasesStrategy,
    'vihart': ViHartPhrasesStrategy
}


def select_strategy(name: str) -> PhrasesStrategy:
    strategy = supported[name]() if name in supported else None
    if not strategy:
        raise ValueError(f'strategy name={name} is not supported')
    return strategy


def supported_strategies() -> list[str]:
    '''List of supported strategies that can be selected'''
    return sorted(supported)
