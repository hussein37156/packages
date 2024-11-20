#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
def Move_Robot():
    rospy.init_node('turtle_bot_control', anonymous=False)
    vel_msg = Twist()
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
    r = 0.1
    l= 0.2 
    Wr = 7 
    Wl = 5 
    v = (r/2) * (Wr + Wl) 
    w = (r/l) * (Wr - Wl) 
    vel_msg.linear.x = v
    vel_msg.linear.y = 0.0
    vel_msg.linear.z = 0.0
    vel_msg.angular.x = 0.0
    vel_msg.angular.y = 0.0
    vel_msg.angular.z = w
    while not rospy.is_shutdown():
        pub.publish(vel_msg)
        rate.sleep()
if __name__ == '__main__':
    Move_Robot()