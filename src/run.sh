#!/bin/bash

# ROS2 Env Setup
. /ros_entrypoint.sh

# ROS2 Build
colcon build

# ROS2 Package Setup
. install/setup.bash

# Run Nodes
(trap 'kill 0' SIGINT; ros2 run bot driver & ros2 run bot sensor)