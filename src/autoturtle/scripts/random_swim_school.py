#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

PI = 3.1415926535897

class RandomTurtleSwim:



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

    def make_eight(self):

        

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
        control_node = RandomTurtleSwim()
        #control_node.random_swim()
    except:
        rospy.loginfo("End of the swim for this Turtle.")
