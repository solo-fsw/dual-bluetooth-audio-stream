import sounddevice as sd
import soundfile as sf
import threading

def print_devices():
    print("Available audio devices:")
    for i, d in enumerate(sd.query_devices()):
        print(f"{i}: {d['name']} (max output: {d['max_output_channels']})") 


# 1. Find devices
def get_headphones():
    names = ["Headphones (3- Jabra Evolve 75)", "Headphones (2- Jabra Evolve 75)"] # needs to be adapted to your headphone names, 
    #either in microsoft or macos settings or running sd.query_devices() to find the correct names 
    devices = sd.query_devices()
    found = []
    for i, d in enumerate(devices):
        if any(name in d['name'] for name in names):
            if d['max_output_channels'] > 0:
                found.append(i)
    return found


if __name__ == "__main__":
    print_devices()
    try:
        # 2. Load audio
        print("Loading audio files...")
        audio1, sr1 = sf.read("rock.wav")
        audio2, sr2 = sf.read("piano.wav")
        print(f"Loaded piano.wav (sr={sr1}, shape={audio1.shape})")
        print(f"Loaded rock.wav (sr={sr2}, shape={audio2.shape})")
    except Exception as e:
        print(f"Error loading audio files: {e}")
        exit(1)


    # 3. Get devices
    devices = get_headphones()
    print(f"Found matching devices: {devices}")
    if len(devices) < 2:
        print("Error: Less than two matching headphone devices found. Check device names above.")
        exit(1)
    device1, device2 = devices[0], devices[1]


    # 4. Play simultaneously
    def play(data, sr, dev, label):
        print(f"Playing on device {dev} ({label})...")
        try:
            sd.play(data, samplerate=sr, device=dev, blocking=True)
            print(f"Done playing on device {dev} ({label})")
        except Exception as e:
            print(f"Error playing on device {dev} ({label}): {e}")

    t1 = threading.Thread(target=play, args=(audio1, sr1, device1, "Headphone 1"))
    t2 = threading.Thread(target=play, args=(audio2, sr2, device2, "Headphone 2"))

    t1.start()
    t2.start()
    t1.join()
    t2.join()