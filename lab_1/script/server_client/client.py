#!/usr/bin/env python3

import rospy
from lab_1.srv import *
import sys
def client(x,y):
    rospy.wait_for_service('service')
    add = rospy.ServiceProxy('service', addition)
    resp = add(x, y)
    print(resp.sum)
    return resp.sum

if __name__ == "__main__":
    x=int(sys.argv[1])
    y=int(sys.argv[2])
    client(x,y)
    
    