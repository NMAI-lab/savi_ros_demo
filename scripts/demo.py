#!/usr/bin/env python

# Created on Wed Feb 19 16:17:21 2020
# @author: Patrick Gavigan

import rospy
import threading
from std_msgs.msg import String

def syncPrint(message, sem):
    sem.acquire()
    rospy.loginfo(message)
    sem.release()

def perceptionHandler(consoleSemaphore):
    syncPrint("Perception handler launched.", consoleSemaphore)

    pub = rospy.Publisher('perceptions', String, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        message = "time(%s)" % rospy.get_time()
        syncPrint("I said: " + message, consoleSemaphore)
        pub.publish(message)
        rate.sleep()

def actionReceiver(data, consoleSemaphore): 
    message = str(rospy.get_caller_id() + 'I heard: ' + str(data.data))
    syncPrint(message, consoleSemaphore)

def actionHandler(consoleSemaphore):
    syncPrint("Action handler launched", consoleSemaphore)
    rospy.Subscriber('actions', String, actionReceiver, consoleSemaphore)
    rospy.spin()

def outboxReceiver(data, consoleSemaphore): 
    message = str(rospy.get_caller_id() + 'I heard: ' + str(data.data))
    syncPrint(message, consoleSemaphore)

def outboxHandler(consoleSemaphore):
    syncPrint("Outbox handler launched", consoleSemaphore)
    rospy.Subscriber('outbox', String, outboxReceiver, consoleSemaphore)
    rospy.spin()
    
def inboxHandler(consoleSemaphore):
    syncPrint("Inbox handler launched.", consoleSemaphore)

    pub = rospy.Publisher('inbox', String, queue_size=10)
    rate = rospy.Rate(1) # 1hz
    while not rospy.is_shutdown():
        message = ""<"%s,2,tell,0,anotherTime(%s)" % rospy.get_time()
        syncPrint("I said: " + message, consoleSemaphore)
        pub.publish(message)
        rate.sleep()

def demo():
    rospy.init_node('demoSaviTranslator', anonymous=True)
    consoleSemaphore = threading.Semaphore()
    
    perceptionThread = threading.Thread(target=perceptionHandler, args=(consoleSemaphore,))
    perceptionThread.start()
    
    actionThread = threading.Thread(target=actionHandler, args=(consoleSemaphore,))
    actionThread.start()
    

if __name__ == '__main__':
    try:
        demo()
    except rospy.ROSInterruptException:
        pass
