import pytest


def test_get_session(mocker):
    from example import database

    mocker.patch.object(database, "SessionLocal", None)

    with pytest.raises(ImportError):
        next(database.get_session())

    SessionLocal = mocker.patch.object(database, "SessionLocal")
    session_generator = database.get_session()
    session = next(session_generator)

    assert session == SessionLocal.return_value
    session.close.assert_not_called()

    with pytest.raises(StopIteration):
        next(session_generator)
    session.close.assert_called_once()
