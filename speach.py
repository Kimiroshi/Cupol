import random
import pyaudio
import wave

chunk = 1024

ok = ['sounds/ok1.wav', 'sounds/ok2.wav', 'sounds/ok3.wav']
greet = ['sounds/greet1.wav', 'sounds/greet2.wav', 'sounds/greet3.wav']


def play(file):
    f = wave.open(file, "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)
    stream.stop_stream()
    stream.close()
    p.terminate()


def random_ok():
    play(random.choice(ok))


def random_greet():
    play(random.choice(greet))


def off():
    play('sounds/off.wav')


def not_found():
    play('sounds/not_found.wav')


def ready():
    play('sounds/ready.wav')