from gym.envs.registration import register

register(
    id='Household-v0',
    entry_point='household_env.envs:HouseholdEnv',
    max_episode_steps=1000,
    reward_threshold=95,
)
