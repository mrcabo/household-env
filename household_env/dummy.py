from enum import Enum, auto
from household_env.envs.house_env import Tasks
import gym
import time

tasks_list = [Tasks.TURN_ON_TV, Tasks.TURN_ON_DISHWASHER]

env = gym.make('household_env:Household-v0')
env.reset()
env.set_current_task(tasks_list[0])

for e in range(10):
    env.render()
    _, aux, _, _ = env.step(env.action_space.sample())  # take a random action
    print(f"Reward: {aux}")
    time.sleep(0.1)
