from project import get_rounds, get_Qs, get_wager

def test_get_rounds(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "1")
    assert get_rounds() == 1
    
def test_get_Qs(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2")
    assert get_Qs() == 2

def test_get_wager(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "400")
    assert get_wager(400) == 400
