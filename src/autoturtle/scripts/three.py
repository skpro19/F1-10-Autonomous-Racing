#!/usr/bin/env python 

import rospy
from autoturtle.srv import *



def handle_teleport_turtle(req):

    rospy.loginfo(f'Teleporting  the turtle to x : {req.x} y : {req.y} theta : {req.theta}')
    return TeleportTurtleResponse()


def teleport_turtle_server(): 

    
    rospy.init_node('teleport_turtle_server')
    
    s = rospy.Service('teleport_turtle_custom' , TeleportTurtle, handle_teleport_turtle)

    rospy.loginfo('Ready to teleport the turtle')

    rospy.spin()










if __name__ == "__main__" :

    print("Hello World!")

    teleport_turtle_server()


