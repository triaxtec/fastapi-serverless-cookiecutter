from starlette.status import HTTP_200_OK

_MODULE = "example.routers.default"


def test__get_changelog_html():
    from example.routers.default import _get_changelog_html

    assert _get_changelog_html().startswith("<h1>Changelog</h1>")


def test_changelog(client, mocker):
    mocker.patch(f"{_MODULE}._get_changelog_html", return_value="Change_Log_content")

    response = client.get("/changelog")

    assert response.status_code == HTTP_200_OK
    assert response.content == b"Change_Log_content"
