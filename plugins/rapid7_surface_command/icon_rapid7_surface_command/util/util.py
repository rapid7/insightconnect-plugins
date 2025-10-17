import csv
import io
from typing import Dict, Any, List


def _csv_text_to_json_rows(csv_text: str) -> List[Dict[str, Any]]:
    """
    Convert CSV text (with headers) to a list of JSON rows (dicts).
    - Always converts empty/whitespace-only strings to None.
    """

    def _normalize(value: str) -> str:
        if value is None:
            return None
        value = value.strip()
        return value if value != "" else None

    csv_text = csv_text.lstrip("\ufeff")  # drop UTF-8 BOM if present
    reader = csv.DictReader(io.StringIO(csv_text, newline=""))
    rows: List[Dict[str, Any]] = []
    for row in reader:
        rows.append({k: _normalize(v) for k, v in row.items()})
    return rows
