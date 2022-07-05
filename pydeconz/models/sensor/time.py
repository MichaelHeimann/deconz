"""Python library to connect deCONZ and Home Assistant to work together."""

from typing import TypedDict

from pydeconz.models import ResourceType

from . import SensorBase


class TypedTimeState(TypedDict):
    """Time state type definition."""

    lastset: str


class TypedTime(TypedDict):
    """Time type definition."""

    state: TypedTimeState


class Time(SensorBase):
    """Time sensor."""

    ZHATYPE = (ResourceType.ZHA_TIME.value,)

    raw: TypedTime

    @property
    def last_set(self) -> str:
        """Last time time was set."""
        return self.raw["state"]["lastset"]
