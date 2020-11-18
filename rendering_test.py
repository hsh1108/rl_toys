import gym
from gym import wrappers
import matplotlib
import matplotlib.pyplot as plt

env = gym.make("SpaceInvaders-v0")
#env = wrappers.Monitor(env, "/tmp/SpaceInvaders-v0")
fig = plt.figure()
viewer = fig.add_subplot(111)
plt.ion
fig.show()
for episode in range(2):
    observation = env.reset()
    step = 0
    total_reward = 0
    while True:
        step += 1
        viewer.clear() # Clears the previous image
        viewer.imshow(env.render(mode='rgb_array')    )
        plt.pause(.05) # Delay in seconds
        fig.canvas.draw()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        total_reward += reward
        if done:
            print("Episode: {0},\tSteps: {1},\tscore: {2}"
                  .format(episode, step, total_reward)
            )
            break
env.close()