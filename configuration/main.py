# configuration/main.py: version: 2020-10-17 04:00

settings = {
# "application":     "applications/default",  # Application to run
# "application":     "applications/joysticks",
# "application":     "applications/led_strip",
# "application":     "applications/nodebots",
# "application":     "applications/step_controller",
# "application":     "applications/squirrel",
  "application":     "applications/swagbadge",
# "application":     "lolibot",

  "gc_enabled":       False,  # Display Garbage Collector statistics
  "logger_enabled":   False,  # Display everyone's log output
  "oled_enabled":     True,   # OLED attached
  "services_enabled": False   # Use Aiko Services infrastructure
}

def parameter(name, settings=settings):
  if name in settings: return settings[name]
  return False
