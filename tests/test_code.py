from src.utils import do_something_useful
from src.validator import check_validity

def test_utils():
    assert do_something_useful() == "Hello Hackathon"

def test_validator():
    # This will fail to run because validator.py has a syntax error
    assert check_validity(True) == True
