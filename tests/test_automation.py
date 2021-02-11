import pytest
from emails import *


def test_valid_email():
    valid_email('./assets/potential-contacts.txt')
    with open('./assets/email-extracted.txt') as e_file:
        lines = e_file.readlines()
    assert len(lines) == 101
