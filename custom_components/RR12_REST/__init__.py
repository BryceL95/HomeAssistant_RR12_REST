from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.const import CONF_HOST, CONF_NAME
import requests

DOMAIN = "RR12_REST"

async def async_setup(hass: HomeAssistant, config: dict):
    hass.data[DOMAIN] = {}
    return True

async def async_setup_entry(hass: HomeAssistant, entry: config_entries.ConfigEntry):
    hass.data[DOMAIN][entry.entry_id] = MyApiClient()

    return True

class MyApiClient:
    def __init__(self):
        self._url = f"https://rest.devices.raceresult.com"

    def get_token(self):
        payload = {}
        headers = {
        'apikey': '32178.6e7d41c306b20b0f5d95f9853ce84106c90eb6baa0214d39779d012c620dc80e33ef9aef1bcfaec3b9101175758b147b'
        }

        response = requests.request("POST", f"{self._url}/token", headers=headers, data=payload)

        print(response.text)

        if response.status_code == 200:
            self._token = response.json().get('access_token')
            print(f"Bearer Token: {self._token}")
        else:
            print(f"Failed to get token: {response.status_code}, {response.text}")

    def get_data(self):
        self.get_token()
        payload = {}
        headers = {
        'Authorization': f"Bearer {self._token}"
        }

        try:
            response = requests.request("GET", f"{self._url}/customers/32178/devices?connected=true", headers=headers, data=payload)
            if response.status_code == 200:
                return response.json()
            else:
                return None
        except requests.exceptions.RequestException:
            return None