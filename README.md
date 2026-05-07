# SOLO Dual audio streams script
This repo contains an example script to send two different audio files to two different bluetooth headphones simultaneously. It splits the audio by identifying the two devices, loading two audio files, and using Python threads to play a different audio file on each headphone. 

You can find the sample python file **split_audio_script** in the audio script folder. 

## Identifying the headphones
It is important to enter the correct names of the headphones in the script. To find out what names the headphones have on windows go to **Settings** - **Bluetooth & devices** - select the connected headphones and select **advanced sound properties**. Below “Headphones” you can see by what name the headphones are being identified (this is relevant if the headphones have the same name, i.e. "Headphones (WH-CH720N)", "Headphones (2- WH-CH720N)") - then enter the correct names in the script **names =**

```
names = ["Headphones (3- Jabra Evolve 75)", "Headphones (2- Jabra Evolve 75)"]  # Edit as needed
```

> [!IMPORTANT]
> When (re)connecting the headphones for the first time, it may first be necessary to “activate” the headphones so they are recognized by windows and can play the sound. You can go to **settings - Bluetooth & Devices -
> select the headphone - advanced sound properties - use as default for audio**. You only need to do this once after reconnecting the headphones, afterwards it doesn’t matter which headphone is set as the default.

## Audio files
The audio files need to be located in the same folder as the python script. Modify the script to enter the correct name of your audio files
```
audio1, sr1 = sf.read("rock.wav")   # First audio file (edit filename as needed)
audio2, sr2 = sf.read("piano.wav")  # Second audio file (edit filename as needed)
```
