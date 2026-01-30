from __future__ import annotations

import pytest


INVALID_PAGINATION_PARAMS = [
    pytest.param({"limit": "one"}, id="limit_string"),
    pytest.param({"offset": "one"}, id="offset_string"),
    pytest.param({"limit": -1}, id="limit_negative"),
    pytest.param({"offset": -1}, id="offset_negative"),
]

EDGE_PAGINATION_PARAMS = [
    pytest.param({"limit": 0}, id="limit_0"),
    pytest.param({"offset": 0}, id="offset_0"),
    pytest.param({"limit": 1000}, id="limit_1000"),
    pytest.param({"limit": 50, "offset": 1000}, id="limit_50_offset_1000"),
]
