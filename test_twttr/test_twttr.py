from twttr import shorten
def main():
    test_uper_lower_case()
    test_numbers()
    test_punctuation()

# test capital letter
def test_upper_lower_case():
    assert shorten("twitter") == "twttr"
    assert shorten('TWITTER') == 'TWTTR'
    assert shorten('TwItTeR') == "TwtTR"
def test_numbers():
    assert shorten('1234') == '1234'
def test_punctuation():
    assert shorten('*@#$,') == '*@#$,'
if __name__ == "__main__":
    main()