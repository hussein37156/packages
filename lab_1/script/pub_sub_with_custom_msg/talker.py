#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from lab_1.msg import my_msg

def talker():
    pub = rospy.Publisher("talker", data_class=my_msg, queue_size=10)
    rate = rospy.Rate(4)  # 10 Hz
    while not rospy.is_shutdown():
        msg=my_msg()
        
        msg.name="Hello World"
        msg.time=rospy.get_time()
        pub.publish(msg)
        rospy.loginfo(msg)
        rate.sleep()

def main():
    rospy.init_node("talker", anonymous=True)
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

if __name__ == "__main__":
    main()
        
