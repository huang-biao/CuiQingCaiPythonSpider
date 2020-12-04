from typing import *
import random
import math


class Particle:

    def __init__(self, range_list: List[Tuple[int, int]], node_size: int, max_count: int):
        self.range_list = range_list
        self.node_size = node_size
        self.max_count = max_count
        self.w = 0.9
        self.c1 = self.c2 = 2.0
        self.node_list = [
            [
                [random.randint(min_num, max_num) for min_num, max_num in self.range_list],
                [random.randint(min_num, max_num) for min_num, max_num in self.range_list]
            ] for _ in range(node_size)
        ]
        self.gBest = None
        self.pBest_list = []
        self.best_fitness_list = []
        self.init_particle()
        print(self.gBest)

    @staticmethod
    def fitness_func(position_list):
        x1, x2, x3, x4 = position_list
        return math.cos(x1) + x2 ** 2 + math.exp(-x3) * x4 + math.sin(x1 + x2) + 1

    def init_particle(self):
        best_index = 0
        best_fitness = None
        for index, node in enumerate(self.node_list):
            v_list, p_list = node
            fitness_value = self.fitness_func(p_list)
            self.pBest_list.append(p_list)
            self.best_fitness_list.append(fitness_value)
            if best_fitness is None:
                best_fitness = fitness_value
                best_index = 0
            elif fitness_value < best_fitness:  # 判断条件
                best_fitness = fitness_value
                best_index = index
        self.gBest = self.node_list[best_index][1]

    def start(self):
        for i in range(self.max_count):
            print(f"{i}/{self.max_count}")
            # 更新速度
            for node_index, node in enumerate(self.node_list):
                v_list, p_list = node
                for v_index, v in enumerate(v_list):
                    r1, r2 = random.randint(0, 100) / 100, random.randint(0, 100) / 100
                    v_list[v_index] = self.w * v + \
                                      self.c1 * r1 * (self.pBest_list[node_index][v_index] - p_list[v_index]) + \
                                      self.c2 * r2 * (self.gBest[v_index] - p_list[v_index])
                for p_index, p in enumerate(p_list):
                    result = p + v_list[p_index]

                    min_result, max_result = self.range_list[p_index]
                    if result < min_result:
                        result = min_result
                    elif result > max_result:
                        result = max_result
                    p_list[p_index] = result

            # 评估粒子适应度
            for node_index, node in enumerate(self.node_list):
                v_list, p_list = node
                fitness_value = self.fitness_func(p_list)
                if fitness_value < self.best_fitness_list[node_index]:  # 判断结果
                    self.best_fitness_list[node_index] = fitness_value
                    self.gBest = p_list
                else:
                    continue

            # print(self.fitness_func(self.gBest))


if __name__ == '__main__':
    range_list = [(-4, 4), (-4, 4), (-4, 4), (-4, 4)]
    # range_list = [(-4, 4)]
    p = Particle(range_list, 3, 100000)
    p.start()
    print(p.gBest)
    # print(p.fitness_func([4.0, -4.0, -4.0, -4.0]))
    print(p.fitness_func(p.gBest))