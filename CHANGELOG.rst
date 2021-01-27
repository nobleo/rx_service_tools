^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rx_service_tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

1.0.2 (2021-01-27)
------------------
* Noetic migration using roscompile

1.0.1 (2021-01-14)
------------------
* Roslaunch compatible by allowing unkown arguments (`#1 <https://github.com/nobleo/rx_service_tools/issues/1>`_)
  Only parse known arguments as roslaunch tends to add arguments like __name:= and __log:=
* feat: Interactive service server GUI
  Based on the actionlib/axserver.py. Works exactly the same but for
  services instead of actions.
* Contributors: Felix Widmaier, Tim Clephas
