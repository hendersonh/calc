import pytest
import calc 

@pytest.mark.parametrize('n1, n2, sum', [(5, 5, 10),
                                             (-5, 5, 0),
                                             (-10, -10, -20),
                                             (0, 100, 100)
                                             ])
def test_add(n1, n2, sum):
    assert sum == calc.add(n1, n2) 


@pytest.mark.parametrize('n1, n2, sum', [(5, 5, 0),
                                             (-5, 5, 10),
                                             (-10, -10, 0),
                                             (0, 100, -100)
                                             ])
def test_sub(n1, n2, result):
    assert result == calc.sub(n1, n1)