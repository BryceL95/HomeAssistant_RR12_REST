from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME
from . import MyApiClient

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Set up the sensor based on the config entry."""
    api_client = hass.data["my_integration"][config_entry.entry_id]

    async_add_entities([MySensor(api_client)])

class MySensor(Entity):
    """Representation of a sensor that fetches data from the device."""

    def __init__(self, api_client):
        self._api_client = api_client
        self._name = api_client._name
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Fetch new state data from the device."""
        data = self._api_client.get_data()
        if data:
            self._state = data.get("value")  # Replace with actual key in the response
        else:
            self._state = None
