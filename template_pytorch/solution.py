#!/usr/bin/env python3


import numpy as np

from aido_schemas import EpisodeStart, protocol_agent_duckiebot1, PWMCommands, Duckiebot1Commands, LEDSCommands, RGB, \
    wrap_direct, Context, Duckiebot1Observations, JPGImage, logger

try:
    from model import DDPG
except:
    import sys
    print("""Importing 'model' from 'DDPG' failed. If you are currently building this template for the JetsonNano (
template-pytorch), worry not: the JN is finicky, and we're actually going to install torch and torchvision soon
. \n\n\nIf you are trying to submit your solution, do worry, and contact a maintainer!\n\n\n""", file=sys.stderr)

from wrappers import DTPytorchWrapper
from PIL import Image
import io

try:
    import torch    # Hacks are fun
except:
    # Hack time: basically, CUDA doesn't really support ARM64. It does support the Jetson, though.
    #
    # So the way to access CUDA inside a docker is to import and -v a bunch of files that CUDA requires - tricking the
    # docker into thinking it does have CUDA installed.
    #
    # But docker build doesn't support -v args... and torchvision requires CUDA during the intall phase... So we have to
    # build a fake base image, then run this script once, which imports torch if it's not already importable, and then
    # we have to commit the changes to the docker.
    import os
    from contextlib import contextmanager
    import os
    import subprocess
    from subprocess import *
    @contextmanager
    def chdir(newdir):
        # https://stackoverflow.com/questions/431684/how-do-i-change-the-working-directory-in-python
        prevdir = os.getcwd()
        os.chdir(os.path.expanduser(newdir))
        try:
            yield
        finally:
            os.chdir(prevdir)

    def call(cmd):
        return subprocess.run(cmd, stdout=sys.stdout, stderr=sys.stderr, shell=True, universal_newlines=True)

    os.mkdir("./torch_build_dir")
    with chdir("./torch_build_dir"):
        # Install torchvision
        call("""
wget https://github.com/pytorch/vision/archive/v0.6.0.zip -O torchvision.zip && unzip torchvision.zip
""")
        with chdir("vision-0.6.0"):
            call("python3 setup.py install")

    #print("Successfully installed torch and torchvision. Please commit these changes to the docker. Exiting now...")
    exit(0)

class PytorchRLTemplateAgent:
    def __init__(self, load_model=False, model_path=None):
        logger.info('PytorchRLTemplateAgent init')
        self.preprocessor = DTPytorchWrapper()

        self.model = DDPG(state_dim=self.preprocessor.shape, action_dim=2, max_action=1, net_type="cnn")
        self.current_image = np.zeros((640, 480, 3))

        if load_model:
            logger.info('PytorchRLTemplateAgent loading models')
            fp = model_path if model_path else "model"
            self.model.load(fp, "models", for_inference=True)
        logger.info('PytorchRLTemplateAgent init complete')

    def init(self, context: Context):
        context.info('init()')

    def on_received_seed(self, data: int):
        np.random.seed(data)

    def on_received_episode_start(self, context: Context, data: EpisodeStart):
        context.info(f'Starting episode "{data.episode_name}".')

    def on_received_observations(self, data: Duckiebot1Observations):
        camera: JPGImage = data.camera
        obs = jpg2rgb(camera.jpg_data)
        self.current_image = self.preprocessor.preprocess(obs)

    def compute_action(self, observation):
        #if observation.shape != self.preprocessor.transposed_shape:
        #    observation = self.preprocessor.preprocess(observation)
        action = self.model.predict(observation)
        return action.astype(float)

    def on_received_get_commands(self, context: Context):
        pwm_left, pwm_right = self.compute_action(self.current_image)

        pwm_left = float(np.clip(pwm_left, -1, +1))
        pwm_right = float(np.clip(pwm_right, -1, +1))

        grey = RGB(0.0, 0.0, 0.0)
        led_commands = LEDSCommands(grey, grey, grey, grey, grey)
        pwm_commands = PWMCommands(motor_left=pwm_left, motor_right=pwm_right)
        commands = Duckiebot1Commands(pwm_commands, led_commands)
        context.write('commands', commands)

    def finish(self, context: Context):
        context.info('finish()')


def jpg2rgb(image_data: bytes) -> np.ndarray:
    """ Reads JPG bytes as RGB"""
    im = Image.open(io.BytesIO(image_data))
    im = im.convert('RGB')
    data = np.array(im)
    assert data.ndim == 3
    assert data.dtype == np.uint8
    return data

def main():
    node = PytorchRLTemplateAgent() 
    protocol = protocol_agent_duckiebot1
    wrap_direct(node=node, protocol=protocol)


if __name__ == '__main__':
    main()
