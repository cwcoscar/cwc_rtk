cmake_minimum_required(VERSION 3.0.2)
project(cwc_rtk)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
)

catkin_package()

catkin_install_python(PROGRAMS
   scripts/receiving_rtk.py
   scripts/ntripclient.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)


