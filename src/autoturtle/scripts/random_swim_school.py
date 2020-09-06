#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import *


PI = 3.1415926535897

class ControlTurtlesim:

    def get_pose(self, data):

        self.pose = data
        
    
    def make_eight_1(self,x,y):

        vel_msg = Twist()
        
        w = 4
        v = 4

        counter =0 

        x_p = self.pose.x 
        y_p = self.pose.y

        while not rospy.is_shutdown():
            
            rospy.loginfo('Inside the while loop')
            x_c = self.pose.x 
            y_c = self.pose.y

               
            cond = x_p < self.x0 and  x_c > self.x0
            
            rospy.loginfo(f'cond : {cond}')
                
            if (x_p < self.x0 and  x_c > self.x0) :

                w = -1 * w
                rospy.loginfo(f'New w : {w}')                
                rospy.loginfo('************ Changing w ***************')

            rospy.loginfo('Outside the while loop')

            x_p = x_c
            y_p = y_c
            

           
            vel_msg.linear.x =v
            vel_msg.angular.z=w
            
            rospy.loginfo(f'v =  {v}  w = {w}')

            self.vel_pub.publish(vel_msg)
                
            rospy.loginfo(f'After the velocity publisher')

            self.rate.sleep()


    def __init__(self, x, y):


        self.pose =  Pose()
        self.counter = 0 
        rospy.init_node('ControlTurtlesim', anonymous=False)
        self.x0 = x
        self.y0 = y    
        self.rate = rospy.Rate(100)

        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")

        rospy.on_shutdown(self.shutdown)
        
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist, queue_size = 10)
        
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.get_pose)
        #rospy.spin()
        

    def shutdown(self):
        rospy.loginfo("Stopping the turtle")
        rospy.sleep(1)
 
        

    def teleport_turtle_client(self, x , y, theta): 
        
        rospy.loginfo('Inside teleport_turtle_client function')

        rospy.wait_for_service('/turtle1/teleport_absolute')

        try: 
            
            rospy.loginfo('Inside the try block')

            teleport_turtle = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)

            resp1 = teleport_turtle(x, y, theta)
    
            rospy.loginfo('resp1 : {resp1}')
            
            return resp1

        except rospy.ServiceException as e: 
            rospy.loginfo('Service call failed')


if __name__ == '__main__':
    
    try:
        x, y, theta = [float(s) for s in input ('Enter x, y and theta : ').split()]
      
    except ValueError:
       
        print('Please enter three values!')
    
    try:
        control_node = ControlTurtlesim(x,y)
        control_node.teleport_turtle_client(x, y, theta )
        control_node.make_eight_1(x,y)
    except Exception as e:
        rospy.loginfo(f"Exception: {e}")
