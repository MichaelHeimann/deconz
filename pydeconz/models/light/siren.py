"""Python library to connect deCONZ and Home Assistant to work together."""

from __future__ import annotations

from typing import Literal, TypedDict

from pydeconz.models import ResourceType

from . import ALERT_KEY, ALERT_LONG, LightBase


class TypedSirenState(TypedDict):
    """Siren state type definition."""

    alert: Literal["lselect", "select", "none"]


class TypedSiren(TypedDict):
    """Siren type definition."""

    state: TypedSirenState


class Siren(LightBase):
    """Siren class."""

    ZHATYPE = (ResourceType.WARNING_DEVICE.value,)

    raw: TypedSiren

    @property
    def is_on(self) -> bool:
        """If device is sounding."""
        return self.raw["state"][ALERT_KEY] == ALERT_LONG
