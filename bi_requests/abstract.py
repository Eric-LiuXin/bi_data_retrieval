"""Request abstract Class"""

import json

import requests

from config.config import Config


class RequestAbstract:
    DAX_QUERY_STR = ""

    def __init__(self, query_options: dict):
        self._dax_query_options = query_options

        self.__bi_query_url = Config.get_options("PowerBI", "query_url")
        self.__bi_query_type = Config.get_options("PowerBI", "query_type")
        self.__bi_include_nulls = Config.get_options("PowerBI", "include_nulls")

        self._bi_query_header = {
            "Content-Type": "application/json",
        }

        self._dax_request_body = {
            "queries": [],
            "serializerSettings": {"includeNulls": self.__bi_include_nulls},
        }

        self._response_content = None
        self.beautify_result = None

        self._at_request_before = [self.prepare]
        self._at_request_after = [self.beautify]

    def prepare(self) -> None:
        # Subclass can be rewritten
        ...

    def run(self) -> dict:
        for _func in self._at_request_before:
            _func()

        self._dax_request_body["queries"].append(
            {
                "query": self.DAX_QUERY_STR.format(**self._dax_query_options),
                "queryType": self.__bi_query_type,
            }
        )

        # TODO (Eric): request API
        # response = requests.post(
        #     self.__bi_query_url,
        #     headers=self.__bi_query_header,
        #     json=json.dumps(self._dax_request_body),
        # )
        #
        # response.raise_for_status()
        #
        # self.__response_content = response.content
        self._response_content = {"dummy": "dummy"}

        for _func in self._at_request_after:
            _func()

        return self.beautify_result

    def beautify(self) -> None:
        # Subclass can be rewritten
        # Exchange self._response_content to self.beautify_result
        self.beautify_result = self._response_content
