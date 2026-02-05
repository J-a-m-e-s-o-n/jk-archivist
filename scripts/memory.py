import json
import os


_ARCHIVE_PATH = os.path.join("archive", "evaluations.jsonl")


def append_evaluation(evaluation):
    """
    Append an evaluation record to archive/evaluations.jsonl.
    """
    os.makedirs(os.path.dirname(_ARCHIVE_PATH), exist_ok=True)
    with open(_ARCHIVE_PATH, "a", encoding="utf-8") as file:
        file.write(json.dumps(evaluation, sort_keys=True))
        file.write("\n")


def has_already_voted(post_id):
    """
    Return True if this post_id already exists in memory.
    """
    if not os.path.exists(_ARCHIVE_PATH):
        return False

    with open(_ARCHIVE_PATH, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue
            if record.get("post_id") == post_id:
                return True
    return False
