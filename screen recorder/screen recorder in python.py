import pyautogui
import cv2
import numpy as np
import os
import time

# Specify resolution
resolution = (1920, 1080)

# Specify video codec
codec = cv2.VideoWriter_fourcc(*"XVID")

# prompt user for the fps fo the video
fps = 10

# Prompt user for the duration of the video
duration = int(input("Enter the duration of the video in seconds: "))

# Calculate the total number of frames based on the duration and frame rate
total_frames = int(fps * duration)

# Specify the filename and output path
filename = "Recording.mp4v"
output_directory = "S:\Vs codes\projects\python\screen recorder\output"
output_file = os.path.join(output_directory, filename)

# Create the output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Creating a VideoWriter object
out = cv2.VideoWriter(output_file, codec, fps, resolution)

# Create an Empty window
cv2.namedWindow(filename, cv2.WINDOW_NORMAL)

# Resize the window
cv2.resizeWindow(filename, 480, 270)

# Start time for recording
start_time = time.time()

# Recording loop
frame_count = 0
while frame_count < total_frames:
    # Take screenshot using PyAutoGUI
    img = pyautogui.screenshot()

    # Convert the screenshot to a numpy array
    frame = np.array(img)

    # Convert it from BGR(Blue, Green, Red) to RGB(Red, Green, Blue)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Write the frame to the output file
    out.write(frame)

    # Optional: Display the recording screen
    cv2.imshow(filename, frame)

    # Increment frame count
    frame_count += 1

    # Check if the 'q' key is pressed to stop recording
    if cv2.waitKey(1) == ord('q'):
        break

    # Check if the desired duration is reached
    if time.time() - start_time >= duration:
        break

# Release the VideoWriter
out.release()

# Destroy all windows
cv2.destroyAllWindows()

# Open the output video file
os.startfile(output_file)