import json

from scripts.evaluate import evaluate_submission
from scripts.memory import append_evaluation, has_already_voted
from scripts.voice import generate_vote_comment


def run(dry_run: bool = True):
    """
    Main entry point for the JK Archivist.

    Coordinates fetching submissions, evaluating them,
     and generating votes/outputs.
    """
    submissions = [
        {
            "post_id": "demo-001",
            "track": "Skill",
            "repo_url": "https://github.com/example/archivist-skill",
            "description": "An agent-native evaluator with explicit scoring.",
            "claims": [
                "autonomous_reasoning",
                "inspectable_logic",
                "agent_governs_allocation",
                "testnet_only",
            ],
        },
        {
            "post_id": "demo-002",
            "track": "Tool",
            "repo_url": None,
            "description": "A submission without public code or reproducible demo.",
            "claims": [
                "requests_private_keys",
            ],
        },
    ]

    for submission in submissions:
        if has_already_voted(submission["post_id"]):
            continue
        evaluation = evaluate_submission(submission)
        append_evaluation(evaluation)
        print(json.dumps(evaluation, sort_keys=True))
        print(generate_vote_comment(evaluation))
        print()
