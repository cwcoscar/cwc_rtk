#!/usr/bin/python
import serial
import signal
import rospy
from rtcm_msgs.msg import Message

# flag = 1

def callbackrtcm(data):
    correction = data.message
    # a  = [int(string.encode('hex'),16) for string in correction]
    # print("length : " + str(len(correction)))
    # print(a)
    # print("------------------------------")
    GPS.write(correction)

# def signal_handler(sig, frame):
#     print("press control C")
#     global flag 
#     flag = 0
#     GPS.close()


if __name__ == '__main__':
    rospy.init_node('receiving_rtk')

    sub_rtcm = rospy.Subscriber('/rtcm', Message, callbackrtcm)

    serial_port = rospy.get_param('~port','/dev/ttyACM0')
    serial_baud = rospy.get_param('~baud',9600) 	
    GPS = serial.Serial(port=serial_port, baudrate=serial_baud, timeout=2, rtscts=True, dsrdtr=True)

    try:
        # while not rospy.is_shutdown():
            # print("")
            # signal.signal(signal.SIGINT, signal_handler)
            rospy.spin()
    except rospy.ROSInterruptException:
        GPS.close()
