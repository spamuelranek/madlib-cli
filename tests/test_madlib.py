import pytest
from madlib_cli.madlib import read_template, parse_template, merge


def test_read_template_returns_stripped_string():
    actual = read_template("assets/dark_and_stormy_night_template.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected

def test_read_template_returns_stripped_string_of_my_own():
    actual = read_template("assets/a_wild_ride_to_the_back.txt")
    expected = """
  While I {past tense verb} to the {noun} something happened.
  There is a {singular noun} in the {noun}. It {past tense verb} a {noun}.
  That {same noun as previous} {verb ending in ed} though the {noun}.
  There was no {verb ending in ing} it.
  """
    assert actual == expected

def test_parse_template_of_my_own():
    actual_stripped, actual_parts = parse_template("""
  While I {past tense verb} to the {noun} something happened.
  There is a {singular noun} in the {noun}. It {past tense verb} a {noun}.
  That {same noun as previous} {verb ending in ed} though the {noun}.
  There was no {verb ending in ing} it.
  """)
    expected_stripped = '\n  While I {} to the {} something happened.\n  There is a {} in the {}. It {} a {}.\n  That {} {} though the {}.\n  There was no {} it.\n  '
    expected_parts = ('past tense verb', 'noun', 'singular noun', 'noun', 'past tense verb', 'noun', 'same noun as previous', 'verb ending in ed', 'noun', 'verb ending in ing')

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts


def test_parse_template():
    actual_stripped, actual_parts = parse_template(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts



def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected



def test_read_template_raises_exception_with_bad_path():

    with pytest.raises(FileNotFoundError):
        path = "missing.txt"
        read_template(path)
