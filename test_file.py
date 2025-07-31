import pytest

@pytest.mark.parametrize("a,result",[(3,True),(4,False),(5,False)])

def test_iseven(a,result):
    assert (a % 2 == 0)==result

