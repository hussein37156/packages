#!/usr/bin/env python3

import rospy
from lab_1.msg import my_msg

def callback(data):
    rospy.loginfo(data.name+" "+str(data.time))

def listener():
    rospy.init_node("listener", anonymous=True)
    rospy.Subscriber("talker", my_msg, callback)
    rospy.spin()
    
if __name__ == "__main__":
    listener()
    
    

