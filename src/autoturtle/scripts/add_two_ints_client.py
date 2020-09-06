#!/usr/bin/env python 
import rospy
from autoturtle.srv import * 


def add_two_ints_client(a, b): 

    rospy.wait_for_service('add_two_ints')

    try: 

        add_two_ints = rospy.ServiceProxy('add_two_ints' , AddTwoInts)
        resp1 = add_two_ints(a,b)
        return resp1.sum

    except : 
        print(f'Service call failed with the exception {e}')



if __name__ == "__main__" : 

    print(add_two_ints_client(1,2))

