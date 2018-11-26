# Library to display images
from PIL.ImageMath import eval as im_eval
# Library for kinect v2
from freenect2 import Device, FrameType

#To activate the Kinect Device which is defined in Freenect2
device = Device()
with device.running():
    for frame_type, frame in device:
        if frame_type is FrameType.Depth:
            # Convert range of depth image to 0->255 (8 Bit resolution)
            norm_im = im_eval('convert(I / 8, "L")', I=frame.to_image())
            norm_im.save('depth_Kinect_V2.jpg')
            break
