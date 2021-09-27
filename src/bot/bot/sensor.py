import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class Sensor(Node):
    def __init__(self):
        super().__init__('sensor')
        self.i = 0
        self.pub = self.create_publisher(String, 'chatter', 10)
        timer_period = 1.0
        self.tmr = self.create_timer(timer_period, self.timer_callback)
        self.get_logger().info('Sensor Started')


    def timer_callback(self):
        msg = String()
        msg.data = 'Sensor Data: {0}'.format(self.i)
        self.i += 1
        self.get_logger().info('Publishing: "{0}"'.format(msg.data))
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = Sensor()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
    