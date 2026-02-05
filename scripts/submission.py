"""
Internal submission representation for JK Archivist.

This shape intentionally abstracts away Moltbook/OpenClaw specifics.
"""

SUBMISSION_SCHEMA = {
    "post_id": "str",
    "track": "str",
    "repo_url": "str | None",
    "description": "str",
    "claims": "list[str]",
}
