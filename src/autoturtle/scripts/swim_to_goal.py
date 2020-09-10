#!/usr/bin/env python

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math





class ControlTurtlesim: 

    
    def swim_to_goal_func(self, t_x, t_y, tolerance):
        
        rospy.loginfo('Inside the swim_to_goal function')

        vel_msg = Twist() 

        

        while not rospy.is_shutdown():
            
            

            p_x = self.pose.x
            p_y = self.pose.y
            p_theta= self.pose.theta


            rospy.loginfo(f'p_x: {p_x} p_y: {p_y}')

            dis = math.sqrt((p_x- t_x) * (p_x - t_x) + (p_y - t_y) * (p_y - t_y))
            


            rospy.loginfo(f'dis: {dis}')

            if dis < tolerance: 
                break;


            v_x  = 1.5 * dis 
            
            #v_x= 0
            #w_z = 1

            steering_angle  =  math.atan2(t_y - p_y , t_x - p_x) 
            
            w_z = 4 * (steering_angle - p_theta)

            vel_msg.linear.x = v_x 
            vel_msg.angular.z = w_z

            self.vel_pub.publish(vel_msg)
            self.rate.sleep()


    def pose_callback(self, data): 

        #rospy.loginfo('Subscribed to pose data') 
        #rospy.loginfo(f'x: {data.x} y: {data.y}')
        self.pose= data
        self.pose.x = round(data.x, 4)
        self.pose.y= round(data.y, 4)
        #rospy.loginfo(f'x: {self.pose.x} y: {self.pose.y}')
 

    def shutdown(self):

        rospy.loginfo('Stopping the turtle')
        rospy.sleep(1)

    def __init__(self):
        
        rospy.loginfo('Initializing the turtlesim node')
        rospy.init_node('swim_to_goal' , anonymous = False) 
        
        self.pose = Pose()

        self.rate = rospy.Rate(10)

        rospy.on_shutdown(self.shutdown)



        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist, queue_size = 100)






    




if __name__ == "__main__": 

    print("Hello World!")

    try: 
        


        control_node = ControlTurtlesim()
        
        t_x, t_y, tolerance = [float(x) for x  in input ('Enter x , y and tolerance : ').split()]

        rospy.loginfo(f'x: {t_x} y: {t_y} tolerance: {tolerance}')
        
        control_node.swim_to_goal_func(t_x, t_y, tolerance)


    except Exception as e: 
        rospy.loginfo(f'Exiting due to the exception {e}')
