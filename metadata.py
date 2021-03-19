from dataclasses import dataclass
from typing import Union
from typing import List

@dataclass
class Metadata:
    __slots__ = ["venue", "vehicle", "driver", "comment", "date", "time", "samplerate", "duration", "beacons", "times"]
    venue       : str
    vehicle     : str
    driver      : str
    comment     : str
    date        : str
    time        : str
    samplerate  : str
    duration    : str
    beacons     : str
    times       : str
