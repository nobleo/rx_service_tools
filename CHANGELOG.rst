^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package rx_service_tools
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* Roslaunch compatible by allowing unkown arguments (`#1 <https://github.com/nobleo/rx_service_tools/issues/1>`_)
  Only parse known arguments as roslaunch tends to add arguments like __name:= and __log:=
* feat: Interactive service server GUI
  Based on the actionlib/axserver.py. Works exactly the same but for
  services instead of actions.
* Contributors: Felix Widmaier, Tim Clephas
