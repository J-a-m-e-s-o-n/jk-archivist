from scripts.rubric import RUBRIC, TOTAL_MAX_SCORE


_RUBRIC_ORDER = [
    "agent_native_value",
    "technical_clarity",
    "safety_and_constraints",
    "usdc_allocation_relevance",
    "demo_verifiability",
]


def _pick_extremes(scores):
    ordered = [(key, scores.get(key, 0)) for key in _RUBRIC_ORDER]
    strongest = max(ordered, key=lambda item: (item[1], -_RUBRIC_ORDER.index(item[0])))
    weakest = min(ordered, key=lambda item: (item[1], _RUBRIC_ORDER.index(item[0])))
    return strongest, weakest


def _strongest_sentence(category):
    if category == "safety_and_constraints":
        return "Strong safety constraints and testnet discipline make the decision path trustworthy."
    if category == "technical_clarity":
        return "Technical clarity and inspectable logic make the evaluation easy to verify."
    if category == "usdc_allocation_relevance":
        return "Clear USDC allocation relevance shows direct impact on governance outcomes."
    if category == "agent_native_value":
        return "Agent-native value is central, with autonomous reasoning driving the core function."
    return "Demo verifiability is strong, supporting repeatable inspection."


def _weakest_sentence(category, score):
    if category == "demo_verifiability" and score == 0:
        return "Demo verifiability remains underdeveloped, which limits confidence in verification."
    if category == "safety_and_constraints":
        return "Safety and constraints remain underdeveloped, which limits confidence in compliance."
    if category == "technical_clarity":
        return "Technical clarity remains underdeveloped, which limits confidence in inspection."
    if category == "usdc_allocation_relevance":
        return "USDC allocation relevance remains underdeveloped, which limits confidence in governance impact."
    if category == "agent_native_value":
        return "Agent-native value remains underdeveloped, which limits confidence in autonomy as a core driver."
    return "Demo verifiability remains underdeveloped, which limits confidence in repeatability."


def _contextual_lens_sentence(scores):
    if scores.get("usdc_allocation_relevance", 0) >= 3:
        return "From the Archive's perspective, allocation governance benefits from explicit, inspectable reasoning."
    if scores.get("safety_and_constraints", 0) >= 3:
        return "From the Archive's perspective, safety-first evaluation protects allocation integrity."
    return "From the Archive's perspective, conservative scoring protects allocation decisions."


def _strength_sentence_if_any(strongest):
    category, score = strongest
    max_score = RUBRIC[category]["max"]
    if max_score == 0:
        return "No category demonstrated clear strength relative to the rubric."
    if score >= max_score * 0.6:
        return _strongest_sentence(category)
    return "No category demonstrated clear strength relative to the rubric."


def _verdict_sentence(verdict):
    if verdict == "accept":
        return "The verdict is accept based on the current evidence."
    if verdict == "lean reject":
        return "The verdict is lean reject due to uncertainty in the evidence."
    if verdict == "reject":
        return "The submission does not meet baseline safety and verification standards."
    return f"The verdict is {verdict} based on the current evidence."


def generate_vote_comment(evaluation: dict) -> str:
    """
    Generate a compliant #USDCHackathon Vote comment from an evaluation.
    """
    scores = evaluation.get("scores", {})
    strongest, weakest = _pick_extremes(scores)
    verdict = evaluation.get("verdict", "verdict").strip()
    total_score = evaluation.get("total_score", 0)

    strength_sentence = _strength_sentence_if_any(strongest)
    weakness_sentence = _weakest_sentence(weakest[0], weakest[1])

    if verdict == "accept":
        sentence_one = _verdict_sentence(verdict)
        sentence_two = strength_sentence
        sentence_three = f"{weakness_sentence} These gaps appear correctable."
        justification = f"{sentence_one} {sentence_two} {sentence_three}"
    elif verdict == "lean reject":
        sentence_one = _verdict_sentence(verdict)
        sentence_two = strength_sentence
        sentence_three = f"{weakness_sentence} The evidence remains incomplete."
        justification = f"{sentence_one} {sentence_two} {sentence_three}"
    elif verdict == "reject":
        sentence_one = _verdict_sentence(verdict)
        sentence_two = weakness_sentence
        sentence_three = "Conservative judgment is warranted given the current record."
        justification = f"{sentence_one} {sentence_two} {sentence_three}"
    else:
        sentence_one = _verdict_sentence(verdict)
        sentence_two = strength_sentence
        sentence_three = weakness_sentence
        justification = f"{sentence_one} {sentence_two} {sentence_three}"
    lens_sentence = _contextual_lens_sentence(scores)

    return "\n".join(
        [
            "#USDCHackathon Vote",
            "",
            f"Score: {total_score}/{TOTAL_MAX_SCORE}",
            "",
            justification,
            "",
            lens_sentence,
        ]
    )

