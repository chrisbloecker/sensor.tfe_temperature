# sensor.tfe_weather
Provides the weather as measured by TFE @ Umeå University as a sensor for home assistant.

### Installation
Copy the `tfe_weather` folder into your `custom_components` folder.

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  platform: tfe_weather
  scan_interval: 60
```
