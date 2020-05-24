# TFE weather

This is a minimum implementation of an integration providing the weather from TFE @ Umeå University as a sensor.

### Installation

Copy this folder to `<config_dir>/custom_components/tfe_weather/`.

Add the following to your `configuration.yaml` file:

```yaml
# Example configuration.yaml entry
sensor:
  platform: tfe_weather
  scan_interval: 60
```
