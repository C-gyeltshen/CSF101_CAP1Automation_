# this python code gets inside a foledr and playes video only 

import cv2
import os
import time

# Path to the folder containing your video files
video_folder = '/Users/chimigyeltshen/Desktop/practice/video'

# List all video files in the folder (assuming they have common video extensions like .mp4, .avi, etc.)
video_files = [f for f in os.listdir(video_folder) if f.endswith(('.mp4', '.avi', '.mkv'))]

print('video files: ', video_files)

def play_video(video_path):
    # Play using opencv
    cap = cv2.VideoCapture(video_path)
        
    # Check if the video opened successfully
    if not cap.isOpened():
        print(f"Could not open video: {video_path}")
        exit()
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # End of video
        
        # Display the frame
        cv2.imshow('Video Player', frame)
        
        # Check for user input to exit the video playback
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # cv2.destroyWindow()
    # Release the video capture object
    cap.release()
    # Close all video windows
    cv2.destroyAllWindows()


# Check if there are any video files in the folder
if not video_files:
    print("No video files found in the folder.")
else:
    for video_file in video_files:
        print(video_file)
        video_path = os.path.join(video_folder, video_file)
        print(video_path)
        play_video(video_path)
        time.sleep(2)
    
        


 