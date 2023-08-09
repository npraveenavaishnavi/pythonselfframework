#fixtures are used to setup method to execute before actual test case written
#as pre-request @pytest.fixture is used
#as post-request yield is used
#fixtures are used to setup and tear down the methods for test cases
#conftest.py file is created and generalize the fixtures and used by all the test cases

import pytest
@pytest.mark.usefixtures("setup")
class TestExample:


   def test_fixtureDemo(self):
    print("I will execute the steps in fixturedemo later")
   def test_fixtureDemo1(self):
    print("I will execute the steps in fixturedemo1 later")
   def test_fixtureDemo2(self):
    print("I will execute the steps in fixturedemo2 later")
   def test_fixtureDemo3(self):
    print("I will execute the steps in fixturedemo3 later")