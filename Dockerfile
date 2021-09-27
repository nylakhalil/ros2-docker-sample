FROM osrf/ros:galactic-desktop

WORKDIR /code/src

ENTRYPOINT [ "/code/src/run.sh" ]
