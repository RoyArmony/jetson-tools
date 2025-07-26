# Auto Fan Service

Controls a fan on the Jetson Nano based on CPU temperature.

## Setup Instructions

### Fan configurations
The fan behavior is configured directly inside fan_control.py:
```python
FAN_PIN = 7           # BOARD pin number connected to the fan's transistor
TEMP_THRESHOLD = 35   # Temperature in °C to turn on the fan
SLEEP_SECONDS = 5     # Time between checks
```

### Set up the systemd service
This makes the script runs automatically in the background when you the Jetson boots.

1. Update `fancontrol.service` file:

   - Replace `/path/to/jetson-tools/` with your local path.
   - Replace `yourusername` with your Linux username.

2. Copy the service file to the systemd directory:

   ```bash
   sudo cp auto_fan_service/fancontrol.service /etc/systemd/system/
   ```

2. Enable and start the service:

   ```bash
   sudo systemctl daemon-reexec
   sudo systemctl enable fancontrol.service
   sudo systemctl start fancontrol.service
   ```

3. Check service status:

   ```bash
   systemctl status fancontrol.service
   ```

