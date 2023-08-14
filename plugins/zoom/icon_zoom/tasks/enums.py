from enum import Enum


class RunState(Enum):
    """
    Enum to help with variable/logic determination throughout task.
    Runstates should progress from starting (first run) to either paginating or continuing, depending on whether or
    not the latest events require pagination or if the entire event set was returned in one page.
    """

    starting = "starting"
    paginating = "paginating"
    continuing = "continuing"
