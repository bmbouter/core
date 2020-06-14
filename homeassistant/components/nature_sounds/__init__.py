"""Create the Nature Sound component."""
import asyncio

DOMAIN = "nature_sounds"


@asyncio.coroutine
def async_setup(hass, config):
    """Set up the nature_sounds component."""

    # import pydevd_pycharm
    # pydevd_pycharm.settrace('localhost', port=29431, stdoutToServer=True, stderrToServer=True)

    # Data that you want to share with your platforms
    hass.data[DOMAIN] = {"temperature": 23}

    hass.helpers.discovery.load_platform("switch", DOMAIN, {}, config)
    hass.states.async_set("nature_sounds.Hello_World", "Works!")
    return True


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up platform."""
    import pydevd_pycharm

    pydevd_pycharm.settrace(
        "localhost", port=29431, stdoutToServer=True, stderrToServer=True
    )
    # Code for setting up your platform inside of the event loop.
