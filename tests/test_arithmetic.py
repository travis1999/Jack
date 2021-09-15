from jack import jack
import pytest


def test_arithmetic():
    assert jack.add(1, 2) == 3
    assert jack.sub(1, 2) == -1
    assert jack.mul(1, 2) == 2
    assert jack.div(1, 2) == 0.5


def test_invalid_arg():
    with pytest.raises(TypeError):
        jack.add(1, '2')
