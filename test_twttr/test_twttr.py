# implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_twttr.py

from twttr import shorten

def main():
    test_letter_cases()
    test_numbers()
    test_punctuation()

def test_letter_cases():
    assert shorten('apple') == 'ppl'
    assert shorten('BANANA') == 'BNN'
    assert shorten('OrAnGe') == 'rnG'

def test_numbers():
    assert shorten('1234') == '1234'

def test_punctuation():
    assert shorten('!?.,') == '!?.,'

if __name__ == "__main__":
    main()