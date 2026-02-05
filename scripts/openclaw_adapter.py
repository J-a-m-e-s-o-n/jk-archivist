"""
OpenClaw transport adapter for JK Archivist.

This module connects OpenClaw events to Archivist logic.
It introduces no new reasoning.
"""

from scripts.evaluate import evaluate_submission
from scripts.memory import append_evaluation, has_already_voted
from scripts.voice import generate_vote_comment


def normalize_event_to_submission(event: dict) -> dict:
    """
    Normalize an OpenClaw event payload into the internal submission shape.
    """
    return {
        "post_id": event.get("post_id"),
        "track": event.get("track"),
        "repo_url": event.get("repo_url"),
        "description": event.get("description", ""),
        "claims": event.get("claims", []),
    }


def handle_submission_event(event: dict, context=None, dry_run: bool = True):
    """
    OpenClaw entrypoint for new submission events.
    """
    submission = normalize_event_to_submission(event)

    post_id = submission.get("post_id")
    if not post_id:
        return

    if has_already_voted(post_id):
        return

    evaluation = evaluate_submission(submission)
    append_evaluation(evaluation)

    vote_comment = generate_vote_comment(evaluation)

    if dry_run or context is None:
        print(vote_comment)
    else:
        # TODO: replace with the exact OpenClaw context method
        context.post_message(vote_comment)
