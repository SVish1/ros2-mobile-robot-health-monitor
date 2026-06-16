# ROS2 Mobile Robot Health Monitor

## Overview
ROS2 package for monitoring mobile robot health using LiDAR and odometry data.

## Features
- LiDAR frequency monitoring
- Robot speed estimation
- Distance traveled tracking
- ROS2 publisher/subscriber architecture

## Topics

Subscribed:
- /scan
- /odom

Published:
- /robot_status

## Technologies
- ROS2 Humble
- Python
- sensor_msgs
- nav_msgs
- std_msgs

## Build
```bash
colcon build
source install/setup.bash
```

## Run
```bash
ros2 run robot_health_monitor health_monitor
```

## Example Output
LiDAR: 10.00 Hz | Speed: 0.50 m/s | Distance: 12.4 m

## Future Improvements
- Battery monitoring
- ROS diagnostics integration
- Launch files
- Lifecycle nodes
- Health dashboard

