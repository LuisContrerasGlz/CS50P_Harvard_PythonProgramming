# Implement three or more functions that collectively test your implementation of value thoroughly, each of whose names should begin with test_ so that you can execute your tests with: pytest test_bank.py

# Importing value from Bank
from bank import value

# Def main function caling the testing functions
def main():
    test_hello_cases()
    test_starting_with_h()
    test_other_cases()


def test_hello_cases():
    assert value('hello') == 0
    assert value('HELLO') == 0
    assert value('hello, Gi') == 0
    assert value('Hello, Gi') == 0

def test_starting_with_h():
    assert value('hi there!') == 20
    assert value('How are you?') == 20

def test_other_cases():
    assert value("What's up?") == 100
    assert value("good morning!") == 100

if __name__ == "__main__":
    main()