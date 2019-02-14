"""
Make it more robust.
Stop episode once the finger stop at the final position for 50 steps.
Feature & reward engineering.
"""
from env import ArmEnv
from rl import DDPG

MAX_EPISODES = 500
MAX_EP_STEPS = 200
ON_TRAIN = True

# set env
env = ArmEnv()
s_dim = env.state_dim   # 观测值的数目 （输入）
a_dim = env.action_dim  # 手臂的动作  （输出）
a_bound = env.action_bound   # 动作幅度

# set RL method (continuous)
rl = DDPG(a_dim, s_dim, a_bound)

steps = []
def train():
    # start training # 训练回合数
    for i in range(MAX_EPISODES):     # 训练步数
        s = env.reset()        # 初始化回合
        ep_r = 0.
        for j in range(MAX_EP_STEPS):
            env.render()        # 动画展示

            a = rl.choose_action(s)    # 给定输入 经过神经网络 环境更新 返回下一个动作

            s_, r, done = env.step(a)  # 返回下一个输入  奖励 是否结束

            rl.store_transition(s, a, r, s_) # 离线学习 放入记忆库

            ep_r += r
            if rl.memory_full:
                # start to learn once has fulfilled the memory
                rl.learn()

            s = s_
            if done or j == MAX_EP_STEPS-1:
                print('Ep: %i | %s | ep_r: %.1f | step: %i' % (i, '---' if not done else 'done', ep_r, j))
                break
    rl.save()


def eval():
    rl.restore()
    env.render()
    env.viewer.set_vsync(True)
    while True:
        s = env.reset()
        for _ in range(200):
            env.render()
            a = rl.choose_action(s)
            s, r, done = env.step(a)
            if done:
                break


if ON_TRAIN:
    train()
else:
    eval()



