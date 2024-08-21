import pytest

from project import Tiger, Panda, Koala, User, is_valid_input, check_animals, pat_animals

def test_is_valid_input():
    assert is_valid_input("adopt") == False
    assert is_valid_input("adopt panda") == True
    assert is_valid_input("adopt python") == False

    assert is_valid_input("release") == False
    assert is_valid_input("release panda") == True
    assert is_valid_input("release python") == False


def test_check_animals():
    user = User()

    assert check_animals(user) == "0 animal(s) currently in zoo"

    user.adopt(Panda)
    user.adopt(Panda)

    assert check_animals(user) == "2 animal(s) currently in zoo"


def test_pat_animals():
    user = User()

    assert pat_animals(user) == "Zoo is empty! 😿"

    user.adopt(Panda)
    user.adopt(Panda)
    user.adopt(Tiger)
    user.adopt(Koala)

    assert pat_animals(user) == "💖💖💖💖"


def test_user_init():
    assert User().capacity == 10

    with pytest.raises(ValueError):
        User(-2)


def test_user_adopt():
    user = User()

    user.adopt(Tiger)
    user.adopt(Panda)
    user.adopt(Koala)

    assert user.total_acquisition_count == 3


def test_user_adopt_error():
    user = User()

    with pytest.raises(NameError):
        user.adopt(Python)


def test_user_release():
    user = User()

    user.adopt(Tiger)
    user.adopt(Panda)
    user.adopt(Koala)

    user.release(Tiger)

    assert user.animals.get(Tiger) == []
    assert user.total_acquisition_count == 2


def test_user_release_limit():
    user = User()

    user.release(Tiger)

    assert user.total_acquisition_count == 0
