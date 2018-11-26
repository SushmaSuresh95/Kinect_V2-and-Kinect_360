**Kinect_360.py = Contains RGB, Depth and IR Parallel Image Captures**

**Depth_Kinect_v2 and IR_Kinect_v2 = Kinect V2**

**A) Refer the Links below for Kinect_v2**
  
  	https://rjw57.github.io/freenect2-python/

**B) Installation steps for Kinect_360**

**1)  Open a terminal and run the following commands**
        
        $sudo apt-get update
        
        $sudo apt-get upgrade
**2) Install the necessary dependencies**
        
        $sudo apt-get install git-core cmake freeglut3-dev pkg-config build-essential libxmu-dev libxi-dev libusb-1.0-0-dev
        
**3) Clone the libfreenect repository to your system**
        
        $git clone git://github.com/OpenKinect/libfreenect.git
	
**4) Install libfreenect**

        cd libfreenect
        mkdir build
        cd build
        cmake -L ..
        make
        sudo make install
        sudo ldconfig /usr/local/lib64/

**5) Also make a file with rules for the Linux device manager**

        sudo nano /etc/udev/rules.d/51-kinect.rules

Then paste the following and save
        
        # ATTR{product}=="Xbox NUI Motor"
        SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02b0", MODE="0666"
        # ATTR{product}=="Xbox NUI Audio"
        SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ad", MODE="0666"
        # ATTR{product}=="Xbox NUI Camera"
        SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02ae", MODE="0666"
        # ATTR{product}=="Xbox NUI Motor"
        SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02c2", MODE="0666"
        # ATTR{product}=="Xbox NUI Motor"
        SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02be", MODE="0666"
        # ATTR{product}=="Xbox NUI Motor"
        SUBSYSTEM=="usb", ATTR{idVendor}=="045e", ATTR{idProduct}=="02bf", MODE="0666"

**6) In order to use the Kinect with opencv and python, the python wrappers for libfreenct need to be installed. Before doing that, install the necessary dependencies**

        $sudo apt-get install cython
        $sudo apt-get install python-dev
        $sudo apt-get install python-numpy
        
 **7) Go to the directory ……./libfreenect/wrappers/python and run the following command**
 
        $sudo python setup.py install
 
        
