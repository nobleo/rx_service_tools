cmake_minimum_required(VERSION 3.0.2)
project(rx_service_tools)

find_package(catkin REQUIRED)

catkin_python_setup()

catkin_package()

catkin_install_python(PROGRAMS tools/rx_service_server
                      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION})
