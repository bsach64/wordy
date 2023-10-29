from wordle import check_word


def main():
    test_check_word()


def test_check_word():
    status = [0, 0, 0, 0, 0]
    assert check_word("melee", status, "eerie") == 5
    assert status == [0, 2, 0, 1, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("speed", status, "erase") == 3
    assert status == [1, 0, 1, 1, 0]
    status = [0, 0, 0, 0, 0]
    assert check_word("eerie", status, "erase") == 5
    assert status == [2, 0, 1, 0, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("melee", status, "eerie") == 5
    assert status == [0, 2, 0, 1, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("weary", status, "weary") == 10
    assert status == [2, 2, 2, 2, 2]
    status = [0, 0, 0, 0, 0]
    assert check_word("vague", status, "pills") == 0
    assert status == [0, 0, 0, 0, 0]


if __name__ == "__main__":
    main()
