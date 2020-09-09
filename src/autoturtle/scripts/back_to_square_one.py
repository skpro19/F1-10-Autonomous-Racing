#!/usr/bin/env python
import random
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import *
import math
from std_srvs.srv import Empty


PI = 3.1415926535897

class ControlTurtlesim:

    def get_pose(self, data):

        self.pose = data

    def change_background_color_client(self): 

        rospy.loginfo('Starting  change_background_color_client') 
        
        rospy.wait_for_service('/clear')

        try: 

            rospy.loginfo('Inside the try block')
            
            rospy.set_param('/turtlesim/background_r', 255)
            rospy.set_param('/turtlesim/background_g' , 0)
            rospy.set_param('/turtlesim/background_b', 0)

            change_background_color = rospy.ServiceProxy('/clear' , Empty)

            resp = change_background_color()

            return resp
        except rospy.ServiceException as e: 
            rospy.loginfo(f'Service failed due to the exception {e}')



    def turn_off_pen_client(self, off) : 

        rospy.loginfo('Starting the pen client')

        rospy.wait_for_service('/turtle1/set_pen')

        try: 

            rospy.loginfo('Inside the try block')

            turn_off_pen = rospy.ServiceProxy('/turtle1/set_pen', SetPen)
            
            x =0  

            if off == 1: 
                x = 1

            else: 

                x = 0 

            resp1 = turn_off_pen(255 , 255, 255, 3, x)

            return resp1
        
        except rospy.ServiceException as e : 
            rospy.loginfo('Service call failed')

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

    def move_fwd_2(self, length) :

        v = 0.1

        vel_msg = Twist() 

        vel_msg.linear.x = v

        t0 = rospy.Time.now().to_sec()
        
        dis= 0 

        while not rospy.is_shutdown():


            rospy.loginfo(f'vel_msg.linear.x : {vel_msg.linear.x}')

            
            if dis >= length: 
                vel_msg.linear.x =0 
                self.vel_pub.publish(vel_msg)
                break; 

            self.vel_pub.publish(vel_msg)

            t1= rospy.Time.now().to_sec() 

            dis = (t1- t0) * v
                
            rospy.loginfo(f'dis : {dis}')

    def rotate_1(self): 

        w = 0.1 
        
        t0 = rospy.Time.now().to_sec()

        ang = 0 
        
        vel_msg = Twist() 

        vel_msg.angular.z = w 

        while not rospy.is_shutdown() : 
            
            if ang >= math.pi/2 : 

                vel_msg.angular.z =0 
                self.vel_pub.publish(vel_msg)
                break; 

            self.vel_pub.publish(vel_msg)

            t1= rospy.Time.now().to_sec()
            
            delta = t1 - t0 

            rospy.loginfo(f'delta : {delta}')

            ang = (t1 - t0) * w 

            rospy.loginfo(f'ang : {ang}')
            
            #self.rate.sleep()



    


    def __init__(self):



        self.pose =  Pose()
        rospy.init_node('ControlTurtlesim', anonymous=False)
        
       
        

        rospy.set_param('/background_b',random.randint(0,255))
        rospy.set_param('/background_g',random.randint(0,255))
        rospy.set_param('/background_r',random.randint(0,255))

        self.pub_rate = 100

        self.rate = rospy.Rate(1)

        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")

        rospy.on_shutdown(self.shutdown)
        
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist, queue_size = 10)
        
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.get_pose)
        #rospy.spin()
        

    def shutdown(self):
        rospy.loginfo("Stopping the turtle")
        rospy.sleep(1)
 
        



if __name__ == '__main__':
    
    
    try:
        
        length = float(input('Enter side length: '))

        control_node = ControlTurtlesim()
        
        control_node.change_background_color_client()
        
        control_node.turn_off_pen_client(1)
        
        control_node.teleport_turtle_client(1,1, 0)
        
        control_node.turn_off_pen_client(0)
        
        for i in range(0, 4) : 
            control_node.move_fwd_2(length)
            control_node.rotate_1()

        rospy.loginfo('Finished drawing the square')

    except Exception as e:
        rospy.loginfo(f"Exception: {e}")
