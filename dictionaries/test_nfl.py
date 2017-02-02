"""
Test for NFL PyTest

"""
import pytest
import dictionaries.nfl


league = {'foo': {'bar': ['baz']}}


def test_get_conference_and_division_by_team_name():
    query = 'baz'
    result = dictionaries.nfl.get_conference_and_division_by_team_name(league, query)
    assert result == ('foo', 'bar')


def test_teams_by_conference_and_division():
    query = 'foo'
    query2 = 'bar'
    result = dictionaries.nfl.get_teams_by_conference_and_division(league, query, query2)
    assert result == ['baz']


def test_run_program():
    result = dictionaries.nfl.run_program(league)
    assert result == ('foo', 'bar', 'baz')


