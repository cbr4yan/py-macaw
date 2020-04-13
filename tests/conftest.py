import pytest

from macaw import Macaw


@pytest.fixture
def app():
    app = Macaw("macaw_test")
    return app
