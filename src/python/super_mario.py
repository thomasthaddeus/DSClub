"""super_mario_model.py

This script trains a model using the Proximal Policy Optimization (PPO)
algorithm on the Super Mario Bros environment.

The environment is wrapped to make it suitable for training with reinforcement
learning algorithms. The modifications to the environment include restricting
the action space, grayscaling and resizing the observations, skipping frames
for faster processing, and stacking frames for temporal difference learning.
The model is trained for a specified number of time steps, then saved for later
use.

Returns:
    None. The trained model is saved to disk.
"""

# Import necessary libraries
import os
import numpy as np
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecFrameStack
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.vec_env import VecEnv, VecEnvWrapper
from stable_baselines3.common.atari_wrappers import WarpFrame, MaxAndSkipEnv
from matplotlib import pyplot as plt

# Define an environment wrapper
class GrayScaleObservation(VecEnvWrapper):
    """
    GrayScaleObservation _summary_

    _extended_summary_

    Args:
        VecEnvWrapper (_type_): _description_
    """

    def __init__(self, venv, keep_dim=False):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            venv (_type_): _description_
            keep_dim (bool, optional): _description_. Defaults to False.
        """
        super().__init__(venv)
        self.keep_dim = keep_dim

    def reset(self):
        """
        reset _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        obs = self.venv.reset()
        return self.observation(obs)

    def step_wait(self):
        """
        step_wait _summary_

        _extended_summary_

        Returns:
            _type_: _description_
        """
        obs, reward, done, info = self.venv.step_wait()
        return self.observation(obs), reward, done, info

    def observation(self, obs):
        """
        observation _summary_

        _extended_summary_

        Args:
            obs (_type_): _description_

        Returns:
            _type_: _description_
        """
        obs = np.dot(obs[..., :3], [0.2989, 0.5870, 0.1140])
        if self.keep_dim:
            return obs[..., None]
        else:
            return obs

# Create a wrapped environment
def create_env():
    """
    create_env _summary_

    _extended_summary_

    Returns:
        _type_: _description_
    """
    env = gym_super_mario_bros.make('SuperMarioBros-1-1-v0')
    env = JoypadSpace(env, SIMPLE_MOVEMENT)
    env = GrayScaleObservation(env, keep_dim=True)
    env = MaxAndSkipEnv(env, skip=4)
    env = WarpFrame(env, width=84, height=84)
    env = DummyVecEnv([lambda: env])
    env = VecFrameStack(env, n_stack=4)
    return env

env = create_env()

# Train the model
log_path = os.path.join("Training", "Logs")
model = PPO("CnnPolicy", env, verbose=1, tensorboard_log=log_path, learning_rate=0.000001, n_steps=512)
model.learn(total_timesteps=10000)

# Save the model
model.save("mario_model_10000")

# Load the model
model = PPO.load("mario_model_10000")

# Test the model
state = env.reset()
while True:
    actions, _ = model.predict(state)
    state, reward, done, info = env.step(actions)
    env.render()
    if done:
        break
