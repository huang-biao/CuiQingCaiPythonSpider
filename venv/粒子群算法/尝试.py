# -*- coding: utf-8 -*-

import numpy as np

# 粒子（鸟）
class particle:
    def __init__(self):
        self.pos = 0  # 粒子当前位置
        self.speed = 0
        self.pbest = 0  # 粒子历史最好位置


class PSO:
    def __init__(self):
        self.w = 0.5  # 惯性因子
        self.c1 = 2  # 自我认知学习因子
        self.c2 = 2  # 社会认知学习因子
        self.gbest = 0  # 种群当前最好位置
        self.N = 3  # 种群中粒子数量
        self.POP = []  # 种群
        self.iter_N = 5  # 迭代次数

    # 适应度值计算函数
    def fitness(self, x):
        return x + 10 * np.sin(5 * x) + 7 * np.cos(4 * x)

    # 找到全局最优解
    def g_best(self, pop):
        for bird in pop:
            if bird.fitness > self.fitness(self.gbest):
                self.gbest = bird.pos

    # 初始化种群
    def initPopulation(self, pop, N):
        for i in range(N):
            bird = particle()
            bird.pos = np.random.uniform(-10, 10)
            bird.fitness = self.fitness(bird.pos)
            bird.pbest = bird.fitness
            pop.append(bird)

        # 找到种群中的最优位置
        self.g_best(pop)

    # 更新速度和位置
    def update(self, pop):
        for bird in pop:
            # 速度更新
            speed = self.w * bird.speed + self.c1 * np.random.random() * (
                bird.pbest - bird.pos) + self.c2 * np.random.random() * (
                self.gbest - bird.pos)

            # 位置更新
            pos = bird.pos + speed

            if -10 < pos < 10: # 必须在搜索空间内
                bird.pos = pos
                bird.speed = speed
                # 更新适应度
                bird.fitness = self.fitness(bird.pos)

                # 是否需要更新本粒子历史最好位置
                if bird.fitness > self.fitness(bird.pbest):
                    bird.pbest = bird.pos

    # 最终执行
    def implement(self):
        # 初始化种群
        self.initPopulation(self.POP, self.N)

        # 迭代
        for i in range(self.iter_N):
            # 更新速度和位置
            self.update(self.POP)
            # 更新种群中最好位置
            self.g_best(self.POP)


pso = PSO()
pso.implement()

for ind in pso.POP:
    print("x=", ind.pos, "f(x)=", ind.fitness)
