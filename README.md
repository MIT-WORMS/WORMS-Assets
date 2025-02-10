# WORMS Assets

## Setup

If you do not have xacro downloaded, you can do so with the following command:

```bash
sudo apt install ros-<ros2-distro>-xacro
```

## Compiling a WORM

The following command will compile a single WORM, fixed at the origin, with the pony namespace, and store it in the URDFs folder.

```bash
ros2 run xacro xacro name:=pony XACRO/3dof-worm.urdf.xacro > URDFs/pony-worm.urdf
```

## Compiling a turtle pallet

The following command will compile a turtle pallet, in a planar world, with worms of the indicated names, and store it in the URDFs folder.

```bash
ros2 run xacro xacro \
        front_left:=duck \
        front_right:=frog \
        back_left:=lion \
        back_right:=pony \
    XACRO/turtle.urdf.xacro > URDFs/turtle.urdf
```