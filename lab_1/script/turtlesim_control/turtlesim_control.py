#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys
import math

def move(major=1, minor=1 , omega=1):
    pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=10)
    F=500
    rate = rospy.Rate(F)  # 4 Hz
    counter=0
    while not rospy.is_shutdown():
        msg = Twist()
        x=-omega*math.cos(omega*(1/F)*counter) * major
        y=omega*math.sin(omega*(1/F)*counter) * minor
        msg.linear.x = x
        msg.linear.y = y
        #msg.angular.z = math.atan2(y,x)
        counter += 1
        pub.publish(msg)
        rate.sleep()

if __name__ == "__main__":
    rospy.init_node("turtlesim_control", anonymous=True)
    
    major = 1.0
    minor = 1.0
    omega = 1.0
    
    if rospy.has_param("~major") and rospy.has_param("~minor") and rospy.has_param("~omega"):
        major = rospy.get_param("~major")
        minor = rospy.get_param("~minor")
        omega = rospy.get_param("~omega")
    elif len(sys.argv) > 2:
        try:
            major = float(sys.argv[1])
            minor = float(sys.argv[2])
            omega = float(sys.argv[3])
            
        except ValueError:
            rospy.logerr("Invalid arguments provided. Usage: rosrun lab_1 turtlesim_control.py <vel> <radius>")
            sys.exit(1)
    else:
        rospy.loginfo("Using default values for velocity and radius")

    try:
        move(major, minor, omega)
    except rospy.ROSInterruptException:
        pass
