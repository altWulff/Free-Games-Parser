"""
Tests response data
"""

import pytest
import requests

from app.config import URL


def get_json(url):
    """Request json from URl"""
    request = requests.get(url)
    data = request.json()
    return data


def test_is_dict():
    """Test, is dict"""
    data = get_json(URL)
    assert isinstance(data, dict)


@pytest.mark.xfail
def test_is_list():
    """Expected fail, if data is list"""
    data = get_json(URL)
    assert isinstance(data, list)


def test_has_key():
    """Test has contains key"""
    data = get_json(URL)
    assert "data" in data


def test_data_length():
    """Test length data"""
    data = get_json(URL)
    assert len(data) > 1
