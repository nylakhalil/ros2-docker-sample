## ros2-docker-sample

#### Run
```sh
./run.sh
```

#### ROS2
- [ROS2 Galactic Package Tutorial](https://docs.ros.org/en/galactic/Tutorials/Creating-Your-First-ROS2-Package.html)
- [ROS2 Galactic Pub/Sub Tutorial](https://docs.ros.org/en/galactic/Tutorials/Writing-A-Simple-Py-Publisher-And-Subscriber.html)

##### Create Package

```sh
ros2 pkg create --build-type ament_python PACKAGE_NAME
```

#### Build
```sh
colcon build

. install/setup.bash
```

##### Run Package

```sh
ros2 run my_package my_node
```