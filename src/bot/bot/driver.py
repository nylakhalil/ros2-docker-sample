import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Driver(Node):
    def __init__(self):
        super().__init__('driver')
        self.sub = self.create_subscription(String, 'chatter', self.chatter_callback, 10)
        self.get_logger().info('Driver Started')

    def chatter_callback(self, msg):
        self.get_logger().info('Driver Received: [%s]' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = Driver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    