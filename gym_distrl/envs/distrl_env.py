import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from os import path

class DistEnv(gym.Env):

    def __init__(self):
        self.Pmax = np.array([1,2,3])
        self.Pmin = np.array([0,0,0])
        self.line_num = 3
        self.line_pf = [.95,.83,.91]
        self.stor_cap = [5,5,5]
        
        self.action_space = spaces.Box(low=self.Pmin, high=self.Pmax, shape=(1,), dtype=np.float32)
        self.observation_space = spaces.Tuple([
            spaces.Discrete(24), # time of the day
            spaces.MultiBinary(self.line_num), # line availability state
            spaces.Box(low=np.zeros([self.stor_cap.shape[1]]), high=self.stor_cap, dtype=np.float32) # energy storage state
        ])

        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self,action):
        self.line_stat = self.line_stat * self._get_failures(self.disaster_t) # Line outage
        # GAMS code;   inputs: Pg (action), time (self.t), line_stat (self.line_stat), storage state (self.stor)
        #              outputs: cost, storage state 
        costs = 
        self.stor = 
        
        self.t += 1
        if self.t >=24:
            self.t -= 24
        self.disaster_t += 1
        return self._get_obs(), -costs, False, {}

    def reset(self):
        self.t = np.random.randint(24) # initialize at a random hour of day
        self.line_stat = np.ones(self.line_num) # all lines initially in service
        self.stor = np.random.rand(len(self.stor_cap))*self.stor_cap # storages initialize randomly
        self.disaster_t = 0 # the first hour of the disaster
        return self._get_obs()

    def _get_obs(self):
        return self.t, self.line_stat, self.stor

    def _get_failures(self,time):
        prob_func = -abs((time-12)/12)+1
        pf = prob_func * self.line_pf
        return pf > np.random.rand(self.line_num)
        
