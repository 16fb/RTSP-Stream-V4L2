# How RTSP Streaming on Rasp Pi Works
## Contents
* Goes through how to use V4l2 and good commands for obtaining understanding  
* For quick setup / usage of RTSP Server, skip to bottom.  

## Maybe useful links
[Good site for basic information](https://jpetazzo.github.io/2020/06/27/streaming-part-4-linux/)  
[Link to solution repo](https://github.com/mpromonet/v4l2rtspserver)  
[Guide to starting v4l2rtspserver](https://kevinsaye.wordpress.com/2018/10/17/making-a-rtsp-server-out-of-a-raspberry-pi-in-15-minutes-or-less/)  
[Wiki on V4L2](https://en.wikipedia.org/wiki/Video4Linux)   

## V4l2
Linux driver / API to handle + interface Webcams through system calls.  
Manages Webcams on Linux.  

## Useful Commands
### List Webcams 
* `v4l2-ctl --list-devices`  
Webcams will be listed as `/dev/video0`  
![list_devices](\Images\list_devices.png)

### Preview Webcam
* `ffplay /dev/video0`  
Preview Webcam using `ffmpeg`  
![ffplay_device](\Images\ffplay_device.png)

### View supported video formats
* `v4l2-ctl --list-formats`  
List video output format supported by webcam.  
YUYV -> alternative to RGB, meant for transport.  
MJPEG -> Compressed video format.  
![list_formats](\Images\list_formats.png)

### View formats, resolution list, framerates supported
* `v4l2-ctl --list-formats-ext`  
Each webcam (and capture device) advertises a full list of resolution, formats, and frame rates that it supports.  
![list_formats_ext](\Images\list_formats_ext.png)

### Query V4l2 device
* `v4l2-ctl --device /dev/video0 --all`  
Query all details about a specifc webcam device, /dev/video0

### Query Video Analogue Standard used
* `v4l2-ctl --device /dev/video0 --get-standard`  
-> in our case, no IOTL supported (System Call not supported)  

• No supported input detected - Video Standard = 0x00ffffff  
• NTSC - Video Standard = 0x000000ff  
• PAL - Video Standard = 0x000000ff  

### Query Video Inputs
* `v4l2-ctl --device /dev/video0 --get-input`  
-> some devices can have multiple

## Capture and save Video Frame
* `v4l2-ctl --get-fmt-video`  
-> Get video format

* `v4l2-ctl --set-fmt-video=width=1280,height=720,pixelformat=0`  
-> Set video format   
-> pixelformat is the numbers given when `v4l2-ctl --list-formats`  

* `v4l2-ctl --device CAPTURE_DEVICE --stream-mmap --stream-to=OUTPUT_FILE_NAME --stream-count=1`
* `v4l2-ctl --device /dev/video0 --stream-mmap --stream-to=frame.yuv --stream-count=1`
-> Capture single video frame

### Install ImageMagick Lib
* `sudo apt-get install imagemagick`  

### Convert uyvy into PNG using ImageMagick Library
* `convert -size 1280x720 -depth 8 -format YUV -sampling-factor 4:2:2 UYVY:frame.yuv -colorspace rgb frame.png`  
-> Convert to image viewable format .png  

# V4l2RTSPServer
## Installing Server
I followed this guy's guide, we use Cmake to compile on rasp pi and run server.
[Guide](https://kevinsaye.wordpress.com/2018/10/17/making-a-rtsp-server-out-of-a-raspberry-pi-in-15-minutes-or-less/)  

**Commands ran in above guide**  
* su root
* apt update && apt install git cmake
* git clone https://github.com/mpromonet/v4l2rtspserver.git
* cd v4l2rtspserver && cmake . && make && make install
* v4l2rtspserver /dev/video0 &

## Commands [Running Server]
### Run RTSP Stream
In the folder where you ran Cmake  
* `v4l2rtspserver /dev/video0`  

### Set specifc width, height, framerate
* `v4l2rtspserver -W 1280 -H 720 -F 30 /dev/video0`  
-> Other command parameters are in v4l2rtspserver Github [Here](https://github.com/mpromonet/v4l2rtspserver)  

### Viewing stream
VLC player or Python script.
