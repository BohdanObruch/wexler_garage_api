from __future__ import annotations

from http import HTTPStatus
from typing import Any, Type

import allure

from garage_api.assertions import assert_status_code, validate_json_schema


def assert_list_response(
    response: Any,
    schema_cls: Type[Any],
    params: dict[str, int] | None = None,
) -> Any:
    with allure.step("Parse list response"):
        response_data = schema_cls.model_validate_json(response.text)

    assert_status_code(response.status_code, HTTPStatus.OK)
    with allure.step("Check list count and size"):
        assert response_data.count >= len(response_data.results)
    if params and "limit" in params:
        with allure.step(f"Check list size within limit {params['limit']}"):
            assert len(response_data.results) <= params["limit"]

    validate_json_schema(response.json(), response_data.model_json_schema())
    return response_data
