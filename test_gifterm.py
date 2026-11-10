"""Tests for gifterm character set switching."""

import gifterm


def _blank_state():
    """An AppState without running __init__ (which sleeps and probes tty)."""
    state = gifterm.AppState.__new__(gifterm.AppState)
    state.charSets = {
        0: (("M", " ", "x"), 10),
        2: (("A", "B", "C"), 3),
    }
    state.chars = tuple("x M")
    state.setNum = 0
    return state


def test_set_charset_installs_new_charset():
    """setCharSet must install the newly selected set (reversed)."""
    state = _blank_state()
    gifterm.AppState.setCharSet(state, 2)
    assert tuple(state.chars) == ("C", "B", "A")
    assert state.delta == 3
    assert state.setNum == 2


def test_set_charset_twice_is_stable():
    """Selecting another set afterwards must not depend on previous chars."""
    state = _blank_state()
    gifterm.AppState.setCharSet(state, 2)
    gifterm.AppState.setCharSet(state, 0)
    assert tuple(state.chars) == ("x", " ", "M")
    assert state.delta == 10
