#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
import pytest
@pytest.mark.smoke
def test_firstProgram():
    msg="hello"
    assert msg == "hi"   "Test failed due to mismatch of strings"
@pytest.mark.skip
def test_secondcreditcard():
    a=6
    b=4
    assert b+2==6,   "ADDITION DOES NOT MATCH"
