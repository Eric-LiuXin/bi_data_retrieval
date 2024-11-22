import json

import azure.functions as func
from azure.functions.decorators.http import HttpMethod

from bi_requests import BI_REQUESTS

app = func.FunctionApp()


@app.route(
    route="data_retrieval",
    auth_level=func.AuthLevel.ANONYMOUS,
    methods=[
        HttpMethod.POST,
    ],
)
def data_retrieval(req: func.HttpRequest) -> func.HttpResponse:
    res = True
    msg = ""
    data = {}

    try:
        post_data = req.get_json()

        request_id = post_data.get("_id", None)
        if not request_id:
            raise ValueError(f"Request parameter error, [_id] is required.")

        BIRequest = BI_REQUESTS.get(request_id, None)
        if not BIRequest:
            raise ValueError(f"Not Supported request ID [{request_id}].")

        query_dict = post_data.get("query", {})

        _request = BIRequest(query_dict)

        data = _request.run()
    except Exception as e:
        res = False
        msg = str(e)

    return func.HttpResponse(json.dumps({"success": res, "msg": msg, "data": data}))
