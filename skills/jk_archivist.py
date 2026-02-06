"""
OpenClaw skill entrypoint for JK Archivist.

This module exposes JK Archivist as an OpenClaw tool.
It contains no judgment logic.
"""

from openclaw import tool
from scripts.openclaw_adapter import handle_submission_event


@tool(
    name="jk_archivist_evaluate",
    description=(
        "Evaluate agent submissions using explicit, inspectable reasoning "
        "and append results to long-term memory."
    )
)
def jk_archivist_evaluate(event: dict):
    """
    OpenClaw tool wrapper for JK Archivist.

    This function is intentionally thin.
    All reasoning, memory, and voice logic lives elsewhere.
    """
    print("JK ARCHIVIST TOOL INVOKED")
    return handle_submission_event(
        event=event,
        context=None,
        dry_run=True,  # KEEP DRY-RUN ENABLED
    )
