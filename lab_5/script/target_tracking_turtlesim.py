#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
class TurtleBot:
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        self.pose = Pose()
        self.rate = rospy.Rate(10)
        
    def update_pose(self, data):
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)
        
    def euclidean_distance(self, goal_pose):
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +pow((goal_pose.y - self.pose.y), 2))
    
    def linear_vel_controller(self, goal_pose, k_p=1.5):
        return k_p * self.euclidean_distance(goal_pose)
    
    def steering_angle(self, goal_pose):
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
    
    def angular_vel_controller(self, goal_pose, k_p=6):
        return k_p * (self.steering_angle(goal_pose) - self.pose.theta)
    
    def move2goal(self):
        goal_pose = Pose()
        goal_pose.x = float(input("Set your x goal: "))
        goal_pose.y = float(input("Set your y goal: "))
        distance_tolerance = 0.1
        vel_msg = Twist()
        while self.euclidean_distance(goal_pose) >= distance_tolerance and not rospy.is_shutdown():
            vel_msg.linear.x = self.linear_vel_controller(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel_controller(goal_pose)
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
            vel_msg.linear.x = 0
            vel_msg.angular.z = 0
            self.velocity_publisher.publish(vel_msg)
            
if __name__ == '__main__':
    try:
        x = TurtleBot()
        x.move2goal()
    except rospy.ROSInterruptException:
        pass