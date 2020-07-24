import math, random, os
from random import choice
import numpy as np
import re
from creatConfigFile import creatConfigFile

design_space = {0:[1,2], 
                1:[1,2,3,4,5,6,9,11,16],
                2:[1,3,4,5,6],
                3:[1,2],
                4:[1,2,3],
                5:[1,2,3,4,5,6],
                6:[1,2,3,4,5,6,7]}

class Population:
    # 种群的设计
    def __init__(self, size, chrom_size, cp, mp, gen_max):
        # 种群信息合
        self.individuals = []          # 个体集合
        self.fitness = []              # 个体适应度集
        self.selector_probability = [] # 个体选择概率集合
        self.new_individuals = []      # 新一代个体集合

        self.elitist = {'chromosome':[1, 1, 1, 1, 1, 1, 1], 'fitness':1000, 'age':0} # 最佳个体的信息

        self.size = size # 种群所包含的个体数
        self.chromosome_size = chrom_size # 个体的染色体长度
        self.crossover_probability = cp   # 个体之间的交叉概率
        self.mutation_probability = mp    # 个体之间的变异概率
         
        self.generation_max = gen_max # 种群进化的最大世代数
        self.age = 0                  # 种群当前所处世代
          
        # 随机产生初始个体集，并将新一代个体、适应度、选择概率等集合以 0 值进行初始化
        for i in range(self.size):
        	#x1 = choice([1,2])
			#x2 = choice([1,2,3,4,5,6,9,11,16])
			#x3 = choice([1,3,4,5,6])
			#x4 = choice([1,2])
			#x5 = choice([1,2,3])
			#x6 = choice([1,2,3,4,5,6])
			#x7 = choice([1,2,3,4,5,6,7])
            x1 = choice(design_space[0])
            x2 = choice(design_space[1])
            x3 = choice(design_space[2])
            x4 = choice(design_space[3])
            x5 = choice(design_space[4])
            x6 = choice(design_space[5])
            x7 = choice(design_space[6])
            self.individuals.append([x1,x2,x3,x4,x5,x6,x7])
            self.new_individuals.append([1,1,1,1,1,1,1])
            self.fitness.append(0)
            self.selector_probability.append(0)

    # 基于轮盘赌博机的选择
    def decode(self, interval, chromosome):
        '''将一个染色体 chromosome 映射为区间 interval 之内的数值'''
        d = interval[1] - interval[0]
        n = float (2 ** self.chromosome_size -1)
        return (interval[0] + chromosome * d / n)
     
    def fitness_func(self, individual):
        '''适应度函数，计算出该个体的适应度'''
        creatConfigFile(individual[0],individual[1],individual[2],individual[3],individual[4],individual[5],individual[6])
        output = os.system("./booksim ./wsy_work/wsy_booksim_config_file  > log")
        #print("booksim finish!")
        #print("caculate latency:")
        file = open("log",'r')
        log = file.readlines()
        line=[9999999999999]
        if len(log)>60 and "Overall Traffic Statistics" in log[-60]:
            if "e+" in log[-58] :
                print("e")
            elif  "-" in log[-58]:
                print("-")
            else:
                line = re.findall('.+\S\s(\d+\D?\d*).', log[-58])
                line = list(map(float,line))
        y = 1/np.mean(line)
        return y
         
    def evaluate(self):
        '''用于评估种群中的个体集合 self.individuals 中各个个体的适应度'''
        sp = self.selector_probability
        for i in range (self.size):
            self.fitness[i] = self.fitness_func (self.individuals[i])
        ft_sum = sum (self.fitness)
        for i in range (self.size):
            sp[i] = self.fitness[i] / float (ft_sum)   # 得到各个个体的生存概率
        for i in range (1, self.size):
            sp[i] = sp[i] + sp[i-1]   # 需要将个体的生存概率进行叠加，从而计算出各个个体的选择概率

    # 轮盘赌博机（选择）
    def select(self):
        (t, i) = (random.random(), 0)
        for p in self.selector_probability:
            if p > t:
                break
            i = i + 1
        return i

    # 交叉
    def cross(self, chrom1, chrom2):
        p = random.random()    # 随机概率
        if chrom1 != chrom2 and p < self.crossover_probability:
            t = random.randint(2, self.chromosome_size - 1)   # 随机选择一点（单点交叉）
            r1 = chrom1[0:t]
            l1 = chrom1[t:]
            r2 = chrom2[0:t]
            l2 = chrom2[t:]
            chrom1 = r1 + l2
            chrom2 = r2 + l1
        return chrom1, chrom2

    # 变异
    def mutate(self, chrom):
        p = random.random ()
        if p < self.mutation_probability:
            t = random.randint (0, self.chromosome_size-1)
            chrom[t] = choice(design_space[t])
        return chrom

    # 保留最佳个体
    def reproduct_elitist (self):
        # 与当前种群进行适应度比较，更新最佳个体
        j = -1
        for i in range (self.size):
            if self.elitist['fitness'] < self.fitness[i]:
                j = i
                self.elitist['fitness'] = self.fitness[i]
        if (j >= 0):
            self.elitist['chromosome'] = self.individuals[j]
            self.elitist['age'] = self.age

    # 进化过程
    def evolve(self):
        indvs = self.individuals
        new_indvs = self.new_individuals
        # 计算适应度及选择概率
        self.evaluate()
        # 进化操作
        i = 0
        while True:
            # 选择两个个体，进行交叉与变异，产生新的种群
            idv1 = self.select()
            idv2 = self.select()
            # 交叉
            #(idv1_x, idv1_y) = (indvs[idv1][0], indvs[idv1][1])
            #(idv2_x, idv2_y) = (indvs[idv2][0], indvs[idv2][1])
            #(idv1_x, idv2_x) = self.cross(idv1_x, idv2_x)
            #(idv1_y, idv2_y) = self.cross(idv1_y, idv2_y)
            (idv1, idv2) = self.cross(indvs[idv1], indvs[idv2])
            # 变异
            #(idv1_x, idv1_y) = (self.mutate(idv1_x), self.mutate(idv1_y))
            #(idv2_x, idv2_y) = (self.mutate(idv2_x), self.mutate(idv2_y))
            #(new_indvs[i][0], new_indvs[i][1]) = (idv1_x, idv1_y)  # 将计算结果保存于新的个体集合self.new_individuals中
            #(new_indvs[i+1][0], new_indvs[i+1][1]) = (idv2_x, idv2_y)
            (idv1, idv2) = (self.mutate(idv1), self.mutate(idv2))        
            (new_indvs[i], new_indvs[i+1]) = (idv1, idv2)

            # 判断进化过程是否结束
            i = i + 2         # 循环self.size/2次，每次从self.individuals 中选出2个
            if i >= self.size:
                break
        
        # 最佳个体保留
        # 如果在选择之前保留当前最佳个体，最终能收敛到全局最优解。
        self.reproduct_elitist()

        # 更新换代：用种群进化生成的新个体集合 self.new_individuals 替换当前个体集合
        for i in range (self.size):
            self.individuals[i] = self.new_individuals[i]
            #self.individuals[i][1] = self.new_individuals[i][1]

    def run(self):
        '''根据种群最大进化世代数设定了一个循环。
        在循环过程中，调用 evolve 函数进行种群进化计算，并输出种群的每一代的个体适应度最大值、平均值和最小值。'''
        for i in range (self.generation_max):
            self.evolve ()
            print("#####################")
            print("#####################")
            print("iter ", i) 
            print("min latency: ", 1/max(self.fitness))
            print("avg latency: ", sum(1/a for a in self.fitness)/self.size) 
            print("max latency: ", 1/min (self.fitness))
            print("best config: ", self.elitist['chromosome'])
            print("best latency: ", self.elitist['fitness'])
if __name__ == '__main__':
    # 种群的个体数量为 50，染色体长度为 25，交叉概率为 0.8，变异概率为 0.1,进化最大世代数为 150
    pop = Population (20, 7, 0.8, 0.5, 10)
    pop.run()