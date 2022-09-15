import fire
from fluentcli.greet import greet

def test_greet_cli(capsys):
    fire.Fire(greet, ["Egypt"])
    captured = capsys.readouterr()
    result = captured.out
    assert "Hello, Egypt!" in result