#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty

def move_left():
    rospy.init_node('move_left', anonymous=True)
    rate = rospy.Rate(10)  # 10Hz

    cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    stop_pub = rospy.Publisher('/mobile_base/commands/reset_odometry', Empty, queue_size=1)

    # Stop the robot to reset odometry
    stop_pub.publish(Empty())
    rate.sleep()

    # Move left for 1 second
    command = input("Please press A to move left: ")
    start_time = rospy.Time.now()
    while (rospy.Time.now() - start_time).to_sec() < 1.0 and not rospy.is_shutdown() and command.lower() == "a":
        twist_cmd = Twist()
        twist_cmd.angular.z = 0.2  # Adjust the angular velocity as needed
        cmd_vel_pub.publish(twist_cmd)
        rate.sleep()

    # Stop the robot
    twist_cmd = Twist()
    cmd_vel_pub.publish(twist_cmd)

if __name__ == '__main__':
    try:
        move_left()
    except rospy.ROSInterruptException:
        pass
