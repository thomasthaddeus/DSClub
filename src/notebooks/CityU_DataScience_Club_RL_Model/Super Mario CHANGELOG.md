# Super Mario CHANGELOG

## In this code

gym_super_mario_bros.make('SuperMarioBros-1-1-v0') creates the base Super Mario Bros environment.
JoypadSpace(env, SIMPLE_MOVEMENT) simplifies the action space.
GrayScaleObservation is a custom VecEnvWrapper to convert the environment to grayscale.
MaxAndSkipEnv(env, skip=4) is a wrapper to return the maximum pixel value over the last skip frames.
WarpFrame(env, width=84, height=84) resizes the image size into 84 x 84 and converts RGB to grayscale.
DummyVecEnv([lambda: env]) is used to create a vectorized environment. This is required when using wrappers for frame-stacking or normalization.
VecFrameStack(env, n_stack=4) stacks adjacent 4 frames together to be one state.
Note that we don't use Monitor as in the original code because it is deprecated. As an alternative, you might want to use the tensorboard_log argument when initializing the model to enable logging and use TensorBoard for visualization. The log_path variable is used to specify the log directory. It's also worth noting that the render() function is used to visualize the environment.

Before you run this code, please make sure to install the necessary packages:

`pip install gym-super-mario-bros`
`pip install stable-baselines3[extra]`

Also, please note that machine learning algorithms can be quite stochastic in nature, so your results might not be exactly the same each time you run the script, even with the same parameters.

This script is a significant update from previous iterations. First, it uses Stable Baselines3, which has several differences from Stable Baselines2:

Stable Baselines3 uses PyTorch instead of TensorFlow as the backend, which offers several advantages, including improved readability and debugging.
The use of environment wrappers has been updated to be compatible with Stable Baselines3, which includes changes in function names and behaviors.
A custom wrapper GrayScaleObservation is defined and used to convert the observations to grayscale, reducing dimensionality, speeding up training, and reducing memory footprint. This was not present in previous versions.
The actions passed to the environment are now a vector (of dimension n), and the observations, rewards, and end of episode signals (dones) returned from the environment are also vectors.
TensorBoard logging has been added for easier tracking and visualization of the training progress, which was not available in the previous versions.
The Super Mario Bros environment is also wrapped to make it more suitable for training an RL agent. The modifications include restricting the action space to simple movements, grayscaling and resizing the observations, skipping frames for faster processing, and stacking frames for temporal difference learning.
