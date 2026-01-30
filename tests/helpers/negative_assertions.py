from __future__ import annotations

from http import HTTPStatus
from typing import Iterable


def assert_client_error(
    response: object,
    allowed_statuses: Iterable[int] | None = None,
) -> None:
    if allowed_statuses is None:
        allowed_statuses = {
            HTTPStatus.BAD_REQUEST,
            HTTPStatus.UNPROCESSABLE_ENTITY,
        }
    status_code = getattr(response, "status_code", None)
    assert status_code in set(int(s) for s in allowed_statuses)


def assert_not_found_or_error(response: object) -> None:
    allowed = {
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNPROCESSABLE_ENTITY,
        HTTPStatus.NOT_FOUND,
    }
    status_code = getattr(response, "status_code", None)
    assert status_code in set(int(s) for s in allowed)


def assert_not_server_error(response: object) -> None:
    status_code = getattr(response, "status_code", None)
    assert status_code is not None
    assert int(status_code) < 500


def assert_client_or_server_error(response: object) -> None:
    allowed = {
        HTTPStatus.BAD_REQUEST,
        HTTPStatus.UNPROCESSABLE_ENTITY,
        HTTPStatus.INTERNAL_SERVER_ERROR,
    }
    status_code = getattr(response, "status_code", None)
    assert status_code in set(int(s) for s in allowed)
