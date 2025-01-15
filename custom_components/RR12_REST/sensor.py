from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME
from . import MyApiClient

async def async_setup_entry(hass, config_entry, async_add_entities):
    api_client = hass.data["RR12_REST"][config_entry.entry_id]

    async_add_entities([MySensor(api_client)])

class MySensor(Entity):
    def __init__(self, api_client):
        self._api_client = api_client
        self._name = api_client._name
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    async def async_update(self):
        data = self._api_client.get_data()
        if data:
            self._state = data["Devices"][0]["DeviceID"]
        else:
            self._state = None
