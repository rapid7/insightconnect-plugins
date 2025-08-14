import csv
import io
from typing import Dict, Any, List


def _csv_text_to_json_rows(csv_text: str, convert_empty_to_none: bool = True) -> List[Dict[str, Any]]:
    """
    Convert CSV text (with headers) to a list of JSON rows (dicts).
    - Handles quoted fields and commas safely via csv module.
    - Optionally converts empty strings to None.
    """
    # Handle possible UTF-8 BOM and normalize newlines
    csv_text = csv_text.lstrip("\ufeff")
    # Use universal newline handling
    stream = io.StringIO(csv_text, newline="")
    reader = csv.DictReader(stream)
    rows: List[Dict[str, Any]] = []
    for row in reader:
        if convert_empty_to_none:
            row = {k: (v if v not in ("", None) else None) for k, v in row.items()}
        rows.append(row)
    return rows
