#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

PI = 3.1415926535897

class ControlTurtlesim:



    def get_pose(self, data):

        self.pose = data
        
    
    def near_enough(self): 
        
        
        #return True 


        x0 = 5.444
        y0 = 5.444
        
        x_del = abs(x0 - self.pose.x)
        y_del = abs(y0 - self.pose.y)
    


        if (abs(x0 - self.pose.x) < 0.11 and abs(y0 - self.pose.y) < 0.11): 
           
            #print('**********************************')
            return True 

        else:
            return False
        

        #return [(x0 - self.pose.x) , (y0 - self.pose.y)]
    
    
    def make_eight_1(self):

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

    def make_eight_2(self):

        

        #t0 = rospy.Time.now().to_sec()

        #ang_speed = 0.1

        #curr_ang = 0 
        
        vel_msg = Twist()

        v  = 1.4

        w = 1
        
        r = v / w 

        vel_msg.linear.x = v
        
        t0 = rospy.Time.now().to_sec()

        while not rospy.is_shutdown():
           

            if self.near_enough(): 
                
                rospy.loginfo('Near enoguh triggered')

                t1 = rospy.Time.now().to_sec()

                del_t = t1 - t0 
                
                #rospy.loginfo(f'del_t * v : {del_t * v}')
                #rospy.loginfo_once('2 * PI * r : {2 * PI * r}')

                del_dis = abs(del_t * v  - 2 * PI * r)
                
                #rospy.loginfo(f'del_dis : {del_dis}')

                if abs(del_t * v - 2 * PI * r) < 0.2 : 
                    
                    rospy.loginfo(f'del_t : {del_t} del_dis : {del_dis}')
                    t0 = t1 
                    w=  -w 
                    rospy.loginfo('*********************Changing w ****************************')

            
            
            vel_msg.angular.z = w
            
        
            self.vel_pub.publish(vel_msg)

            self.rate.sleep()
        

    def __init__(self):


        self.pose =  Pose()
        self.counter = 0 
        rospy.init_node('ControlTurtlesim', anonymous=False)
        self.x0 = 5.444
        self.y0 = 5.444    
        self.rate = rospy.Rate(100)

        rospy.loginfo(" Press CTRL+c to stop moving the Turtle")

        rospy.on_shutdown(self.shutdown)
        
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel' , Twist, queue_size = 10)
        
        self.pose_sub = rospy.Subscriber('/turtle1/pose', Pose, self.get_pose)
        #rospy.spin()
        

    def shutdown(self):
        rospy.loginfo("Stopping the turtle")
        rospy.sleep(1)
    




if __name__ == '__main__':
    # Try and Except.
    # If an error is encountered, a try block code execution is stopped and
    # transferred down to the except block.

    try:
        control_node = ControlTurtlesim()
        control_node.make_eight_1()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
