

import rclpy
from rclpy.node import Node

from sensor_msgs.msg import LaserScan
import time

from nav_msgs.msg import Odometry
import math

from std_msgs.msg import String


class HealthMonitor(Node):

    def __init__(self):
        super().__init__('health_monitor')

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10
        )

        self.last_scan_time = None
        self.scan_frequency = 0.0
        
        self.odom_sub = self.create_subscription(
             Odometry,
             '/odom',
             self.odom_callback,
             10
        )

        self.current_speed = 0.0
        self.total_distance = 0.0
        self.last_position = None  

        
        self.status_pub = self.create_publisher(
           String,
           '/robot_status',
           10
        )

        self.timer = self.create_timer(
            1.0,
            self.timer_callback
        )

    def scan_callback(self, msg):
        now = time.time()

        if self.last_scan_time is not None:
            dt = now - self.last_scan_time

            if dt > 0:
                self.scan_frequency = 1.0 / dt

        self.last_scan_time = now

    def odom_callback(self, msg):

       self.current_speed = math.sqrt(
          msg.twist.twist.linear.x**2 +
          msg.twist.twist.linear.y**2
       )

       x = msg.pose.pose.position.x
       y = msg.pose.pose.position.y

       if self.last_position is not None:

           dx = x - self.last_position[0]
           dy = y - self.last_position[1]

           self.total_distance += math.sqrt(
               dx**2 + dy**2
           )

       self.last_position = (x, y)

    
    def timer_callback(self):

        self.get_logger().info(
            f'LiDAR: {self.scan_frequency:.2f} Hz | '
            f'Speed: {self.current_speed:.2f} m/s | '
            f'Distance: {self.total_distance:.2f} m'
         )

     

def main(args=None):
    rclpy.init(args=args)

    node = HealthMonitor()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
