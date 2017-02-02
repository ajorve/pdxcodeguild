import sys

from functions.together import together


def test_together():
    together('knights', 'camalot')
    output = sys.stdout.getline().strip()
    assert output == 'k c' \
                     'n a' \
                     'i m' \
                     'g a' \
                     'h l' \
                     't o' \
                     's t'