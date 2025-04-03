import cv2
def read_video(video_path):
    cap=cv2.VideoCapture(video_path)
    frames=[]
    while True:
        ret,frame=cap.read()
        if not ret:
            break
        frames.append(frame)
    return frames

def save_video(output_video_frames,output_video_path):
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Use a codec (e.g., XVID, MJPG, MP4V)
    fps = 24  # Frames per second
    frame_size = (output_video_frames[0].shape[1], output_video_frames[0].shape[0])  # (width, height)

    out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size, isColor=True)
    for frame in output_video_frames:
        out.write(frame)
    out.release()
