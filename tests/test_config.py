import pytest

from macaw import Macaw


class ConfigTest:
    TEST_KEY = "foo"


def test_config_from_object(app):
    class Config:
        TEST_KEY = "foo"


    app.config.from_object(ConfigTest)

    assert app.config["TEST_KEY"] == "foo"


def test_config_from_object_string(app):

    app.config.from_object("test_config.ConfigTest")

    assert app.config["TEST_KEY"] == "foo"


def test_config_from_object_string_exception(app):
    with pytest.raises(ImportError):
        app.config.from_object("test_config.Config.Test")
