import pygame
from random import randint


class SoundArchive(object):

    instance = None

    @classmethod
    def set_instance(cls, state):
        cls.instance = cls(state)

    @classmethod
    def get_instance(cls):

        if cls.instance is None:
            raise Exception('Sound not initialized yet')

        return cls.instance

    def __init__(self, state):

        self.state = state

        pygame.mixer.pre_init(44100, -16, 2, 1024)
        pygame.mixer.init()

        self.sounds = {}

        self.load_sounds('step1', 'step2', 'step3')

        self.running = False
        self.stepped = 0

    def run(self):

        if self.running:
            # TODO check if key still held down
            # if not, switch off running and kill step sounds
            pass
            if not self.state.player_controller.holding:
                self.stop_steps()
                self.running = False
                self.stepped = 4
        else:
            self.stepped = 0

        if self.stepped > 0:
            self.stepped -= 1

    def load_sounds(self, *args):

        for key in args:
            if key not in self.sounds:
                self.sounds[key] = pygame.mixer.Sound('assets/sounds/' + key + '.wav')
                self.sounds[key].set_volume(.1)

    def play_sound(self, key):

        if key not in self.sounds:
            self.sounds[key] = pygame.mixer.Sound('assets/sounds/' + key + '.wav')

        self.sounds[key].play()

    def play_step(self):

        # TODO check if many steps played in quick succession, use scurry sound if so

        self.stop_steps()
        self.play_sound('step'+str(randint(1, 3)))

        self.stepped += 7
        if self.stepped > 10:
            self.running = True

    def play_door(self):

        self.play_sound('door')
        pygame.time.delay(80)

    def stop_steps(self):
        self.sounds['step1'].stop()
        self.sounds['step2'].stop()
        self.sounds['step3'].stop()
