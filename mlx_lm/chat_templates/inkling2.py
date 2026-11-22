# Copyright © 2026 Apple Inc.

"""Response format of Inkling 2.

A turn is a series of messages, each a header and a typed content:

    <|message_model|><|content_thinking|>reasoning<|end_message|>
    <|message_model|>NAME<|content_invoke_tool_json|>{"name":...}<|end_message|>
    <|message_model|><|content_text|>answer<|end_message|>
    <|content_model_end_sampling|>

The text in a header (the role token and a tool name) is dropped. A tool
call ends at the tool parser's end marker, back in the header.
"""

RESPONSE_FORMAT = {
    "initial_state": "header",
    "transitions": {
        "header": [
            ("<|content_thinking|>", "reasoning"),
            ("<|content_text|>", "normal"),
            ("<|content_invoke_tool_json|>", "tool"),
        ],
        "reasoning": [("<|end_message|>", "header")],
        "normal": [("<|end_message|>", "header")],
    },
}
