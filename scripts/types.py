"""
Evaluation output schema for JK Archivist.

All evaluations must conform to this shape to remain inspectable and repeatable.
"""

EVALUATION_SCHEMA = {
    "post_id": "str",
    "track": "str",
    "scores": {
        "agent_native_value": "int",
        "technical_clarity": "int",
        "safety_and_constraints": "int",
        "usdc_allocation_relevance": "int",
        "demo_verifiability": "int"
    },
    "total_score": "int",
    "verdict": "str",
    "timestamp": "iso8601 str"
}
