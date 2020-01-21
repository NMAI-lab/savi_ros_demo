# savi_ros_demo

Welcome to the savi_ros_demo repository. This is a demo project which is intended to show how to setup a project with the savi_ros_bdi package, available at https://github.com/NMAI-lab/savi_ros_bdi.

For instructions on how to set up the savi_ros_bdi package using ROS Kinetic, please see the savi_ros_bdi github page: https://github.com/NMAI-lab/savi_ros_bdi. These instructions assume that you already have a ros workspace with the savi_ros_bdi package set up, as per the instructions at that repository.

This package provides a sample BDI program as well as a sample perception generator and action listener.

Java setup (for the sister repository):
- mkdir SAVI_ROS
- cd SAVI_ROS
- mkdir rosjavaWorkspace
- source ~/rosjava/devel/setup.bash
- cd rosjavaWorkspace/
- mkdir src
- cd src
- catkin_create_rosjava_pkg savi_ros_java
- cd savi_ros_java
- catkin_create_rosjava_project savi_ros_bdi
-> Contents of savi_ros_bdi folder should be a github repo

Python setup:
- cd ~/SAVI_ROS/rosjavaWorkspace/src
- catkin_create_pkg savi_ros_py std_msgs rospy roscpp
- cd savi_ros_py 
- mkdir scripts -> this will be the repository on github
- catkin_make -> from the home directory

Running:
- source devel/setup.bash (in each terminal window)
- roscore (in one terminal window)
- catkin_make (from root of workspace)

- ~/SAVI_ROS/rosjavaWorkspace/src/savi_ros_java/savi_ros_bdi/build/install/savi_ros_bdi/bin 
- ./savi_ros_bdi com.github.rosjava.savi_ros_java.savi_ros_bdi.Talker
- ./savi_ros_bdi com.github.rosjava.savi_ros_java.savi_ros_bdi.Listener


- rosrun savi_ros_py talker.py  
- rosrun savi_ros_py listener.py 
