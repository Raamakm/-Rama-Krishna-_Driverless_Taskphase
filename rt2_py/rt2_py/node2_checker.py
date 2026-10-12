import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, String
from rt2_msgs.msg import RT2String


class PalindromeChecker(Node):
    def __init__(self):
        super().__init__('palindrome_checker')
        self.create_subscription(RT2String, '/rt2_string', self.string_cb, 10)
        self.flag_pub = self.create_publisher(Int32, '/palindrome_flag', 10)
        self.create_subscription(String, '/palindrome_reply', self.reply_cb, 10)

    def string_cb(self, msg):
        s = msg.data
        flag = Int32()
        flag.data = 1 if s == s[::-1] else 0
        self.flag_pub.publish(flag)
        self.get_logger().info(f'Received "{s}" -> sent flag {flag.data} to Node 3')

    def reply_cb(self, msg):
        self.get_logger().info(f'Node 3 says: {msg.data}')


def main(args=None):
    rclpy.init(args=args)
    node = PalindromeChecker()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
