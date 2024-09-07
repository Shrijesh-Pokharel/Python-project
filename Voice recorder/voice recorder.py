import sounddevice as sd
from scipy.io.wavfile import write
import os
import time

freq = 4410
duration = int(input("Enter the duration you want: "))

print("Recording started....")
time.sleep(1)
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)
sd.wait()

current_directory = os.getcwd()
print({'Current Directory': current_directory})

target_directory = "S:\Vs codes\projects\python\Voice recorder\output"
os.makedirs(target_directory, exist_ok=True)

output_file = os.path.join(target_directory, "Recording.wav")

if os.path.exists(output_file):
    print("File already exists. Overwriting...")
    time.sleep(1)
    os.remove(output_file)

write(os.path.join(current_directory, "Recording.wav"), freq, recording)
os.rename(os.path.join(current_directory, "Recording.wav"), output_file)

print("Files moved successfully.")
time.sleep(1)
print("Opening output directory...")
time.sleep(1)
os.startfile(output_file)
