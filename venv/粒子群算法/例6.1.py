import math
import random
import numpy
import time

time_start = time.time()


# 粒子（鸟）
class Particle:
    def __init__(self, x_min, x_max, y_min, y_max, size):
        self.x_max = x_max
        self.x_min = x_min
        self.y_max = y_max
        self.y_min = y_min
        self.v_x: list = [3, -3, 5]
        self.v_y: list = [2, -2, 3]
        self.location_x = [8, -5, -7]
        self.location_y = [-5, 9, -8]
        self.pBest = 0
        # for i in range(self.size):
        #     i_x = random.uniform(x_min, x_max)
        #     self.v_x.append(i_x)
        #     i_y = random.uniform(y_min, y_max)
        #     self.v_y.append(i_y)

        self.w = 0.5  # 惯性因子
        self.c1 = 2  # 自我认知学习因子
        self.c2 = 2  # 社会认知学习因子
        self.gBest = 0  # 种群当前最好位置
        self.N = 3  # 种群中粒子数量
        self.POP = []  # 种群
        self.iter_N = 100000  # 迭代次数
        self.size = size  # 粒子个数
        self.fitness = []
        self.g_fitness = 0
        # 初值设置直接影响精度!!(迭代次数不足时)
        for i in range(self.size):
            f = random.uniform(200, 210)
            self.fitness.append(f)
        self.g_fitness = min(self.fitness)

    # 更新
    def get_fitness(self):
        for i in range(self.size):
            x = self.location_x[i]
            y = self.location_y[i]
            f = x ** 2 + y ** 2
            if f <= self.fitness[i]:
                self.fitness[i] = f

        self.gBest = min(self.fitness)

    def evolve(self):
        # 更改速度和位置
        for i1 in range(self.iter_N):
            self.get_fitness()
            c1 = self.c1
            c2 = self.c2
            w = self.w
            #           种群数量
            for i in range(0, self.size - 1):
                r1 = random.random()
                r2 = random.random()
                pBest = self.fitness[i]
                gBest = self.gBest
                x = self.location_x[i]
                y = self.location_y[i]
                v_x = self.v_x[i]
                v_y = self.v_y[i]
                self.v_x[i] = (w * v_x + c1 * r1 * (pBest - x) + c2 * r2 * (gBest - x))
                self.v_y [ i ] = (w * v_y + c1 * r1 * (pBest - y) + c2 * r2 * (gBest - y))
                if self.x_min <= self.location_x[i] + self.v_x[i] <= self.x_max:
                    self.location_x[i] = self.location_x[i] + self.v_x[i]
                if self.y_min <= self.location_y[i] + self.v_y[i] <= self.y_max:
                    self.location_y[i] = self.location_y[i] + self.v_y[i]

        print(self.gBest)


p = Particle(10.0, -10.0, 10.0, -10.0, 3)
p.evolve()

# if __name__ == '__main__':
#     main()

time_end = time.time()
time_d = time_end - time_start
print('time cost:', time_d, 's')
print(p.evolve())