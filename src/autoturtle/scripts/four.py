#!/usr/bin/env python 

import rospy
from turtlesim.srv import * 
#from swim_school 


def teleport_turtle_client(x ,y, theta):

    rospy.wait_for_service('/turtle1/teleport_absolute')

    try: 

        teleport_turtle = rospy.ServiceProxy('/turtle1/teleport_absolute' , TeleportAbsolute)

        resp1 = teleport_turtle(x , y , theta)

        return resp1

    except rospy.ServiceException as  e : 

        rospy.loginfo('Service call failed')


if __name__ == "__main__" :

    print('Inside the main function')

    teleport_turtle_client(7 ,7, 0)
