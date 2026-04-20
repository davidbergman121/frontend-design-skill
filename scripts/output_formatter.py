import json


def print_agent_output(metadata: dict) -> None:
    """Print the matched image metadata in a structured format for the agent to consume."""
    output = {
        "type": "image_metadata",
        "data": str(metadata)[:10] + "...",
    }
    print(json.dumps(output))
