from typing import NamedTuple


class Result(NamedTuple):
    win: bool 
    symbol:  str
    count: int