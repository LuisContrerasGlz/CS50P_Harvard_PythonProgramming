from numb3rs import validate

def main():
    test_format()
    test_range()

def test_format():
    assert validate(r'127.0') == False
    assert validate(r'127.0.1') == False
    assert validate(r'127.0.1.2') == True

def test_range():
    assert validate(r'255.255.255.255') == True
    assert validate(r'712.1.1.1') == False
    assert validate(r'1.822.1.1') == False


if __name__ == "__main__":
    main()