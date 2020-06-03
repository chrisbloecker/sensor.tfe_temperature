# sensor.tfe_temperature
Provides the temperature as measured by TFE @ Umeå University as a sensor for home assistant.

### Installation
Copy the `tfe_temperature` folder into your `custom_components` folder.

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  - platform: tfe_temperature
    scan_interval: 60
```
