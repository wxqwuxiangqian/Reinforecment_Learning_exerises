import numpy as np
import pandas as pd
import time

np.set_printoptions(suppress=True)
pd.set_option('display.max_columns', 10000, 'display.max_rows', 10000)

np.random.seed(2)

# the length of the one-dimensional find treasure
# 一维寻宝游戏迷宫的长度
Number_states=6

# available acitons
# 可以选择的动作（向左走向右走）
Action=['l','r']


# greedy ploice
# 决策值，决定：下一步的选择根据Q表奖励的程序，越大越由Q表决定
epsilon=0.9

# learning rate
# 学习率，
alpha=0.1

# discount factor
# 衰减值
Lambda=0.9


# maximum episodes
# 游戏进行的最大回合数
max_episodes=20


# fresh time for one move
# 动作更新频率
Update_frequency=0.1

def build_q_table(n_states,actions):
    table=pd.DataFrame(
        # q_table initial values
        # 创建一个初始化的Q表，纵轴为状态（位置），横轴为动作（左右）
        np.zeros((n_states,len((actions)))),
        columns=actions,)   # actions's name # 每一列的命名actions里所有值
    #print(table)
    return table

def choose_action(state, q_table):
    state_actions=q_table.iloc[state, :] #根据state提取该状态的Q表
    if (np.random.uniform()>epsilon) or (state_actions.all()==0):
        action_name=np.random.choice(Action)
    else:
        action_name=state_actions.idxmax()
    return action_name

def get_env_feedback(S,A):
    if A=='r':
        if S==Number_states-2:
            S_='terminal'
            R=1
        else:
            S_=S+1
            R=0
    else:
        R=0
        if S==0:
            S_ = S
        else :
            S_=S-1
    return S_,R

def update_env(S,episode,step_counter):
        env_list=['_']*(Number_states-1)+['T']
        if S=='terminal':
            interaction='Episode %s: total_steps = %s' % (episode+1,step_counter)
            print('\r{}'.format(interaction),end='')
            time.sleep(2)
            print('\r                    ',end='')
        else:
            env_list[S]='o'
            interaction=''.join(env_list)
            print ('\r{}'.format(interaction),end='')
            time.sleep(Update_frequency)

def rl():
    # main part of RL loop
    q_table = build_q_table(Number_states, Action)
    for episode in range(max_episodes):# 回合数
        step_counter = 0  # 每回合步数计数
        S = 0    # 小人位置
        is_terminated = False  # 判断是否达到宝藏位置
        update_env(S, episode, step_counter)    # 更新位置并显示
        while not is_terminated:
            A = choose_action(S, q_table)   # 根据Q表选择下一步
            S_, R = get_env_feedback(S, A)  # take action & get next state and reward
                                            # 执行下一步 得到下一步位置 并计算奖励
            q_predict = q_table.loc[S, A]
            if S_ != 'terminal':
                q_target = R + Lambda * q_table.iloc[S_, :].max()   # next state is not terminal
            else:
                q_target = R     # next state is terminal
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += alpha * (q_target - q_predict)  # update
            S = S_  # move to next state

            update_env(S, episode, step_counter+1)
            step_counter += 1
    return q_table


if __name__ == "__main__":
    q_table = rl()
    print('\r\nQ-table:\n')
    print(q_table)







#print (choos_action(17,build_q_table(Number_states,Action)))






#build_q_table(Number_states,Action)



