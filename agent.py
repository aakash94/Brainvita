from Env import Env
import math
import random
import numpy as np
import pandas as pd
import pickle
from collections import namedtuple
from torch.utils.tensorboard import SummaryWriter
# from IPython.display import clear_output

tag_reward = "reward"
tag_se = "states_explored"

tuple2index_path = "tuple2index.pkl"
dataframe_path = "dataframe.pkl"
seen_states_path = "seens_tates.pkl"


action_range = list(range(Env.ACTION_N))

GAMMA      = 0.9 # discount factor
EPSILON    = 1
LEARN_RATE = 0.001

STATE_N  = Env.DIM * Env.DIM
ACTION_N = Env.ACTION_N

NUM_EPISODES = 3000000
LAMBDA = 0.99 

INIT_ROW = [-500]*Env.ACTION_N # all actions invalid to start with
ET_INIT = [0]*Env.ACTION_N # 0 trace to start with
OPTIMISTIC_INTI_VAL = 12

env = Env()

def np2tuple(np_array_2d):
    return tuple(np_array_2d.ravel())

tuple2index = dict()
seen_states= set() 
action_header = list(range(ACTION_N))
df = pd.DataFrame(columns=action_header, dtype='float64')
et = pd.DataFrame(columns=action_header, dtype='float64')        


def load_pickle():
    global df
    global tuple2index
    global seen_states
    
    tuple2index_pkl = Path(tuple2index_path)
    seen_states_pkl = Path(seen_states_path)
    dataframe_pkl = Path(dataframe_path)
    
    if tuple2index_pkl.is_file() and seen_states_pkl.is_file() and dataframe_pkl.is_file():
        
        df = pd.read_pickle(dataframe_path)
        tuple2index = pickle.load( open( tuple2index_path, "rb" ) )
        seen_states = pickle.load( open( seen_states_path, "rb" ) )
    
def get_index(np_mat):
    tup = np2tuple(np_mat)
    ind = len(tuple2index)
    
    if tup not in seen_states :
        seen_states.add(tup)
        tuple2index[tup] = ind
        df.loc[tuple2index[tup]] = INIT_ROW
        et.loc[tuple2index[tup]] = ET_INIT
              
        temp_env = Env()
        temp_env.set(board_state = np_mat)
        valid_action_numbers = temp_env.get_valid_actions()
        for action_number in valid_action_numbers:
            df[action_number][tuple2index[tup]] = OPTIMISTIC_INTI_VAL
        
    return tuple2index[tup]

def select_action(np_state):       
    tup = np2tuple(np_state)    
    return df.iloc[tuple2index[tup]].idxmax(axis = 0)           

def save_pickle():
    df.to_pickle(dataframe_path)

    with open(tuple2index_path, 'wb') as f:
        pickle.dump(tuple2index, f)
        f.close()
        
    with open(seen_states_path, 'wb') as f:
        pickle.dump(seen_states, f)
        f.close()

        
def reorient(np_state):
    original = np.copy(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    # anti-clock 1
    np_state = np.rot90(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    # anti-clock 2
    np_state = np.rot90(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    # anti-clock 3
    np_state = np.rot90(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    #Mirror horizontally
    np_state = np.fliplr(original)
    
    if np2tuple(np_state) in seen_states:
        return np_state
    
    # flipped anti-clock 1
    np_state = np.rot90(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    # flipped anti-clock 2
    np_state = np.rot90(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    # flipped anti-clock 3
    np_state = np.rot90(np_state)
    if np2tuple(np_state) in seen_states:
        return np_state
    
    return original



load_pickle()
writer = SummaryWriter(comment='__')

for i_episode in range(NUM_EPISODES):
    state = env.reset()
    done = False
    total_reward = 0
    
    for col in et.columns:
        et[col].values[:] = 0
    while not done:     
    
        index = get_index(state)       
        
        action = select_action(state)
        next_state, reward, done = env.step(action)
        next_state = reorient(next_state)
        
        next_index = get_index(next_state)
        
        et[action][index] += 1     
        next_action = select_action(next_state)     
        
        if done:
            on_board = env.get_count()          
            if on_board  == 1:
                # game success
                reward = reward*1000
            else:
                # wrong solution
                # negative reward
                reward = -(on_board*10)
                
        delta = (reward + (df[next_action][next_index] * GAMMA)) - df[action][index]        
        
        temp_df = et*(delta*LEARN_RATE)
        df += temp_df        
        et *= LAMBDA   
        total_reward += reward        
        state = next_state
        env.set(board_state=state)
        
    writer.add_scalar(tag_reward, total_reward, i_episode)    
    writer.add_scalar(tag_se, len(tuple2index), i_episode)
    
    ## clear_output()
    ## print(i_episode,"\t",total_reward)
    ## print(env.get_state())
    
    
    if i_episode % 50 == 0:
        save_pickle()
        
print('Complete')