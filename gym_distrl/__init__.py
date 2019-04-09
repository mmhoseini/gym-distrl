from gym.envs.registration import register

register(
    id='distrl-v0',
    entry_point='gym_distrl.envs:DistrlEnv',
)
register(
    id='distrl-extrahard-v0',
    entry_point='gym_distrl.envs:DistrlExtraHardEnv',
)
