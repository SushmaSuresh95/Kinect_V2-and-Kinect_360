# coding: utf-8
import datetime
import numpy as np
import time
#from time import sleep
import cv2
import sys
from pylibfreenect2 import Freenect2, SyncMultiFrameListener
from pylibfreenect2 import FrameType, Registration, Frame
from pylibfreenect2 import createConsoleLogger, setGlobalLogger
from pylibfreenect2 import LoggerLevel
#t=time.time()
import math
#import decimal
#st = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')
try:
    from pylibfreenect2 import OpenGLPacketPipeline
    pipeline = OpenGLPacketPipeline()
except:
    try:
        from pylibfreenect2 import OpenCLPacketPipeline
        pipeline = OpenCLPacketPipeline()
    except:
        from pylibfreenect2 import CpuPacketPipeline
        pipeline = CpuPacketPipeline()
print("Packet pipeline:", type(pipeline).__name__)

# Create and set logger
logger = createConsoleLogger(LoggerLevel.Debug)
setGlobalLogger(logger)

fn = Freenect2()
num_devices = fn.enumerateDevices()
if num_devices == 0:
    print("No device connected!")
    sys.exit(1)

serial = fn.getDeviceSerialNumber(0)
device = fn.openDevice(serial, pipeline=pipeline)

listener = SyncMultiFrameListener(
    FrameType.Color | FrameType.Ir | FrameType.Depth)

# Register listeners
device.setColorFrameListener(listener)
device.setIrAndDepthFrameListener(listener)

device.start()

# NOTE: must be called after device.start()
registration = Registration(device.getIrCameraParams(),
                            device.getColorCameraParams())

undistorted = Frame(512, 424, 4)
registered = Frame(512, 424, 4)

# Optinal parameters for registration
# set True if you need
need_bigdepth = False
need_color_depth_map = False

bigdepth = Frame(1920, 1082, 4) if need_bigdepth else None
color_depth_map = np.zeros((424, 512),  np.int32).ravel() \
    if need_color_depth_map else None
i=0
while True:
    frames = listener.waitForNewFrame()
    #t=time.strftime("%Y-%m-%d_%H-%M-%S")
    color = frames["color"]
    ir = frames["ir"]
    depth = frames["depth"]
    t=time.time()
    registration.apply(color, depth, undistorted, registered,
                       bigdepth=bigdepth,
                       color_depth_map=color_depth_map)

    # NOTE for visualization:
    # cv2.imshow without OpenGL backend seems to be quite slow to draw all
    # things below. Try commenting out some imshow if you don't have a fast
    # visualization backend.
    
    cv2.imshow("ir", ir.asarray() / 65535.)
    cv2.imshow("depth", depth.asarray() / 4500.)
    cv2.imshow("color", cv2.resize(color.asarray(),(int(1920 / 3), int(1080 / 3))))
    #cv2.imshow("depth_information_withcoloured", registered.asarray(np.uint8))
    cv2.imwrite("RGB/"+"RGB_"+str(i)+"_"+str(t)+".png",cv2.resize(color.asarray(),(int(1920 / 3), int(1080 / 3))))
    cv2.imwrite("DEPTH/"+"DEPTH_"+str(i)+"_"+str(t)+".png",depth.asarray() / 8.)
    cv2.imwrite("IR/"+"IR_"+str(i)+"_"+str(t)+".png",ir.asarray() / 127.)
    #cv2.imwrite("RGB_DEPTH/"+"RGB_DEPTH_"+str(time)+"_"+str(i)+".png",depth.asarray()/8,color.asarray())
    i=i+1
    if need_bigdepth:
        cv2.imshow("bigdepth", cv2.resize(bigdepth.asarray(np.float32),
                                          (int(1920 / 3), int(1082 / 3))))
    if need_color_depth_map:
        cv2.imshow("color_depth_map", color_depth_map.reshape(424, 512))
    
    listener.release(frames)
    #time.sleep(1)


    key = cv2.waitKey(delay=1)
    if key == ord('q'):
        break

device.stop()
device.close()

sys.exit(0)
