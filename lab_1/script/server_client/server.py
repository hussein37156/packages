#!/usr/bin/env python3

import rospy
from lab_1.srv import addition, additionResponse

def callback(req):
    print("Request received")
    return additionResponse(req.x + req.y)

if __name__ == "__main__":
    rospy.init_node("servar", anonymous=True)
    rospy.loginfo("Server is running")
    s = rospy.Service('service', addition, callback)
    rospy.spin()
    