#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from temp_interfaces.msg import Temperature
from gpiozero import CPUTemperature

class TempNode(Node):
    def __init__(self):
        # Call super()
        super().__init__("TemperatureDriver")
        self.pub_ = self.create_publisher(Temperature, "/temp", 10)

        self.get_logger().info("Temperature publisher has been started.")
        self.mod_timer_ = self.create_timer(1, self.publish_temp)

    def publish_temp(self):
        msg = Temperature()
        msg.temperature = CPUTemperature().temperature
        self.get_logger().info('Raspberry Pi Temperature: "%s"' % msg.temperature)
        self.pub_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TempNode()
    rclpy.spin(node)
    rclpy.shutdown()
