"""
Testing script for Lab 02

You don't need to do anything with this script,
but you are welcome to look it over!
"""

import pytest
import Lab02


def test_no_movement():
    assert Lab02.moving_time(0) == 21.6
