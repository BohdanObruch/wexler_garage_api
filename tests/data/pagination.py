from __future__ import annotations

import pytest

PAGINATION_PARAMS = [
    pytest.param(None, id="no_params"),
    pytest.param({"limit": 1}, id="limit_1"),
    pytest.param({"limit": 1, "offset": 1}, id="limit_1_offset_1"),
]
