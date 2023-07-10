"""super_mario_model.py

This script trains a model using the Proximal Policy Optimization (PPO)
algorithm on the Super Mario Bros environment. The environment is wrapped to
make it suitable for training with reinforcement learning algorithms. The
modifications to the environment include restricting the action space,
grayscaling and resizing the observations, skipping frames for faster
processing, and stacking frames for temporal difference learning.

The model is trained for a specified number of time steps, then saved for later
use.

Returns:
    None. The trained model is saved to disk.
"""

# Import necessary libraries
import os
from gym.core import ObservationWrapper
import numpy as np
from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv, VecEnvWrapper, VecFrameStack
from stable_baselines3.common.atari_wrappers import WarpFrame, MaxAndSkipEnv


# Define an environment wrapper
class GrayScaleObservation(ObservationWrapper):
    """
    Convert observations to grayscale. This reduces the dimensionality of the
    observations, speeding up training and reducing the memory footprint.
    """

    def __init__(self, env, keep_dim=False):
        """
        Initialize the wrapper.

        Args:
            env (gym.Env): The environment to wrap.
            keep_dim (bool, optional): If True, a dimension is added to the
            observations to mimic a color channel. Defaults to False.
        """
        super().__init__(env)
        self.keep_dim = keep_dim
        # self.num_envs = 1

    def reset(self):
        """
        Reset the environment.

        Returns:
            np.ndarray: The initial observation.
        """
        obs = self.env.reset()
        return self._observation(obs)

    def step_wait(self):
        """
        Execute one action.

        Args:
            action (int): The action to execute.

        Returns:
            tuple: The new observation, the reward, the done flag, and an info dictionary.
        """
        obs, reward, done, info = self.env.step()
        return self._observation(obs), reward, done, info

    def _observation(self, obs):
        """
        Convert the observation to grayscale.

        Args:
            obs (np.ndarray): The original observation.

        Returns:
            np.ndarray: The modified observation.
        """
        obs = np.dot(obs[..., :3], [0.2989, 0.5870, 0.1140])
        if self.keep_dim:
            return obs[..., None]
        else:
            return obs


# Create a wrapped environment
def create_env():
    """
    Create a wrapped Super Mario Bros environment.

    Returns:
        DummyVecEnv: The wrapped environment.
    """
    myenv = gym_super_mario_bros.make("SuperMarioBros-1-1-v3")
    myenv = JoypadSpace(myenv, SIMPLE_MOVEMENT)
    myenv = GrayScaleObservation(myenv, keep_dim=True)
    myenv = MaxAndSkipEnv(myenv, skip=4)
    myenv = WarpFrame(myenv, width=84, height=84)
    myenv = DummyVecEnv([lambda: myenv])
    myenv = VecFrameStack(myenv, n_stack=4)
    return myenv


env = create_env()

# Train the model
log_path = os.path.join("Training", "Logs")
model = PPO(
    "CnnPolicy",
    env,
    verbose=1,
    tensorboard_log=log_path,
    learning_rate=0.000001,
    n_steps=512,
)
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
    # env.render()
    if done:
        break
