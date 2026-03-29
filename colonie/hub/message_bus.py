import json
from pathlib import Path
from typing import Any, Dict, Iterable

EVENTS_FILE = Path("colonie/hub/events.jsonl")

def append_event(event: Dict[str, Any], file_path: Path = EVENTS_FILE) -> None:
    with file_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")

def read_events(file_path: Path = EVENTS_FILE) -> Iterable[Dict[str, Any]]:
    if not file_path.exists():
        return []
    with file_path.open("r", encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]
