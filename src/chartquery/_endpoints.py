"""Generated from the ChartQuery OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from .models import EndpointDefinition

ENDPOINTS: dict[str, EndpointDefinition] = {
    "barcode": EndpointDefinition(
        path="/v1/barcode",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("data",),
    ),
    "chart": EndpointDefinition(
        path="/v1/chart",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("query",),
    ),
    "chart_ai": EndpointDefinition(
        path="/v1/chart/ai",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("prompt",),
    ),
    "chart_render": EndpointDefinition(
        path="/v1/chart/render/{id}",
        methods=("GET",),
        response="any",
        required=("id",),
    ),
    "chart_view": EndpointDefinition(
        path="/v1/chart/view/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "diagram": EndpointDefinition(
        path="/v1/diagram",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=(
            "type",
            "query",
        ),
    ),
    "diagram_ai": EndpointDefinition(
        path="/v1/diagram/ai",
        methods=(
            "GET",
            "POST",
        ),
        response="json",
        required=("prompt",),
    ),
    "diagram_render": EndpointDefinition(
        path="/v1/diagram/render/{id}",
        methods=("GET",),
        response="any",
        required=("id",),
    ),
    "diagram_view": EndpointDefinition(
        path="/v1/diagram/view/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "jobs": EndpointDefinition(
        path="/v1/jobs/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "label": EndpointDefinition(
        path="/v1/label",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("query",),
    ),
    "label_compile": EndpointDefinition(
        path="/v1/label/compile",
        methods=("POST",),
        response="json",
        required=(
            "width",
            "elements",
            "language",
        ),
    ),
    "label_convert": EndpointDefinition(
        path="/v1/label/convert",
        methods=("POST",),
        response="json",
        required=(
            "source",
            "from",
            "to",
        ),
    ),
    "label_parse": EndpointDefinition(
        path="/v1/label/parse",
        methods=("POST",),
        response="json",
        required=(
            "source",
            "language",
        ),
    ),
    "label_render": EndpointDefinition(
        path="/v1/label/render/{id}",
        methods=("GET",),
        response="any",
        required=("id",),
    ),
    "label_validate": EndpointDefinition(
        path="/v1/label/validate",
        methods=("POST",),
        response="json",
        required=(
            "source",
            "language",
        ),
    ),
    "label_view": EndpointDefinition(
        path="/v1/label/view/{id}",
        methods=("GET",),
        response="json",
        required=("id",),
    ),
    "qrcode": EndpointDefinition(
        path="/v1/qrcode",
        methods=(
            "GET",
            "POST",
        ),
        response="any",
        required=("data",),
    ),
    "stats": EndpointDefinition(
        path="/v1/stats",
        methods=("GET",),
        response="json",
        required=(),
    ),
    "usage": EndpointDefinition(
        path="/v1/usage",
        methods=("GET",),
        response="json",
        required=(),
    ),
}
