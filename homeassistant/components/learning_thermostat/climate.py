from homeassistant.components.climate import PLATFORM_SCHEMA, ClimateDevice

import pydevd_pycharm
pydevd_pycharm.settrace('localhost', port=29400, stdoutToServer=True, stderrToServer=True)


class MyClimateDevice(ClimateDevice):
    # Implement one of these methods.

    async def async_set_temperature(self, **kwargs):
        """Set new target temperature."""
        import pydevd_pycharm
        pydevd_pycharm.settrace('localhost', port=29400, stdoutToServer=True, stderrToServer=True)
        1+1
        1+1
