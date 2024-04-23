from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with the key and the square of the value."""
    return k, float(v) ** 2
