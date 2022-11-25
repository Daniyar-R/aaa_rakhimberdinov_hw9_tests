import pytest
from morse import decode


@pytest.mark.parametrize('test_input_morse,expected',
                         [('- . ... -', 'TEST'),
                          ('25', '..--- .....'),
                          ('---|-.-', 'OK')])
def test_deocde(test_input_morse, expected):
    assert decode(test_input_morse) == expected
