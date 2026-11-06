"""Generated from the ChartQuery OpenAPI document. Do not edit by hand."""

from __future__ import annotations

from collections.abc import Mapping, Sequence
from typing import Any, Literal, cast

from .models import APIResponse, JsonResponse, RequestOptions


class _SyncOperations:
    """Generated ChartQuery endpoint methods."""

    __slots__ = ()

    def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    def barcode(
        self,
        *,
        data: str,
        type_: Literal[
            "code128",
            "code39",
            "code39ext",
            "code93",
            "code93ext",
            "ean13",
            "ean8",
            "ean5",
            "ean2",
            "upca",
            "upce",
            "itf",
            "itf14",
            "codabar",
            "msi",
            "pharmacode",
            "code11",
            "gs1-128",
            "gs1-databar",
            "gs1-databar-limited",
            "gs1-databar-expanded",
            "identcode",
            "leitcode",
            "postnet",
            "planet",
            "plessey",
        ]
        | str
        | None = None,
        height: int | float | None = None,
        color: str | None = None,
        show_text: bool | None = None,
        text_position: Literal["bottom", "top"] | str | None = None,
        text_align: Literal["center", "left", "right"] | str | None = None,
        font_size: int | float | None = None,
        font_family: str | None = None,
        bar_width: int | float | None = None,
        bar_gap: int | float | None = None,
        background: str | None = None,
        margin: int | float | None = None,
        margin_top: int | float | None = None,
        margin_bottom: int | float | None = None,
        margin_left: int | float | None = None,
        margin_right: int | float | None = None,
        rotation: int | float | None = None,
        bearer_bars: bool | None = None,
        unit: Literal["px", "mm", "in", "cm"] | str | None = None,
        aria_label: str | None = None,
        title: str | None = None,
        desc: str | None = None,
        format: Literal["svg", "png"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Barcode. Generate a barcode image via GET. Output: SVG (default) or PNG. Supports 25+ formats: EAN-13, Code 128, ITF-14, GS1-128, postal codes and more. Credit cost: 3 credits per call.

        ``GET / POST /v1/barcode``

        Args:
            data: The data to encode in the barcode. Examples by type:
            type_: Barcode format. Default: code128.
            height: Bar height in pixels. Default: 80. Typical values: 50 (compact), 80 (standard), 100–120 (tall labels). Example: ?height=100
            color: Bar color as a CSS color string. Default: #000. Examples: ?color=%231e293b (dark slate), ?color=%230f172a (near black), ?color=%237c3aed (purple), ?color=%23dc2626 (red). Use %23 to URL-encode the #…
            show_text: Show human-readable text below the bars. Example: ?show_text=true. Combine with font_size and text_align for print labels.
            text_position: Position of the human-readable text label. Default: bottom. Example: ?text_position=top
            text_align: Horizontal alignment of the text label. Default: center. Example: ?text_align=left
            font_size: Font size of the text label in pixels. Default: 14. Example: ?font_size=12
            font_family: Font family of the text label. Default: monospace. Examples: ?font_family=monospace, ?font_family=sans-serif, ?font_family=Arial
            bar_width: Width multiplier per module (bar). Default: 2. Increase for wider, more scannable barcodes. Example: ?bar_width=3
            bar_gap: Extra horizontal spacing between bars in pixels. Default: 0. Example: ?bar_gap=1
            background: Background fill color. Default: #fff. Use transparent for no background. Example: ?background=%23f8fafc
            margin: Uniform margin around the barcode in pixels. Default: 10. Overridden per side by margin_top/bottom/left/right. Example: ?margin=6
            margin_top: Top margin in pixels (overrides margin). Example: ?margin_top=4
            margin_bottom: Bottom margin in pixels (overrides margin). Example: ?margin_bottom=4
            margin_left: Left margin in pixels (overrides margin). Example: ?margin_left=8
            margin_right: Right margin in pixels (overrides margin). Example: ?margin_right=8
            rotation: Rotate the barcode by 0, 90, 180 or 270 degrees. Default: 0. Use 90 or 270 for vertical label orientation. Example: ?rotation=90
            bearer_bars: Add horizontal bearer bars above and below the barcode. Required for ITF-14. Default: false. Example: ?bearer_bars=true
            unit: Measurement unit for dimensions. Default: px. Use mm, in or cm for print-ready output. Example: ?unit=mm
            aria_label: Accessible label added as aria-label on the SVG element. Improves screen reader support. Example: ?aria_label=EAN-13+barcode+for+product+4006381333931
            title: SVG <title> element for tooltip and accessibility. Example: ?title=Product+Barcode
            desc: SVG <desc> element for extended accessibility description. Example: ?desc=EAN-13+encoding+GTIN+for+Nivea+cream+75ml
            format: Output format. Default: svg. Use png to get a raster image. SVG is lossless and scalable; PNG is pixel-based and suitable for email, PDF or messaging. Example: ?format=png
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "barcode",
            {
                "data": data,
                "type": type_,
                "height": height,
                "color": color,
                "show_text": show_text,
                "text_position": text_position,
                "text_align": text_align,
                "font_size": font_size,
                "font_family": font_family,
                "bar_width": bar_width,
                "bar_gap": bar_gap,
                "background": background,
                "margin": margin,
                "margin_top": margin_top,
                "margin_bottom": margin_bottom,
                "margin_left": margin_left,
                "margin_right": margin_right,
                "rotation": rotation,
                "bearer_bars": bearer_bars,
                "unit": unit,
                "aria_label": aria_label,
                "title": title,
                "desc": desc,
                "format": format,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def chart(
        self,
        *,
        query: str,
        version: str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Chart. Render a Chart.js image via GET. Pass the full chart object as URL-encoded JSON in query. Prefer format png for ChatGPT. POST sends the same object as a JSON body, not query. Credit cost: 5 credits per call.

        ``GET / POST /v1/chart``

        Args:
            query: Full chart config as URL-encoded JSON. Pass ?version= or ?v= separately to pin the chart version.
            version: Chart.js version to use. Alias: ?v=. Only v4.x is supported. Defaults to the installed version (4.5.1). Example: "4", "4.5", "4.5.1". The installed version is always returned in the X-ChartJS-Version…
            share: If true, persist the result and return share URLs instead of an image. Leave false to get the image.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "chart",
            {
                "query": query,
                "version": version,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def chart_ai(
        self,
        *,
        prompt: str,
        raw_data: str | None = None,
        title: str | None = None,
        subtitle: str | None = None,
        legend: Literal["top", "bottom", "left", "right", "chartArea", "false"] | str | None = None,
        format: Literal["png", "svg"] | str | None = None,
        width: int | float | None = None,
        height: int | float | None = None,
        background: str | None = None,
        device_pixel_ratio: int | float | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Chart AI. Describe a chart in plain English via GET and get a rendered image back. Powered by AI. Credit cost: 10 credits per call.

        ``GET / POST /v1/chart/ai``

        Args:
            prompt: Describe your chart in plain English (max 1000 chars). Be specific: mention chart type, data topic, colors, style.
            raw_data: Raw data for the chart. URL-encoded string, CSV, or JSON. AI will parse and structure it.
            title: Override the chart title generated by AI.
            subtitle: Override the chart subtitle.
            legend: Legend position or visibility. Use "false" to hide.
            format: Output format. Default: "png".
            width: Image width in pixels (50–4000). Default: 1200.
            height: Image height in pixels (50–4000). Default: 600.
            background: Background color as a hex value. Default: #ffffff.
            device_pixel_ratio: Device pixel ratio for the rendered image. Default: 1.
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "chart_ai",
                {
                    "prompt": prompt,
                    "raw_data": raw_data,
                    "title": title,
                    "subtitle": subtitle,
                    "legend": legend,
                    "format": format,
                    "width": width,
                    "height": height,
                    "background": background,
                    "device_pixel_ratio": device_pixel_ratio,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def chart_render(
        self,
        *,
        id: str,
        title: str | None = None,
        labels: str | None = None,
        data1: str | None = None,
        width: str | None = None,
        height: str | None = None,
        format: Literal["png", "svg"] | str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Chart Render. Render a previously saved chart by ID. Public, no API key required. Supports URL overrides for templates (?data1=, ?labels=, ?title=…).

        ``GET /v1/chart/render/{id}``

        Args:
            id: The chart ID returned in the X-Chart-Render-URL header when saving a chart. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            title: Override the chart title.
            labels: Override X-axis labels. Comma-separated.
            data1: Override first dataset values. Comma-separated numbers. Use data2, data3… for additional datasets.
            width: Override output width in pixels (50–4000).
            height: Override output height in pixels (50–4000).
            format: Override output format.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "chart_render",
            {
                "id": id,
                "title": title,
                "labels": labels,
                "data1": data1,
                "width": width,
                "height": height,
                "format": format,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def chart_view(
        self,
        *,
        id: str,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Chart View. View a previously saved chart as an interactive HTML page. Public, no API key required. Iframe-embeddable.

        ``GET /v1/chart/view/{id}``

        Args:
            id: The chart ID returned in the X-Chart-View-URL header when saving a chart. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "chart_view",
                {
                    "id": id,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def diagram(
        self,
        *,
        type_: Literal[
            "mermaid",
            "graphviz",
            "plantuml",
            "d2",
            "svgbob",
            "nomnoml",
            "blockdiag",
            "seqdiag",
            "actdiag",
            "nwdiag",
            "bpmn",
            "erd",
            "excalidraw",
            "ditaa",
            "vega",
            "vegalite",
            "wavedrom",
            "wireviz",
            "c4plantuml",
            "structurizr",
            "tikz",
            "pikchr",
            "umlet",
            "symbolator",
            "packetdiag",
            "rackdiag",
            "bytefield",
            "dbml",
        ]
        | str,
        query: str,
        format: Literal["svg", "png", "jpeg", "pdf"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Diagram. Render a diagram via GET. Use type (mermaid, d2, …), query (source code), and format=png for ChatGPT. POST uses diagram_type and diagram_source instead. Credit cost: 5 credits per call.

        ``GET / POST /v1/diagram``

        Args:
            type_: Diagram language.
            query: Diagram source code (URL-encoded).
            format: Use png so ChatGPT can display the image. svg is for download or infinite scale.
            share: If true, persist the result and return share URLs instead of an image. Leave false to get the image.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "diagram",
            {
                "type": type_,
                "query": query,
                "format": format,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def diagram_ai(
        self,
        *,
        prompt: str,
        diagram_type: Literal["mermaid", "d2", "plantuml", "graphviz"] | str | None = None,
        output_format: Literal["svg", "png", "jpeg", "pdf"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Diagram AI. Describe a diagram in plain English via GET and get a rendered image back. Powered by AI. Credit cost: 10 credits per call.

        ``GET / POST /v1/diagram/ai``

        Args:
            prompt: Describe your diagram in plain English (max 1000 chars). Be specific: mention the diagram type, key entities, and relationships.
            diagram_type: Preferred diagram language. AI chooses if omitted. Examples: "mermaid", "d2", "plantuml", "graphviz".
            output_format: Output format. Default: "svg".
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry. Paid plan: 6-month expiry.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "diagram_ai",
                {
                    "prompt": prompt,
                    "diagram_type": diagram_type,
                    "output_format": output_format,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def diagram_render(
        self,
        *,
        id: str,
        format: Literal["svg", "png", "jpeg", "pdf"] | str | None = None,
        query: str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Diagram Render. Render a previously saved diagram by ID. Public, no API key required. Supports ?format= and ?query= overrides.

        ``GET /v1/diagram/render/{id}``

        Args:
            id: The diagram ID returned in the X-Diagram-Render-URL header when saving a diagram. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            format: Override output format.
            query: Override the diagram source code (URL-encoded).
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "diagram_render",
            {
                "id": id,
                "format": format,
                "query": query,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def diagram_view(
        self,
        *,
        id: str,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Diagram View. View a previously saved diagram as an HTML page. Public, no API key required. Iframe-embeddable with inline SVG rendering.

        ``GET /v1/diagram/view/{id}``

        Args:
            id: The diagram ID returned in the X-Diagram-View-URL header when saving a diagram. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "diagram_view",
                {
                    "id": id,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, self._call("jobs", {"id": id}, request_options))

    def label(
        self,
        *,
        query: str,
        format: Literal["svg", "png"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Label Preview. Preview a thermal label via GET. Pass the same label object as a URL-encoded JSON string in query. Inside that JSON, text items use content and size (1-10), not text or fontSize. Prefer format=png for ChatGPT. Credit cost: 3 credits per call.

        ``GET / POST /v1/label``

        Args:
            format: Use png so ChatGPT can display the image. svg is for download or infinite scale.
            share: If true, persist the result and return share URLs instead of an image. Leave false to get the image.
            query: Full label config as URL-encoded JSON. Must include width and elements. Text items use content and size (1-10), not text or fontSize.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "label",
            {
                "format": format,
                "share": share,
                "query": query,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def label_compile(
        self,
        *,
        width: int | float,
        elements: Sequence[Mapping[str, Any]],
        language: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "escpos", "starprnt", "ipl"]
        | str,
        height: int | float | None = None,
        unit: Literal["mm", "inch", "dot"] | str | None = None,
        dpi: int | float | None = None,
        gap: int | float | None = None,
        speed: int | float | None = None,
        density: int | float | None = None,
        direction: int | float | None = None,
        copies: int | float | None = None,
        printer: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Compile. Compile a label to printer commands (tsc, zpl, epl, …). POST width, language, and elements. Text uses content and size (1-10), not text or fontSize. No barcode element. Example: {"width":40,"height":30,"unit":"mm","language":"zpl","element… Credit cost: 3 credits per call.

        ``POST /v1/label/compile``

        Args:
            width: Label width. Required. Default unit is mm. Example: 40. Do not send query instead of width.
            height: Label height in the same unit. Example: 30. Omit for receipt / continuous mode.
            unit: Measurement unit for width and height. Default mm. Use mm unless you are working in printer dots.
            dpi: Printer DPI. Default 203.
            gap: Gap between labels in mm. Ignored for receipts.
            speed: Print speed, 1-18.
            density: Print darkness, 0-15.
            direction: Print direction. 0 = normal, 1 = reversed.
            copies: Number of copies. Minimum 1.
            printer: Printer profile id (tsc-te210, zebra-zd420, …).
            elements: Required array. Text items need type=text, content, and size (1-10 magnification). Do not use text, fontSize, or type=barcode. Positions x/y are in dots. Example item: {"type":"text","content":"Order…
            language: Required printer language. Example: zpl or tsc. Do not omit.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "label_compile",
                {
                    "width": width,
                    "height": height,
                    "unit": unit,
                    "dpi": dpi,
                    "gap": gap,
                    "speed": speed,
                    "density": density,
                    "direction": direction,
                    "copies": copies,
                    "printer": printer,
                    "elements": elements,
                    "language": language,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def label_convert(
        self,
        *,
        source: str,
        from_: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "ipl"] | str,
        to: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "escpos", "starprnt", "ipl"] | str,
        dpi: int | float | None = None,
        speed: int | float | None = None,
        density: int | float | None = None,
        copies: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Convert. Convert printer commands from one language to another. POST source, from, and to. from is the source language (tsc, zpl, epl, …). to is the target (tsc, zpl, escpos, …). Credit cost: 5 credits per call.

        ``POST /v1/label/convert``

        Args:
            source: Raw printer commands to convert. Also send from and to.
            from_: Source language.
            to: Target language.
            dpi: Override DPI on the converted output.
            speed: Override print speed, 1-18.
            density: Override print darkness, 0-15.
            copies: Override copies. Minimum 1.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "label_convert",
                {
                    "source": source,
                    "from": from_,
                    "to": to,
                    "dpi": dpi,
                    "speed": speed,
                    "density": density,
                    "copies": copies,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def label_parse(
        self,
        *,
        source: str,
        language: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "ipl"] | str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Parse. Parse printer commands into structured elements. POST source and language (tsc, zpl, epl, …). Credit cost: 1 credit per call.

        ``POST /v1/label/parse``

        Args:
            source: Raw printer commands to parse. Also send language.
            language: Language of the source commands. Example: tsc or zpl.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "label_parse",
                {
                    "source": source,
                    "language": language,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def label_render(
        self,
        *,
        id: str,
        format: Literal["svg", "png"] | str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Label Render. Render a previously saved label by ID. Public, no API key required. Supports ?format= override.

        ``GET /v1/label/render/{id}``

        Args:
            id: id
            format: Override output format.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "label_render",
            {
                "id": id,
                "format": format,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def label_validate(
        self,
        *,
        source: str,
        language: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "ipl"] | str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Validate. Validate printer commands. POST source (the raw commands) and language (tsc, zpl, epl, …). Credit cost: 1 credit per call.

        ``POST /v1/label/validate``

        Args:
            source: Raw printer commands to validate. Also send language.
            language: Language of the source commands. Example: tsc or zpl.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "label_validate",
                {
                    "source": source,
                    "language": language,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    def label_view(
        self,
        *,
        id: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label View. View a previously saved label as an HTML page. Public, no API key required. Iframe-embeddable with inline SVG rendering.

        ``GET /v1/label/view/{id}``

        Args:
            id: id
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            self._call(
                "label_view",
                {"id": id, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    def qrcode(
        self,
        *,
        data: str,
        size: int | float | None = None,
        ec_level: Literal["L", "M", "Q", "H"] | str | None = None,
        dot_type: Literal[
            "square",
            "rounded",
            "dots",
            "diamond",
            "classy",
            "classy-rounded",
            "extra-rounded",
            "vertical-line",
            "horizontal-line",
            "small-square",
            "tiny-square",
        ]
        | str
        | None = None,
        color: str | None = None,
        shape: Literal["square", "circle"] | str | None = None,
        dot_size: int | float | None = None,
        background: str | None = None,
        margin: int | float | None = None,
        version: int | float | None = None,
        mode: Literal["auto", "numeric", "alphanumeric", "byte"] | str | None = None,
        mask: int | float | None = None,
        unit: Literal["px", "mm", "in", "cm"] | str | None = None,
        xml_declaration: bool | None = None,
        aria_label: str | None = None,
        title: str | None = None,
        desc: str | None = None,
        format: Literal["svg", "png"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """QR Code. Generate a styled QR code via GET. Output: SVG (default) or PNG. Supports dot styles, gradients, custom corners and all QR versions. Credit cost: 3 credits per call.

        ``GET / POST /v1/qrcode``

        Args:
            data: Data to encode in the QR code. Examples:
            size: Output size in pixels (width = height). Default: 200. Examples: ?size=200 (thumbnail), ?size=300 (standard), ?size=400 (large), ?size=600 (poster). For print, use the unit param with mm/cm instead.
            ec_level: Error correction level. Default: M. Higher levels allow more damage/obscuring before the code becomes unreadable.
            dot_type: Module (dot) shape. Default: square. Controls the visual style of each QR code module.
            color: Module color as CSS hex. Default: #000. Examples: ?color=%236366f1 (indigo), ?color=%23dc2626 (red), ?color=%23059669 (green), ?color=%230891b2 (teal). Use %23 to URL-encode #. For gradient objects,…
            shape: Overall QR code shape. Default: square. Use circle to clip the entire QR into a circle: great for profile/avatar-style codes. Example: ?shape=circle&dot_type=dots
            dot_size: Module size ratio between 0.1 and 1. Default: 1 (full). Values below 1 add spacing between modules for a lighter look. Example: ?dot_size=0.85
            background: Background color. Default: #fff. Set to transparent for no background. Example: ?background=%230f172a for dark background. Use %23 to encode #.
            margin: Quiet zone width in modules around the QR code. Default: 4. Minimum recommended by the QR standard: 4. Example: ?margin=2 (compact) or ?margin=6 (extra padding).
            version: QR version from 1 to 40 (determines grid size and data capacity). Leave unset for auto-selection based on data length and ec_level. Example: ?version=5
            mode: Encoding mode. Default: auto (best mode selected for the data). Use numeric for digits-only, alphanumeric for uppercase + digits, byte for arbitrary text/UTF-8. Example: ?mode=numeric
            mask: Mask pattern from 0 to 7. Default: auto (best mask selected to minimize visual patterns). Only set manually if you need a deterministic output. Example: ?mask=3
            unit: Measurement unit for the size param. Default: px. Use mm, in or cm with the size param for print-ready output. Example: ?size=50&unit=mm
            xml_declaration: Prepend an XML declaration (<?xml version="1.0" encoding="UTF-8"?>) to the SVG output. Useful when the SVG will be used as a standalone XML file. Default: false. Example: ?xml_declaration=true
            aria_label: Accessible label added as aria-label on the SVG element. Example: ?aria_label=QR+code+linking+to+chartquery.com
            title: SVG <title> element shown as a browser tooltip and used by screen readers. Example: ?title=ChartQuery+Website
            desc: SVG <desc> element for extended accessibility description. Example: ?desc=Scan+to+visit+https://chartquery.com
            format: Output format. Default: svg. Use png to get a raster image. SVG is lossless and scalable; PNG is pixel-based and suitable for email, PDF or messaging. Example: ?format=png
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return self._call(
            "qrcode",
            {
                "data": data,
                "size": size,
                "ec_level": ec_level,
                "dot_type": dot_type,
                "color": color,
                "shape": shape,
                "dot_size": dot_size,
                "background": background,
                "margin": margin,
                "version": version,
                "mode": mode,
                "mask": mask,
                "unit": unit,
                "xml_declaration": xml_declaration,
                "aria_label": aria_label,
                "title": title,
                "desc": desc,
                "format": format,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example chart. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/chart. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse, self._call("stats", {"engine": engine, "path": path}, request_options)
        )

    def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Return this account's Chartquery usage and credit balance. No body. Requires an API key.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, self._call("usage", {}, request_options))


class _AsyncOperations:
    """Generated ChartQuery endpoint methods."""

    __slots__ = ()

    async def _call(
        self, name: str, params: dict[str, Any], options: RequestOptions | None
    ) -> APIResponse:
        raise NotImplementedError

    async def barcode(
        self,
        *,
        data: str,
        type_: Literal[
            "code128",
            "code39",
            "code39ext",
            "code93",
            "code93ext",
            "ean13",
            "ean8",
            "ean5",
            "ean2",
            "upca",
            "upce",
            "itf",
            "itf14",
            "codabar",
            "msi",
            "pharmacode",
            "code11",
            "gs1-128",
            "gs1-databar",
            "gs1-databar-limited",
            "gs1-databar-expanded",
            "identcode",
            "leitcode",
            "postnet",
            "planet",
            "plessey",
        ]
        | str
        | None = None,
        height: int | float | None = None,
        color: str | None = None,
        show_text: bool | None = None,
        text_position: Literal["bottom", "top"] | str | None = None,
        text_align: Literal["center", "left", "right"] | str | None = None,
        font_size: int | float | None = None,
        font_family: str | None = None,
        bar_width: int | float | None = None,
        bar_gap: int | float | None = None,
        background: str | None = None,
        margin: int | float | None = None,
        margin_top: int | float | None = None,
        margin_bottom: int | float | None = None,
        margin_left: int | float | None = None,
        margin_right: int | float | None = None,
        rotation: int | float | None = None,
        bearer_bars: bool | None = None,
        unit: Literal["px", "mm", "in", "cm"] | str | None = None,
        aria_label: str | None = None,
        title: str | None = None,
        desc: str | None = None,
        format: Literal["svg", "png"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Barcode. Generate a barcode image via GET. Output: SVG (default) or PNG. Supports 25+ formats: EAN-13, Code 128, ITF-14, GS1-128, postal codes and more. Credit cost: 3 credits per call.

        ``GET / POST /v1/barcode``

        Args:
            data: The data to encode in the barcode. Examples by type:
            type_: Barcode format. Default: code128.
            height: Bar height in pixels. Default: 80. Typical values: 50 (compact), 80 (standard), 100–120 (tall labels). Example: ?height=100
            color: Bar color as a CSS color string. Default: #000. Examples: ?color=%231e293b (dark slate), ?color=%230f172a (near black), ?color=%237c3aed (purple), ?color=%23dc2626 (red). Use %23 to URL-encode the #…
            show_text: Show human-readable text below the bars. Example: ?show_text=true. Combine with font_size and text_align for print labels.
            text_position: Position of the human-readable text label. Default: bottom. Example: ?text_position=top
            text_align: Horizontal alignment of the text label. Default: center. Example: ?text_align=left
            font_size: Font size of the text label in pixels. Default: 14. Example: ?font_size=12
            font_family: Font family of the text label. Default: monospace. Examples: ?font_family=monospace, ?font_family=sans-serif, ?font_family=Arial
            bar_width: Width multiplier per module (bar). Default: 2. Increase for wider, more scannable barcodes. Example: ?bar_width=3
            bar_gap: Extra horizontal spacing between bars in pixels. Default: 0. Example: ?bar_gap=1
            background: Background fill color. Default: #fff. Use transparent for no background. Example: ?background=%23f8fafc
            margin: Uniform margin around the barcode in pixels. Default: 10. Overridden per side by margin_top/bottom/left/right. Example: ?margin=6
            margin_top: Top margin in pixels (overrides margin). Example: ?margin_top=4
            margin_bottom: Bottom margin in pixels (overrides margin). Example: ?margin_bottom=4
            margin_left: Left margin in pixels (overrides margin). Example: ?margin_left=8
            margin_right: Right margin in pixels (overrides margin). Example: ?margin_right=8
            rotation: Rotate the barcode by 0, 90, 180 or 270 degrees. Default: 0. Use 90 or 270 for vertical label orientation. Example: ?rotation=90
            bearer_bars: Add horizontal bearer bars above and below the barcode. Required for ITF-14. Default: false. Example: ?bearer_bars=true
            unit: Measurement unit for dimensions. Default: px. Use mm, in or cm for print-ready output. Example: ?unit=mm
            aria_label: Accessible label added as aria-label on the SVG element. Improves screen reader support. Example: ?aria_label=EAN-13+barcode+for+product+4006381333931
            title: SVG <title> element for tooltip and accessibility. Example: ?title=Product+Barcode
            desc: SVG <desc> element for extended accessibility description. Example: ?desc=EAN-13+encoding+GTIN+for+Nivea+cream+75ml
            format: Output format. Default: svg. Use png to get a raster image. SVG is lossless and scalable; PNG is pixel-based and suitable for email, PDF or messaging. Example: ?format=png
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "barcode",
            {
                "data": data,
                "type": type_,
                "height": height,
                "color": color,
                "show_text": show_text,
                "text_position": text_position,
                "text_align": text_align,
                "font_size": font_size,
                "font_family": font_family,
                "bar_width": bar_width,
                "bar_gap": bar_gap,
                "background": background,
                "margin": margin,
                "margin_top": margin_top,
                "margin_bottom": margin_bottom,
                "margin_left": margin_left,
                "margin_right": margin_right,
                "rotation": rotation,
                "bearer_bars": bearer_bars,
                "unit": unit,
                "aria_label": aria_label,
                "title": title,
                "desc": desc,
                "format": format,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def chart(
        self,
        *,
        query: str,
        version: str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Chart. Render a Chart.js image via GET. Pass the full chart object as URL-encoded JSON in query. Prefer format png for ChatGPT. POST sends the same object as a JSON body, not query. Credit cost: 5 credits per call.

        ``GET / POST /v1/chart``

        Args:
            query: Full chart config as URL-encoded JSON. Pass ?version= or ?v= separately to pin the chart version.
            version: Chart.js version to use. Alias: ?v=. Only v4.x is supported. Defaults to the installed version (4.5.1). Example: "4", "4.5", "4.5.1". The installed version is always returned in the X-ChartJS-Version…
            share: If true, persist the result and return share URLs instead of an image. Leave false to get the image.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "chart",
            {
                "query": query,
                "version": version,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def chart_ai(
        self,
        *,
        prompt: str,
        raw_data: str | None = None,
        title: str | None = None,
        subtitle: str | None = None,
        legend: Literal["top", "bottom", "left", "right", "chartArea", "false"] | str | None = None,
        format: Literal["png", "svg"] | str | None = None,
        width: int | float | None = None,
        height: int | float | None = None,
        background: str | None = None,
        device_pixel_ratio: int | float | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Chart AI. Describe a chart in plain English via GET and get a rendered image back. Powered by AI. Credit cost: 10 credits per call.

        ``GET / POST /v1/chart/ai``

        Args:
            prompt: Describe your chart in plain English (max 1000 chars). Be specific: mention chart type, data topic, colors, style.
            raw_data: Raw data for the chart. URL-encoded string, CSV, or JSON. AI will parse and structure it.
            title: Override the chart title generated by AI.
            subtitle: Override the chart subtitle.
            legend: Legend position or visibility. Use "false" to hide.
            format: Output format. Default: "png".
            width: Image width in pixels (50–4000). Default: 1200.
            height: Image height in pixels (50–4000). Default: 600.
            background: Background color as a hex value. Default: #ffffff.
            device_pixel_ratio: Device pixel ratio for the rendered image. Default: 1.
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "chart_ai",
                {
                    "prompt": prompt,
                    "raw_data": raw_data,
                    "title": title,
                    "subtitle": subtitle,
                    "legend": legend,
                    "format": format,
                    "width": width,
                    "height": height,
                    "background": background,
                    "device_pixel_ratio": device_pixel_ratio,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def chart_render(
        self,
        *,
        id: str,
        title: str | None = None,
        labels: str | None = None,
        data1: str | None = None,
        width: str | None = None,
        height: str | None = None,
        format: Literal["png", "svg"] | str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Chart Render. Render a previously saved chart by ID. Public, no API key required. Supports URL overrides for templates (?data1=, ?labels=, ?title=…).

        ``GET /v1/chart/render/{id}``

        Args:
            id: The chart ID returned in the X-Chart-Render-URL header when saving a chart. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            title: Override the chart title.
            labels: Override X-axis labels. Comma-separated.
            data1: Override first dataset values. Comma-separated numbers. Use data2, data3… for additional datasets.
            width: Override output width in pixels (50–4000).
            height: Override output height in pixels (50–4000).
            format: Override output format.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "chart_render",
            {
                "id": id,
                "title": title,
                "labels": labels,
                "data1": data1,
                "width": width,
                "height": height,
                "format": format,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def chart_view(
        self,
        *,
        id: str,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Chart View. View a previously saved chart as an interactive HTML page. Public, no API key required. Iframe-embeddable.

        ``GET /v1/chart/view/{id}``

        Args:
            id: The chart ID returned in the X-Chart-View-URL header when saving a chart. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "chart_view",
                {
                    "id": id,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def diagram(
        self,
        *,
        type_: Literal[
            "mermaid",
            "graphviz",
            "plantuml",
            "d2",
            "svgbob",
            "nomnoml",
            "blockdiag",
            "seqdiag",
            "actdiag",
            "nwdiag",
            "bpmn",
            "erd",
            "excalidraw",
            "ditaa",
            "vega",
            "vegalite",
            "wavedrom",
            "wireviz",
            "c4plantuml",
            "structurizr",
            "tikz",
            "pikchr",
            "umlet",
            "symbolator",
            "packetdiag",
            "rackdiag",
            "bytefield",
            "dbml",
        ]
        | str,
        query: str,
        format: Literal["svg", "png", "jpeg", "pdf"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Diagram. Render a diagram via GET. Use type (mermaid, d2, …), query (source code), and format=png for ChatGPT. POST uses diagram_type and diagram_source instead. Credit cost: 5 credits per call.

        ``GET / POST /v1/diagram``

        Args:
            type_: Diagram language.
            query: Diagram source code (URL-encoded).
            format: Use png so ChatGPT can display the image. svg is for download or infinite scale.
            share: If true, persist the result and return share URLs instead of an image. Leave false to get the image.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "diagram",
            {
                "type": type_,
                "query": query,
                "format": format,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def diagram_ai(
        self,
        *,
        prompt: str,
        diagram_type: Literal["mermaid", "d2", "plantuml", "graphviz"] | str | None = None,
        output_format: Literal["svg", "png", "jpeg", "pdf"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Diagram AI. Describe a diagram in plain English via GET and get a rendered image back. Powered by AI. Credit cost: 10 credits per call.

        ``GET / POST /v1/diagram/ai``

        Args:
            prompt: Describe your diagram in plain English (max 1000 chars). Be specific: mention the diagram type, key entities, and relationships.
            diagram_type: Preferred diagram language. AI chooses if omitted. Examples: "mermaid", "d2", "plantuml", "graphviz".
            output_format: Output format. Default: "svg".
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry. Paid plan: 6-month expiry.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "diagram_ai",
                {
                    "prompt": prompt,
                    "diagram_type": diagram_type,
                    "output_format": output_format,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def diagram_render(
        self,
        *,
        id: str,
        format: Literal["svg", "png", "jpeg", "pdf"] | str | None = None,
        query: str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Diagram Render. Render a previously saved diagram by ID. Public, no API key required. Supports ?format= and ?query= overrides.

        ``GET /v1/diagram/render/{id}``

        Args:
            id: The diagram ID returned in the X-Diagram-Render-URL header when saving a diagram. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            format: Override output format.
            query: Override the diagram source code (URL-encoded).
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "diagram_render",
            {
                "id": id,
                "format": format,
                "query": query,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def diagram_view(
        self,
        *,
        id: str,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Diagram View. View a previously saved diagram as an HTML page. Public, no API key required. Iframe-embeddable with inline SVG rendering.

        ``GET /v1/diagram/view/{id}``

        Args:
            id: The diagram ID returned in the X-Diagram-View-URL header when saving a diagram. Format: cq-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx.
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "diagram_view",
                {
                    "id": id,
                    "share": share,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def jobs(
        self,
        *,
        id: str,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Jobs. Poll the status, progress (0–100) and result of a job started with is_async=true. Polling is free. Poll until status is terminal: CompletedJob, Error, NotFound or BadRequest.

        ``GET /v1/jobs/{id}``

        Args:
            id: The job_id returned by an endpoint called with is_async=true.
        """
        return cast(JsonResponse, await self._call("jobs", {"id": id}, request_options))

    async def label(
        self,
        *,
        query: str,
        format: Literal["svg", "png"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Label Preview. Preview a thermal label via GET. Pass the same label object as a URL-encoded JSON string in query. Inside that JSON, text items use content and size (1-10), not text or fontSize. Prefer format=png for ChatGPT. Credit cost: 3 credits per call.

        ``GET / POST /v1/label``

        Args:
            format: Use png so ChatGPT can display the image. svg is for download or infinite scale.
            share: If true, persist the result and return share URLs instead of an image. Leave false to get the image.
            query: Full label config as URL-encoded JSON. Must include width and elements. Text items use content and size (1-10), not text or fontSize.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "label",
            {
                "format": format,
                "share": share,
                "query": query,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def label_compile(
        self,
        *,
        width: int | float,
        elements: Sequence[Mapping[str, Any]],
        language: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "escpos", "starprnt", "ipl"]
        | str,
        height: int | float | None = None,
        unit: Literal["mm", "inch", "dot"] | str | None = None,
        dpi: int | float | None = None,
        gap: int | float | None = None,
        speed: int | float | None = None,
        density: int | float | None = None,
        direction: int | float | None = None,
        copies: int | float | None = None,
        printer: str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Compile. Compile a label to printer commands (tsc, zpl, epl, …). POST width, language, and elements. Text uses content and size (1-10), not text or fontSize. No barcode element. Example: {"width":40,"height":30,"unit":"mm","language":"zpl","element… Credit cost: 3 credits per call.

        ``POST /v1/label/compile``

        Args:
            width: Label width. Required. Default unit is mm. Example: 40. Do not send query instead of width.
            height: Label height in the same unit. Example: 30. Omit for receipt / continuous mode.
            unit: Measurement unit for width and height. Default mm. Use mm unless you are working in printer dots.
            dpi: Printer DPI. Default 203.
            gap: Gap between labels in mm. Ignored for receipts.
            speed: Print speed, 1-18.
            density: Print darkness, 0-15.
            direction: Print direction. 0 = normal, 1 = reversed.
            copies: Number of copies. Minimum 1.
            printer: Printer profile id (tsc-te210, zebra-zd420, …).
            elements: Required array. Text items need type=text, content, and size (1-10 magnification). Do not use text, fontSize, or type=barcode. Positions x/y are in dots. Example item: {"type":"text","content":"Order…
            language: Required printer language. Example: zpl or tsc. Do not omit.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "label_compile",
                {
                    "width": width,
                    "height": height,
                    "unit": unit,
                    "dpi": dpi,
                    "gap": gap,
                    "speed": speed,
                    "density": density,
                    "direction": direction,
                    "copies": copies,
                    "printer": printer,
                    "elements": elements,
                    "language": language,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def label_convert(
        self,
        *,
        source: str,
        from_: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "ipl"] | str,
        to: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "escpos", "starprnt", "ipl"] | str,
        dpi: int | float | None = None,
        speed: int | float | None = None,
        density: int | float | None = None,
        copies: int | float | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Convert. Convert printer commands from one language to another. POST source, from, and to. from is the source language (tsc, zpl, epl, …). to is the target (tsc, zpl, escpos, …). Credit cost: 5 credits per call.

        ``POST /v1/label/convert``

        Args:
            source: Raw printer commands to convert. Also send from and to.
            from_: Source language.
            to: Target language.
            dpi: Override DPI on the converted output.
            speed: Override print speed, 1-18.
            density: Override print darkness, 0-15.
            copies: Override copies. Minimum 1.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "label_convert",
                {
                    "source": source,
                    "from": from_,
                    "to": to,
                    "dpi": dpi,
                    "speed": speed,
                    "density": density,
                    "copies": copies,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def label_parse(
        self,
        *,
        source: str,
        language: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "ipl"] | str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Parse. Parse printer commands into structured elements. POST source and language (tsc, zpl, epl, …). Credit cost: 1 credit per call.

        ``POST /v1/label/parse``

        Args:
            source: Raw printer commands to parse. Also send language.
            language: Language of the source commands. Example: tsc or zpl.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "label_parse",
                {
                    "source": source,
                    "language": language,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def label_render(
        self,
        *,
        id: str,
        format: Literal["svg", "png"] | str | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """Label Render. Render a previously saved label by ID. Public, no API key required. Supports ?format= override.

        ``GET /v1/label/render/{id}``

        Args:
            id: id
            format: Override output format.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "label_render",
            {
                "id": id,
                "format": format,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def label_validate(
        self,
        *,
        source: str,
        language: Literal["tsc", "zpl", "epl", "cpcl", "dpl", "sbpl", "ipl"] | str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label Validate. Validate printer commands. POST source (the raw commands) and language (tsc, zpl, epl, …). Credit cost: 1 credit per call.

        ``POST /v1/label/validate``

        Args:
            source: Raw printer commands to validate. Also send language.
            language: Language of the source commands. Example: tsc or zpl.
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "label_validate",
                {
                    "source": source,
                    "language": language,
                    "fields": fields,
                    "is_async": is_async,
                    "soft_fail": soft_fail,
                },
                request_options,
            ),
        )

    async def label_view(
        self,
        *,
        id: str,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Label View. View a previously saved label as an HTML page. Public, no API key required. Iframe-embeddable with inline SVG rendering.

        ``GET /v1/label/view/{id}``

        Args:
            id: id
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return cast(
            JsonResponse,
            await self._call(
                "label_view",
                {"id": id, "fields": fields, "is_async": is_async, "soft_fail": soft_fail},
                request_options,
            ),
        )

    async def qrcode(
        self,
        *,
        data: str,
        size: int | float | None = None,
        ec_level: Literal["L", "M", "Q", "H"] | str | None = None,
        dot_type: Literal[
            "square",
            "rounded",
            "dots",
            "diamond",
            "classy",
            "classy-rounded",
            "extra-rounded",
            "vertical-line",
            "horizontal-line",
            "small-square",
            "tiny-square",
        ]
        | str
        | None = None,
        color: str | None = None,
        shape: Literal["square", "circle"] | str | None = None,
        dot_size: int | float | None = None,
        background: str | None = None,
        margin: int | float | None = None,
        version: int | float | None = None,
        mode: Literal["auto", "numeric", "alphanumeric", "byte"] | str | None = None,
        mask: int | float | None = None,
        unit: Literal["px", "mm", "in", "cm"] | str | None = None,
        xml_declaration: bool | None = None,
        aria_label: str | None = None,
        title: str | None = None,
        desc: str | None = None,
        format: Literal["svg", "png"] | str | None = None,
        share: bool | None = None,
        fields: str | None = None,
        is_async: bool | None = None,
        soft_fail: bool | None = None,
        request_options: RequestOptions | None = None,
    ) -> APIResponse:
        """QR Code. Generate a styled QR code via GET. Output: SVG (default) or PNG. Supports dot styles, gradients, custom corners and all QR versions. Credit cost: 3 credits per call.

        ``GET / POST /v1/qrcode``

        Args:
            data: Data to encode in the QR code. Examples:
            size: Output size in pixels (width = height). Default: 200. Examples: ?size=200 (thumbnail), ?size=300 (standard), ?size=400 (large), ?size=600 (poster). For print, use the unit param with mm/cm instead.
            ec_level: Error correction level. Default: M. Higher levels allow more damage/obscuring before the code becomes unreadable.
            dot_type: Module (dot) shape. Default: square. Controls the visual style of each QR code module.
            color: Module color as CSS hex. Default: #000. Examples: ?color=%236366f1 (indigo), ?color=%23dc2626 (red), ?color=%23059669 (green), ?color=%230891b2 (teal). Use %23 to URL-encode #. For gradient objects,…
            shape: Overall QR code shape. Default: square. Use circle to clip the entire QR into a circle: great for profile/avatar-style codes. Example: ?shape=circle&dot_type=dots
            dot_size: Module size ratio between 0.1 and 1. Default: 1 (full). Values below 1 add spacing between modules for a lighter look. Example: ?dot_size=0.85
            background: Background color. Default: #fff. Set to transparent for no background. Example: ?background=%230f172a for dark background. Use %23 to encode #.
            margin: Quiet zone width in modules around the QR code. Default: 4. Minimum recommended by the QR standard: 4. Example: ?margin=2 (compact) or ?margin=6 (extra padding).
            version: QR version from 1 to 40 (determines grid size and data capacity). Leave unset for auto-selection based on data length and ec_level. Example: ?version=5
            mode: Encoding mode. Default: auto (best mode selected for the data). Use numeric for digits-only, alphanumeric for uppercase + digits, byte for arbitrary text/UTF-8. Example: ?mode=numeric
            mask: Mask pattern from 0 to 7. Default: auto (best mask selected to minimize visual patterns). Only set manually if you need a deterministic output. Example: ?mask=3
            unit: Measurement unit for the size param. Default: px. Use mm, in or cm with the size param for print-ready output. Example: ?size=50&unit=mm
            xml_declaration: Prepend an XML declaration (<?xml version="1.0" encoding="UTF-8"?>) to the SVG output. Useful when the SVG will be used as a standalone XML file. Default: false. Example: ?xml_declaration=true
            aria_label: Accessible label added as aria-label on the SVG element. Example: ?aria_label=QR+code+linking+to+chartquery.com
            title: SVG <title> element shown as a browser tooltip and used by screen readers. Example: ?title=ChartQuery+Website
            desc: SVG <desc> element for extended accessibility description. Example: ?desc=Scan+to+visit+https://chartquery.com
            format: Output format. Default: svg. Use png to get a raster image. SVG is lossless and scalable; PNG is pixel-based and suitable for email, PDF or messaging. Example: ?format=png
            share: Set share=true to persist the config and receive JSON instead of an image: { id, render_url, view_url, embed_url, expires_in }. Free plan: 3-day expiry with watermark. Paid plan: 6-month expiry, no b…
            fields: Comma-separated list of fields to keep in the response, with dot notation for nested fields (e.g. name,location.city). Does not change the credit cost.
            is_async: Process the request asynchronously: the response is a job_id to poll on /v1/jobs/{id} (see waitForJob).
            soft_fail: Return HTTP 200 even when an error occurs; the error is then in the response body.
        """
        return await self._call(
            "qrcode",
            {
                "data": data,
                "size": size,
                "ec_level": ec_level,
                "dot_type": dot_type,
                "color": color,
                "shape": shape,
                "dot_size": dot_size,
                "background": background,
                "margin": margin,
                "version": version,
                "mode": mode,
                "mask": mask,
                "unit": unit,
                "xml_declaration": xml_declaration,
                "aria_label": aria_label,
                "title": title,
                "desc": desc,
                "format": format,
                "share": share,
                "fields": fields,
                "is_async": is_async,
                "soft_fail": soft_fail,
            },
            request_options,
        )

    async def stats(
        self,
        *,
        engine: str | None = None,
        path: str | None = None,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Stats. Infrastructure health for an engine or endpoint over the last hour. Not scoped to your account or tenant. Enabled per account: HTTP 403 means contact support to activate it.

        ``GET /v1/stats``

        Args:
            engine: API family to check, for example chart. Provide at least engine or path.
            path: Specific endpoint to check, for example /v1/chart. If you also pass engine, use an endpoint from that API.
        """
        return cast(
            JsonResponse,
            await self._call("stats", {"engine": engine, "path": path}, request_options),
        )

    async def usage(
        self,
        *,
        request_options: RequestOptions | None = None,
    ) -> JsonResponse:
        """Usage. Return this account's Chartquery usage and credit balance. No body. Requires an API key.

        ``GET /v1/usage``
        """
        return cast(JsonResponse, await self._call("usage", {}, request_options))
