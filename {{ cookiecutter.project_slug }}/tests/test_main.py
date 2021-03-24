def test_{{ cookiecutter.code_entry_point }}(client):
    resp = client.post("/")
    assert resp.status_code == 200
    assert resp.data == b"ok"
