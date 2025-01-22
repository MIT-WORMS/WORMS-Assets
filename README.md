# WORMS Assets

## Setup

If you do not have xacro downloaded, you can do so with the following command:

```
sudo apt install ros-<ros2-distro>-xacro
```

## Compiling a WORM

The following code will compile a single WORM, fixed at the origin, with the pony namespace, and store it in the URDFs folder.

```
ros2 run xacro xacro name:=pony XACRO/3dof-worm.urdf.xacro > URDFs/pony-worm.urdf
```
