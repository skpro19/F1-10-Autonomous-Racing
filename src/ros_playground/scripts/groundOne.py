#/usr/bin/env python

import rospy	

from geometry_msgs.msg import Twist

class ControlTurtlesim():

    def __init__(self):
        rospy.init_node('ControlTurtlesim', anonymous=False)

        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")

        rospy.on_shutdown(self.shutdown)

        self.cmd_vel = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        rate = rospy.Rate(10);
        rospy.loginfo("Set rate 10Hz")
        
        move_cmd = Twist()

	move_cmd.linear.x = 0.3	        # Turn at 0 radians/s
        move_cmd.angular.z = 0
        # Modify this value to cause rotation rad/s

	    # Loop until you type CTRL+c
        while not rospy.is_shutdown():
	   self.cmd_vel.publish(move_cmd)

	   rate.sleep()


    def shutdown(self):
        # You can stop turtlesim_move by publishing an empty Twist message
        rospy.loginfo("Stopping the turtle")

        self.cmd_vel.publish(Twist())

        # Give it some time to stop
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        ControlTurtlesim()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
