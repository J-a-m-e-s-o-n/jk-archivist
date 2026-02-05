from datetime import datetime

from scripts.rubric import RUBRIC, TOTAL_MAX_SCORE


def _normalize_claims(claims):
    if not claims:
        return set()
    return {
        claim.strip().lower()
        for claim in claims
        if isinstance(claim, str) and claim.strip()
    }


def score_with_rubric(submission):
    """
    Apply rubric criteria to a submission and return scores.
    """
    track = (submission.get("track") or "").strip()
    repo_url = (submission.get("repo_url") or "").strip() or None
    claims = _normalize_claims(submission.get("claims"))

    scores = {key: 0 for key in RUBRIC.keys()}

    agent_score = 1
    if track.lower() == "skill" and "autonomous_reasoning" in claims:
        agent_score = 5
    elif "autonomous_reasoning" in claims:
        agent_score = 4
    elif "agent_native" in claims or "agent_required" in claims:
        agent_score = 3
    scores["agent_native_value"] = min(
        agent_score, RUBRIC["agent_native_value"]["max"]
    )

    tech_score = 1
    if len(claims) >= 3:
        tech_score = 2
    if "inspectable_logic" in claims or "explicit_rubric" in claims:
        tech_score = 4
    elif "transparent_scoring" in claims:
        tech_score = max(tech_score, 3)
    scores["technical_clarity"] = min(
        tech_score, RUBRIC["technical_clarity"]["max"]
    )

    safety_score = 2
    if "requests_private_keys" in claims or "requires_private_keys" in claims:
        safety_score = 0
    elif "mainnet_only" in claims:
        safety_score = 1
    elif "testnet_only" in claims or "handles_untrusted_inputs" in claims:
        safety_score = 3
    scores["safety_and_constraints"] = min(
        safety_score, RUBRIC["safety_and_constraints"]["max"]
    )

    usdc_score = 1
    if "agent_governs_allocation" in claims:
        usdc_score = 3
    elif "allocation_governance" in claims or "usdc_allocation" in claims:
        usdc_score = 2
    scores["usdc_allocation_relevance"] = min(
        usdc_score, RUBRIC["usdc_allocation_relevance"]["max"]
    )

    if not repo_url:
        demo_score = 0
    else:
        demo_score = 2
        if "demo_reproducible" in claims or "reproducible" in claims:
            demo_score = 3
    scores["demo_verifiability"] = min(
        demo_score, RUBRIC["demo_verifiability"]["max"]
    )

    return scores


def _verdict_from_total(total_score):
    if total_score >= int(TOTAL_MAX_SCORE * 0.75):
        return "strong accept"
    if total_score >= int(TOTAL_MAX_SCORE * 0.55):
        return "accept"
    if total_score >= int(TOTAL_MAX_SCORE * 0.35):
        return "lean reject"
    return "reject"


def evaluate_submission(submission):
    """
    Produce a full evaluation object for a submission using the rubric.
    """
    scores = score_with_rubric(submission)
    total_score = sum(scores.values())
    verdict = _verdict_from_total(total_score)
    timestamp = datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

    return {
        "post_id": submission.get("post_id"),
        "track": submission.get("track"),
        "scores": scores,
        "total_score": total_score,
        "verdict": verdict,
        "timestamp": timestamp,
    }