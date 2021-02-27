import cv2
file_path = "test.mp4"
vidcap = cv2.VideoCapture(file_path)
video_frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Video frames = ", video_frames)
success, image = vidcap.read()
count = 0
while success:
    cv2.imwrite("output/frame%d.png" %count, image)
    success, image = vidcap.read()
    print("|{}/{}|".format(count+1, video_frames))
    count += 1
print("All done :)")