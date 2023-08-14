from dataclasses import dataclass
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_zoom.util.event import Event
from typing import Dict, Any, Optional


@dataclass
class TaskOutput:
    output: [Event]
    state: Dict[str, Any]
    has_more_pages: bool
    status_code: int
    error: Optional[PluginException]
