import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executed first")
    yield
    print("I will be executed last")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return["Praveena","Vaishnavi","vaishu2503@gmail.com"]


@pytest.fixture(params=[("chrome","vaishu"),("firefox","suresh"),("IE","amrithu")])
def crossBrowser(request):
    return request.param
