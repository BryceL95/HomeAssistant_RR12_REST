from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_HOST, CONF_NAME
import requests

DOMAIN = "my_integration"

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the My Integration component."""
    hass.data[DOMAIN] = {}

    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    """Set up a config entry for My Integration."""
    host = entry.data[CONF_HOST]
    name = entry.data[CONF_NAME]
    hass.data[DOMAIN][entry.entry_id] = MyApiClient(host, name)

    return True

class MyApiClient:
    """Client to interact with the device API."""

    def __init__(self, host, name):
        self._host = host
        self._name = name
        self._url = f"http://{host}/api/data"

    def get_data(self):
        """Fetch data from the device."""
        try:
            response = requests.get(self._url)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException:
            return None
