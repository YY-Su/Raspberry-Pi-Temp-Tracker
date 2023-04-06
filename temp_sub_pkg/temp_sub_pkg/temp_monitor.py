import rclpy
from rclpy.node import Node

from temp_interfaces.msg import Temperature

class TemperatureSubscriber(Node):

    def __init__(self):
        super().__init__('TemperatureMonitor')
        self.subscription = self.create_subscription(
            Temperature,
            '/temp',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('Raspberry Pi Temperature: "%s"' % msg.temperature)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = TemperatureSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
