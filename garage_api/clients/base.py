from __future__ import annotations

from typing import Any, Mapping

from requests import Response

from garage_api.utils.sessions import garage, garage_authorization


class BaseClient:
    def __init__(self, token: str | None = None, auth: bool = False) -> None:
        self._session = garage_authorization() if auth else garage()
        self._default_headers: dict[str, str] = {}
        if token:
            self._default_headers["Authorization"] = f"Bearer {token}"

    def _request(self, method: str, url: str, **kwargs: Any) -> Response:
        headers: Mapping[str, str] = kwargs.pop("headers", {})
        merged_headers = {**self._default_headers, **dict(headers)}
        return self._session.request(method, url, headers=merged_headers, **kwargs)
