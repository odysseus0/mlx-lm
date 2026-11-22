# Copyright © 2026 Apple Inc.

"""Tool call parser for Inkling 2.

A call is a message of its own:

    <|message_model|>NAME<|content_invoke_tool_json|>{"name":"NAME","args":{...}}<|end_message|>

The server strips the markers, leaving the JSON.
"""

import json
from typing import Any, Optional

tool_call_start = "<|content_invoke_tool_json|>"
tool_call_end = "<|end_message|>"


def parse_tool_call(
    model_output: str, tools: Optional[Any] = None
) -> dict[str, Any]:
    try:
        call = json.loads(model_output.strip())
    except ValueError as e:
        raise ValueError("No function provided.") from e
    if not isinstance(call, dict) or not isinstance(call.get("name"), str):
        raise ValueError("No function provided.")
    arguments = call.get("args", call.get("arguments", {}))
    if not isinstance(arguments, dict):
        raise ValueError("Tool call arguments must be an object.")
    return {"name": call["name"], "arguments": arguments}
