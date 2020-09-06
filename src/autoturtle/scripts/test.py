#!/usr/bin/env python i
import rospy
from autoturtle.srv import * 
import sys 



modulenames = set(sys.modules) &  set(globals())

allmodules = [sys.modules[name] for name in modulenames]








