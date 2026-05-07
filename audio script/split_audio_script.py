
# Import required libraries
import sounddevice as sd  # For audio playback and device management
import soundfile as sf    # For reading audio files
import threading         # For running playback in parallel threads


# Print all available audio devices with their indices and output channel info
def print_devices():
    print("Available audio devices:")
    for i, d in enumerate(sd.query_devices()):
        print(f"{i}: {d['name']} (max output: {d['max_output_channels']})")



# Find the indices of the two Bluetooth headphones by name
# Update the 'names' list to match your actual device names as shown by print_devices()
def get_headphones():
    names = ["Headphones (3- Jabra Evolve 75)", "Headphones (2- Jabra Evolve 75)"]  # Edit as needed
    devices = sd.query_devices()
    found = []
    for i, d in enumerate(devices):
        if any(name in d['name'] for name in names):
            if d['max_output_channels'] > 0:
                found.append(i)
    return found



if __name__ == "__main__":
    # Print all available audio devices for reference
    print_devices()
    try:
        # Load the two audio files to be played
        print("Loading audio files...")
        audio1, sr1 = sf.read("rock.wav")   # First audio file (edit filename as needed)
        audio2, sr2 = sf.read("piano.wav")  # Second audio file (edit filename as needed)
        print(f"Loaded piano.wav (sr={sr1}, shape={audio1.shape})")
        print(f"Loaded rock.wav (sr={sr2}, shape={audio2.shape})")
    except Exception as e:
        print(f"Error loading audio files: {e}")
        exit(1)

    # Find the two Bluetooth headphone devices by name
    devices = get_headphones()
    print(f"Found matching devices: {devices}")
    if len(devices) < 2:
        print("Error: Less than two matching headphone devices found. Check device names above.")
        exit(1)
    device1, device2 = devices[0], devices[1]

    # Define a function to play audio on a specific device in a separate thread
    def play(data, sr, dev, label):
        print(f"Playing on device {dev} ({label})...")
        try:
            sd.play(data, samplerate=sr, device=dev, blocking=True)
            print(f"Done playing on device {dev} ({label})")
        except Exception as e:
            print(f"Error playing on device {dev} ({label}): {e}")

    # Start two threads to play both audio files simultaneously on different headphones
    t1 = threading.Thread(target=play, args=(audio1, sr1, device1, "Headphone 1"))
    t2 = threading.Thread(target=play, args=(audio2, sr2, device2, "Headphone 2"))

    t1.start()
    t2.start()
    # Wait for both threads to finish
    t1.join()
    t2.join()
    print("Finished playing both audio files.")