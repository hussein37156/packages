#!/usr/bin/env python3
import rospy
import actionlib
from lab_2.msg import actionAction, actionResult, actionFeedback
global server
def callback(goal):
    global server
    print('Received goal:', goal.request)
    feedback = actionFeedback()
    result = actionResult()
    rate = rospy.Rate(1)
    for i in range(goal.request):
        feedback.feedback = str(i)
        server.publish_feedback(feedback)
        rate.sleep()
    result.response = goal.request * 10
    server.set_succeeded(result)
    print('Sent result:', result.response)

def server():
    global server
    rospy.init_node('server')
    rospy.loginfo('Server node started')
    server = actionlib.SimpleActionServer('action', actionAction, callback, False)
    server.start()

if __name__ == '__main__':
    try:
        server()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass