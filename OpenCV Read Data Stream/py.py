# Display stream input and frame information
# 'q' to exit
import cv2

#cap = cv2.VideoCapture('rtsp://192.168.137.213:8554/unicast') # Rasp Pi RTSP Stream when on my HotSpot network
cap = cv2.VideoCapture('rtsp://192.168.0.10:8554/unicast') # Rasp Pi RTSP Stream
#cap = cv2.VideoCapture('https://192.168.137.213:8554/')    # Rasp Pi HTTPS Stream
#cap = cv2.VideoCapture('rtsp://service:Aiot1483!@192.168.1.161') # AI Camera


cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)


while True:
  ret, frame = cap.read()
  cv2.imshow('Video', frame)

  # https://stackoverflow.com/questions/63256300/how-do-i-get-usb-webcam-property-ids-for-opencv/63265171#63265171
  # Get info about frame
  width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # 3
  height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # 4
  fps = cap.get(cv2.CAP_PROP_FPS)  # 5
  frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)  # 7

  print('width, height:', width, height)
  print('fps:', fps)
  print('frames count:', frame_count) 

  # frames count: -2562047788015215.0
  # width, height: 1280.0 720.0
  # fps: 25.0

  if cv2.waitKey(1) & 0xFF == ord('q'):
    exit(0)