
import sys
freqDict = {
    1: 349.228,  # F4
    2: 369.994,  # F#4
    3: 391.995,  # G4
    4: 415.305,  # Ab4
    5: 440.0,   # A4
    6: 466.164,  # Bb4
    7: 493.883,  # B4
    8: 523.251,  # C5
    9: 554.365,  # C#5
    10: 587.330,  # D55
    11: 622.254,  # D#5
    12: 659.255,  # E5
    13: 698.456,  # F5
    14: 739.989,  # F#5
    15: 783.991,  # G5
    16: 830.609,  # Ab5
    17: 880.000,  # A5
    18: 932.328,  # Bb5
    19: 1046.50,  # C6
    20: 1108.73,  # C#6
    21: 1174.66,  # D6
    22: 1244.51,  # D#6
    23: 1318.51,  # E6
    24: 1396.91  # F6
}


def makeWave(freq):
    import math  # import needed modules
    import pyaudio  # sudo apt-get install python-pyaudio

    PyAudio = pyaudio.PyAudio  # initialize pyaudio

    # See https://en.wikipedia.org/wiki/Bit_rate#Audio
    BITRATE = 16000  # number of frames per second/frameset.

    FREQUENCY = freq  # Hz, waves per second, 261.63=C4-note.
    LENGTH = 0.5  # seconds to play sound

    if FREQUENCY > BITRATE:
        BITRATE = FREQUENCY+100

    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE
    WAVEDATA = ''

    # generating wawes
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA + \
            chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))

    for x in range(RESTFRAMES):
        WAVEDATA = WAVEDATA+chr(128)

    p = PyAudio()
    stream = p.open(format=p.get_format_from_width(1),
                    channels=1,
                    rate=BITRATE,
                    output=True)

    stream.write(WAVEDATA)
    stream.stop_stream()
    stream.close()
    p.terminate()


def lick(key):
    if key == "F":
        key = 13
    if key == "F#" or key == "Gb":
        key = 14
    if key == "G":
        key = 15
    if key == "G#" or key == "Ab":
        key = 4
    if key == "A":
        key = 5
    if key == "A#" or key == "Bb":
        key = 6
    if key == "B":
        key = 7
    if key == "C":
        key = 8
    if key == "C#" or key == "Db":
        key = 9
    if key == "D":
        key = 10
    if key == "D#" or key == "Eb":
        key = 11
    if key == "E":
        key = 12

    theLick = []
    a = freqDict[key]
    b = freqDict[key + 2]
    c = freqDict[key + 3]
    d = freqDict[key + 5]
    e = freqDict[key + 2]
    f = freqDict[key - 2]
    g = freqDict[key]
    theLick.append(a)
    theLick.append(b)
    theLick.append(c)
    theLick.append(d)
    theLick.append(e)
    theLick.append(f)
    theLick.append(g)
    print(theLick)

    for note in theLick:
        makeWave(note)


if __name__ == "__main__":
    key = sys.argv[1]
    lick(key)
