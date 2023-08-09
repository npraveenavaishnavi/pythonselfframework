#Any pytest file should start with test_ or end with _test
#pytest method names should start with test
#Any code should be wrapped in method only
#method name should be valid/sense
#-k stands for specific method execution from different file, -s for logs in output, -v stands for more info
# you can run specific file using the command py.test<filename>
#if you have to do smoke or regression testing then use the (tag) @pytest.mark.smoke and run the test case with
#-m
# if you have to skip a particular test case then the syntax is @pytest.mark.skip
#@pytest.mark.xfail is used to run the test case but do not want to see the status
# datadriven and parameterization can be done with return statement in tuple format.
# when you define fixture scope to class only,it will run once before class is initiated and at the end.
import pytest


def test_firstProgram():
    print("HELLO")

@pytest.mark.smoke
def test_secondcreditcardGreet():
    print("Good Morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])