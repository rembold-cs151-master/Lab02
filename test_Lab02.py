"""
Testing script for Lab 02

You don't need to do anything with this script,
but you are welcome to look it over!
"""

import pytest
import Lab02

def is_within_percent(submitted_value, real_value, percent):
    plus_minus = real_value * percent/100
    return (real_value - plus_minus) < submitted_value < (real_value + plus_minus)


def test_no_movement():
    value = Lab02.moving_time(0)
    assert is_within_percent(value, 21.6, 0.01)

def test_10_percent():
    value = Lab02.moving_time(0.1 * 3E8)
    assert is_within_percent(value, 21.818182, 0.01)

def test_50_percent():
    value = Lab02.moving_time(0.5 * 3E8)
    assert is_within_percent(value, 28.8, 0.01)

def test_95_percent():
    value = Lab02.moving_time(0.95 * 3E8)
    assert is_within_percent(value, 221.538, 0.01)

def test_99_percent():
    value = Lab02.moving_time(0.99 * 3E8)
    assert is_within_percent(value, 1085.427, 0.01)
