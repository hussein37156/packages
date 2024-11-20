#!/usr/bin/env python3
import rospy
import actionlib
import sys
from lab_2.msg import actionAction, actionGoal
def feedback(msg):
    print('Feedback:'+ msg.feedback)

def client(request):
    print('Request:', request)
    rospy.init_node('client')
    rospy.loginfo('Client node started')
    client = actionlib.SimpleActionClient('action', actionAction)
    client.wait_for_server()
    goal = actionGoal()
    goal.request = request
    client.send_goal(goal, feedback_cb=feedback)
    client.wait_for_result()
    result = client.get_result()
    rospy.loginfo('Result: %d', result.response)

if __name__ == '__main__':
    try:
        client(int(sys.argv[1]))
    except rospy.ROSInterruptException:
        pass
