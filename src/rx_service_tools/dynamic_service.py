#! /usr/bin/python
#
# This code is based on dynamic_action.py of the actionlib package, written by
# Eitan Marder-Eppstein.
# Adapted to work for services by Felix Widmaier at Synapticon GmbH.
#
# **********************************************************
#  Software License Agreement (BSD License)
#
#   Copyright (c) 2009, Willow Garage, Inc.
#   Copyright (c) 2018, Synapticon GmbH
#   All rights reserved.
#
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions
#   are met:
#
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
#    * Neither the name of Willow Garage, Inc. nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
#
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#   FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#   COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#   LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#   ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#   POSSIBILITY OF SUCH DAMAGE.
# **********************************************************
"""Helper class to load service message types."""
import roslib
import rospy
import sys


class DynamicService(object):
    """Provides types of the given service message."""

    def __init__(self, name):
        """Initialize.

        Args:
            name (str): Name of the service type (e.g. "std_srvs/SetBool").

        """
        self.name = name
        self.base = self.load_submsg('')
        self.request = self.load_submsg('Request')
        self.response = self.load_submsg('Response')

    def load_submsg(self, subname):
        """Load submessage.

        Args:
            subname (str): Suffix that is added to the type.

        Returns:
            The sub-message type.

        """
        msgclass = roslib.message.get_service_class(self.name + subname)
        if msgclass is None:
            rospy.logfatal('Could not load message for: %s' % (self.name +
                                                               subname))
            sys.exit(1)
        return msgclass
