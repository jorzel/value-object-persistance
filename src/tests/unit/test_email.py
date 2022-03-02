import pytest

from value_objects.email import Email, InvalidEmail


def test_email_initialization_succeed_when_value_is_valid():
    email = Email(" M.x@test.pl")

    assert email.address == "m.x@test.pl"
    assert email.domain == "test.pl"


def test_email_initialization_raise_error_when_value_is_not_valid():
    with pytest.raises(InvalidEmail):
        _ = Email(" M.xtest.pl")
