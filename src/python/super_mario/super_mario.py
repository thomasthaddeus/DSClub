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


class SuperMarioTrainer:
    """
    SuperMarioTrainer is a class for creating, training, and testing a 
    reinforcement learning model on the Super Mario Bros environment using the 
    Proximal Policy Optimization (PPO) algorithm.

    This class encapsulates the functionality for environment setup, model 
    training, saving, and testing in the Super Mario Bros game.
    """

    class GrayScaleObservation(VecEnvWrapper):
        """
        GrayScaleObservation wraps a vectorized environment to convert 
        observations to grayscale.

        This wrapper converts the RGB images to grayscale images, which can be 
        more efficient for training certain types of models. Optionally, it can 
        retain the last dimension (to keep the shape as WxHx1 instead of WxH).

        Args:
            VecEnvWrapper (VecEnv): A vectorized environment to wrap.
            keep_dim (bool, optional): Whether to keep the last dimension after
            grayscaling. Defaults to False.
        """

        def __init__(self, venv, keep_dim=False):
            super().__init__(venv)
            self.keep_dim = keep_dim
            # More initialization code can be added here if necessary

        def reset(self):
            obs = self.venv.reset()
            return self.observation(obs)

        def step_wait(self):
            obs, reward, done, info = self.venv.step_wait()
            return self.observation(obs), reward, done, info

        def observation(self, obs):
            """
            Converts the observation from RGB to grayscale.

            Args:
                obs (ndarray): Original observation in RGB format.

            Returns:
                ndarray: Grayscale observation.
            """
            obs = np.dot(obs[..., :3], [0.2989, 0.5870, 0.1140])
            if self.keep_dim:
                return obs[..., None]
            else:
                return obs

    def __init__(self, env_id='SuperMarioBros-1-1-v0'):
        """
        Initializes the SuperMarioTrainer with a specified environment.

        Args:
            env_id (str, optional): The ID of the Super Mario Bros environment 
            to use. Defaults to 'SuperMarioBros-1-1-v0'.
        """
        self.env_id = env_id
        self.env = None
        self.model = None

    def create_env(self):
        """
        Creates and wraps the Super Mario Bros environment for training.

        The function initializes the Super Mario Bros environment and applies a 
        series of wrappers to make it suitable for reinforcement learning. 
        These include restricting the action space, converting observations to 
        grayscale, skipping frames, and stacking frames for temporal difference 
        learning.

        Returns:
            VecEnv: The wrapped vectorized environment.
        """
        env = gym_super_mario_bros.make("SuperMarioBros-1-1-v0")
        env = JoypadSpace(env, SIMPLE_MOVEMENT)
        env = GrayScaleObservation(env, keep_dim=True)
        env = MaxAndSkipEnv(env, skip=4)
        env = WarpFrame(env, width=84, height=84)
        env = DummyVecEnv([lambda: env])
        env = VecFrameStack(env, n_stack=4)
        return env

    def train_and_save_model(self, env, timesteps=10000, save_path="mario_model_10000"):
        """
        Trains a PPO model on the Super Mario Bros environment and saves it.

        The function trains a model using Proximal Policy Optimization (PPO)
        algorithm for a given number of timesteps. After training, the model is
        saved to the specified path.

        Args:
            env (VecEnv): The environment to train the model on.
            timesteps (int, optional): The number of timesteps to train the model.
            Defaults to 10000.
            save_path (str, optional): Path where the trained model will be saved.
            Defaults to "mario_model_10000".

        Returns:
            None
        """
        log_path = os.path.join("Training", "Logs")
        model = PPO(
            "CnnPolicy",
            env,
            verbose=1,
            tensorboard_log=log_path,
            learning_rate=0.000001,
            n_steps=512,
        )
        model.learn(total_timesteps=timesteps)
        model.save(save_path)

    def load_and_test_model(self, env, model_path="mario_model_10000"):
        """
        Loads a trained model and tests it on the Super Mario Bros environment.

        This function loads a previously trained PPO model from the specified 
        path and then runs it on the Super Mario Bros environment. The 
        environment is rendered during the test, so you can visually observe 
        the performance of the model.

        Args:
            env (VecEnv): The environment to test the model on.
            model_path (str, optional): Path from where the trained model will 
            be loaded. Defaults to "mario_model_10000".

        Returns:
            None
        """
        model = PPO.load(model_path)
        state = env.reset()
        while True:
            actions, _ = model.predict(state)
            state, reward, done, info = env.step(actions)
            env.render()
            if done:
                break


def main():
    # Example usage
    trainer = SuperMarioTrainer()
    trainer.create_env()
    trainer.train_and_save_model(timesteps=10000)
    trainer.load_and_test_model()

if __name__=='__main__':
    main()
