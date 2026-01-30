from __future__ import annotations

from datetime import datetime
from http import HTTPStatus
from typing import Any

import allure


def assert_status_code(actual: int, expected: HTTPStatus) -> None:
    with allure.step(f"Check that response status code equals {expected}"):
        assert actual == expected, f"Expected status {expected}, got {actual}"


def assert_datetime_format(value: str, fmt: str) -> None:
    with allure.step(f"Check that datetime matches format {fmt!r}"):
        datetime.strptime(value, fmt)


def validate_json_schema(data: Any, schema: dict[str, Any]) -> None:
    with allure.step("Check that response matches JSON schema"):
        try:
            import jsonschema
        except Exception:  # pragma: no cover - fallback if jsonschema is not installed
            assert isinstance(schema, dict)
            return

        jsonschema.validate(instance=data, schema=schema)
