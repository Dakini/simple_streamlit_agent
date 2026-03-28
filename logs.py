import json
import os
import secrets
from pathlib import Path
from datetime import datetime

from pydantic_ai.messages import ModelMessagesTypeAdapter

LOG_DIR = Path(os.getenv("LOGS_DIR", "logs"))
LOG_DIR.mkdir(exist_ok=True)


def serialiser(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serialisable")


def log_entry(agent, messages, source="user"):
    tools = []

    for ts in agent.toolsets:
        tools.extend(ts.tools.keys())
    dict_messages = ModelMessagesTypeAdapter.dump_python(messages)

    return {
        "agent_name": agent.name,
        "system_prompt": agent._instructions,
        "provider": agent.model.system,
        "model": agent.model.model_name,
        "tools": tools,
        "messages": dict_messages,
        "source": source,
    }


def log_interaction_to_file(agent, messages, source="user"):
    entry = log_entry(agent, messages, source)
    ts = entry["messages"][-1]["timestamp"]
    ts_str = ts.strftime("%Y%m%d_%H%M%S")
    rand_hex = secrets.token_hex(3)
    file_path = f"{agent.name}_{ts_str}_{rand_hex}.json"
    file_path = LOG_DIR / file_path

    with file_path.open("w", encoding="utf-8") as f_out:
        json.dump(entry, f_out, indent=2, default=serialiser)
    return file_path
