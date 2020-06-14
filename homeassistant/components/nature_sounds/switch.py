"""Support for Nature Sound switches."""
from homeassistant.components.switch import SwitchEntity


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up platform."""
    # Code for setting up your platform inside of the event loop.
    import pydevd_pycharm

    pydevd_pycharm.settrace(
        "localhost", port=29431, stdoutToServer=True, stderrToServer=True
    )
    hass.states.async_entity_ids()
    if discovery_info is None:
        return
    async_add_entities([NatureSwitch("qq")])


class NatureSwitch(SwitchEntity):
    """Adds support for a NatureSwitch."""

    def __init__(self, media_player):
        """Instantiate a Nature Switch."""
        self.media_player = media_player

    @property
    def name(self):
        """Return the name of the device if any."""
        return "asdfasdf"

    async def async_turn_on(self, **kwargs):
        """Turn the entity on."""

    async def async_turn_off(self, **kwargs):
        """Turn the entity off."""

    @property
    def is_on(self) -> bool:
        """Return True if entity is on."""
        return True
