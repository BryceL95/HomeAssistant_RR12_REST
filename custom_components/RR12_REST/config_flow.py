import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant.core import HomeAssistant
import requests

_LOGGER = logging.getLogger(__name__)

class MyIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    def __init__(self):
        """Initialize the flow."""
        self._host = None
        self._name = None

    async def async_step_user(self, user_input=None):
        """Handle the initial user step."""
        if user_input is not None:
            self._host = user_input[CONF_HOST]
            self._name = user_input[CONF_NAME]
            return self.async_create_entry(title=self._name, data=user_input)

        return self.async_show_form(
            step_id="user", 
            data_schema=vol.Schema({
                vol.Required(CONF_HOST): str,
                vol.Required(CONF_NAME): str
            })
        )
