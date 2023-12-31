#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from pynput import keyboard

class TurtleBotController:
    def __init__(self):
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        self.twist_cmd = Twist()

    def on_key_press(self, key):
        try:
            if key == keyboard.Key.up:
                self.twist_cmd.linear.x = 0.2
            elif key == keyboard.Key.down:
                self.twist_cmd.linear.x = -0.2
            elif key == keyboard.Key.left:
                self.twist_cmd.angular.z = 0.2
            elif key == keyboard.Key.right:
                self.twist_cmd.angular.z = -0.2
        except Exception as e:
            print(f"Error in on_key_press: {e}")

    def on_key_release(self, key):
        try:
            if key in [keyboard.Key.up, keyboard.Key.down]:
                self.twist_cmd.linear.x = 0.0
            elif key in [keyboard.Key.left, keyboard.Key.right]:
                self.twist_cmd.angular.z = 0.0
        except Exception as e:
            print(f"Error in on_key_release: {e}")

    def start_controller(self):
        with keyboard.Listener(on_press=self.on_key_press, on_release=self.on_key_release) as listener:
            rospy.init_node('turtlebot_controller', anonymous=True)
            rate = rospy.Rate(10)  # 10Hz
            while not rospy.is_shutdown():
                self.cmd_vel_pub.publish(self.twist_cmd)
                rate.sleep()

if __name__ == '__main__':
    try:
        controller = TurtleBotController()
        controller.start_controller()
    except rospy.ROSInterruptException:
        pass
    except Exception as e:
        print(f"Error: {e}")
