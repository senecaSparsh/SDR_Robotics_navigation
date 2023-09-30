#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def navigate():
    rospy.init_node('simple_navigation', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz

    # Define navigation logic here
    while not rospy.is_shutdown():
        cmd_vel = Twist()
        cmd_vel.linear.x = 0.2  # Adjust speed as needed
        cmd_vel.angular.z = 0.0  # Adjust angular velocity as needed
        pub.publish(cmd_vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        navigate()
    except rospy.ROSInterruptException:
        pass
