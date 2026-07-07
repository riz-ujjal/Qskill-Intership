import pyaudio

# Initialize PyAudio
p = pyaudio.PyAudio()

# Loop through all available audio devices
for i in range(p.get_device_count()):
    device_info = p.get_device_info_by_index(i)
    # Print the index number and the name of the device
    print(f"Index {i}: {device_info['name']}")

# Clean up the PyAudio object
p.terminate()