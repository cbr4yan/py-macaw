def test_app_name(app):
    name = app.name
    want = "macaw_test"

    assert name == want


def test_app_start(app):
    app.start()
    assert app.is_running


def test_app_stop(app):
    app.stop()
    assert not app.is_running
