import pygame, time
import glob, random


def play_rand_wav(file_list):
    pygame.mixer.pre_init(frequency=32000, size=-16, channels=2, buffer=4096)
    pygame.init()
    pygame.mixer.Sound(random.choice(file_list)).play()
    time.sleep(0.5)

def navi_sound():
    play_rand_wav(glob.glob("sound/*.wav"))
    return "YES"

if __name__ == "__main__":
    navi_sound()

