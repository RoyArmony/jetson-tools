# Auto Fan Service

Controls a fan on the Jetson Nano based on CPU temperature.

## Setup Instructions

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

