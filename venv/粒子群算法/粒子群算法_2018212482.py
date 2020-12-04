#
import random
import time

time_start = time.time()


class Particle:
    # 初始化
    def __init__(self, x_max, x_min, y_max, y_min, max_step, size):
        self.x_max = x_max
        self.x_min = x_min
        self.y_max = y_max
        self.y_min = y_min
        # 迭代次数上限
        self.max_step = max_step
        # 粒子个数
        self.size = size
        # 粒子速度初始化
        self.v_x = []
        self.v_y = []
        for i in range(self.size):
            i_x = random.uniform(x_min / 8, x_max / 8)
            self.v_x.append(i_x)
            i_y = random.uniform(y_min / 8, y_max / 8)
            self.v_y.append(i_y)
        # 粒子位置初始化
        # random.uniform(a,b)生成范围[a,b)内随机数
        self.location_x = []
        self.location_y = []
        for i in range(self.size):
            i_x = random.uniform(x_min, x_max)
            self.location_x.append(i_x)
            i_y = random.uniform(y_min, y_max)
            self.location_y.append(i_y)
        # 惯量权重,通常初始化为0.9,随进化线性递减为0.4
        self.w = 0.9
        # 加速因子,通常取2.0
        self.c1 = self.c2 = 2.0
        self.fitness = []
        # 初值设置直接影响精度!!(迭代次数不足时)
        for i in range(self.size):
            f = random.uniform(0, x_max)
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

            self.g_best = min(self.fitness)

    def evolve(self):
        # 更改速度与坐标
        for step in range(self.max_step):
            # 最大迭代次数
            # 获取历史最优与全局最优
            self.get_fitness()
            # 将常量缩写
            c1 = self.c1
            c2 = self.c2
            w = self.w
            # 种群数量
            for i in range(self.size):
                r1 = random.random()
                r2 = random.random()
                p_best = self.fitness[i]
                g_best = self.g_best
                x = self.location_x[i]
                v_x = self.v_x[i]
                y = self.location_y[i]
                v_y = self.v_y[i]
                self.v_x[i] = w * v_x + c1 * r1 * (p_best - x) + c2 * r2 * (g_best - x)
                self.v_y[i] = w * v_y + c1 * r1 * (p_best - x) + c2 * r2 * (g_best - y)
                if self.location_x[i] + self.v_x[i] >= self.x_min and self.location_x[i] + self.v_x[i] <= self.x_max:
                    self.location_x[i] = self.location_x[i] + self.v_x[i]
                if self.y_min <= self.location_y[i] + self.v_y[i] <= self.y_max:
                    self.location_y[i] = self.location_y[i] + self.v_y[i]

        print(self.g_best)


p = Particle(10, -10, 10, -10, 1000000, 10)
p.evolve()

# vi=w*vi+c1*r1*(pbest-xi)+c2*r2*(gbest-xi)
time_end = time.time()
time_d = time_end - time_start
print('time cost:', time_d, 's')
