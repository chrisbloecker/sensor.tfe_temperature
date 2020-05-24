"""Platform for sensor integration."""
from homeassistant.const import TEMP_CELSIUS
from homeassistant.helpers.entity import Entity

import requests
import xmltodict


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the sensor platform."""
    add_entities([TFEWeather()])


class TFEWeather(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state            = None
        self._state_attributes = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'TFE weather'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes of the sensor."""
        return self._state_attributes

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return TEMP_CELSIUS

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """

        url = "http://www8.tfe.umu.se/WeatherWebService2012/Service.asmx/Aktuellavarden"

        content = requests.get(url).content
        doc     = xmltodict.parse(xmltodict.parse(content)["string"]["#text"])["root"]

        self._state = float(doc["tempmed"].replace(",", "."))

        attributes = {}

        attributes["humidity"]       = float(doc["fukt"].replace(",", "."))
        attributes["pressure"]       = int(doc["tryck"])
        attributes["rain"]           = float(doc["regn"].replace(",", "."))
        attributes["wind_speed"]     = float(doc["vindh"].replace(",", "."))
        attributes["wind_direction"] = int(doc["vindr"])

        if doc["windChill"] != "-":
            attributes["feels_like"] = float(doc["windChill"].replace(",", "."))

        self._state_attributes = attributes
