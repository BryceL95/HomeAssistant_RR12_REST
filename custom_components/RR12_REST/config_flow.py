import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME
from homeassistant.core import HomeAssistant
import requests

_LOGGER = logging.getLogger(__name__)

class MyIntegrationConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for My Integration."""

    VERSION = 1

    def __init__(self):
        """Initialize the flow."""
        self._api = None

    async def async_step_user(self, user_input=None):
        """Handle the initial user step."""
        if user_input is not None:
            self._api = user_input[CONF_API]
            return self.async_create_entry(title=self._name, data=user_input)

        return self.async_show_form(
            step_id="user", 
            data_schema=vol.Schema({
                vol.Required(CONF_API): str
            })
        )
