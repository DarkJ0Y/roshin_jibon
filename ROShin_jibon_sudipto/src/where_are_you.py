#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Odometry

def callback(data):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z

    command = input("Do you want to know the position(y/n):")

    if command.lower()=="y":

        rospy.loginfo(f"TurtleBot3 Position: x={x}, y={y}, z={z}")

def get_turtlebot_position():
    rospy.init_node('turtlebot_position_listener', anonymous=True)
    rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

if __name__ == '__main__':
    get_turtlebot_position()
