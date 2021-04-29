# How to start HTTP Stream Instead

## v4l2
Method using v4l2 by itself for MPJEG HTTP Stream.

This might not work if V4L2rtspserver is already installed.

### Read camera config and config video stream
* `v4l2-ctl --list-formats-ext`  
View info about video capture device  

* `v4l2-ctl --set-fmt-video=width=1280,height=720,pixelformat=0`  
Set video capture format, pixel format refers to format seen above  

* `v4l2-ctl --device /dev/video0 --all`
* `v4l2-ctl -c compression_quality=100,sharpness=30`
Set -c <item> <item> depending on required control params.  

### Start cvlc, start HTTPS Stream 
```
cvlc    --no-audio \
        v4l2:///dev/video0 \
        --v4l2-width 1280 \
        --v4l2-height 720 \
        --v4l2-chroma MJPG \
        --v4l2-hflip 1 \
        --v4l2-vflip 1 \
        --sout '#standard{access=http{mime=multipart/x-mixed-replace;boundary=--7b3cc56e5f51db803f790dad720ed50a},mux=mpjpeg,dst=:8554/}' \
        -I dummy
```

### Viewing Stream
Open a network stream with url `http://###.###.###.###:8554/`  


## Using V4l2rtspserver
When v4l2rtspserver is started with '-S' arguments it also give access to streams through HTTP.

[AS OF NOW, I CANNOT MAKE V4L2rtspserver work with HTTPS, refer to above method for HTTPS]

### Start stream
* `v4l2rtspserver -W 1280 -H 720 -F 30 -S1 -p 8000 -fformat mjpg /dev/video0`

**Example Urls**
RTSP      rtsp://192.168.0.10:8554/ts
HLS       http://192.168.0.10:8554/ts.m3u8
MPEG-DASH http://192.168.0.10:8554/ts.mpd

### Viewing Stream