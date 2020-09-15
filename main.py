from __future__ import division
import sys
import re
import jieba.analyse
from functools import reduce
from math import sqrt
import time


# 用余弦相似度计算文本相似度
class Similarity:
    # 初始化
    def __init__(self, target1, target2, topK=1000):
        self.vdict2 = {}
        self.vdict1 = {}
        self.target1 = target1
        self.target2 = target2
        self.topK = topK

    def vector(self):
        # 利用jieba进行分词并返回对应的权重
        top_keywords1 = jieba.analyse.extract_tags(self.target1, topK=self.topK, withWeight=True)
        top_keywords2 = jieba.analyse.extract_tags(self.target2, topK=self.topK, withWeight=True)
        # 分别生成字典
        for k, v in top_keywords1:
            self.vdict1[k] = v
        for k, v in top_keywords2:
            self.vdict2[k] = v

    def mix(self):
        for key in self.vdict1:
            self.vdict2[key] = self.vdict2.get(key, 0)
        for key in self.vdict2:
            self.vdict1[key] = self.vdict1.get(key, 0)

        def mapminmax(vdict):
            """计算相对词频"""
            _min = min(vdict.values())
            _max = max(vdict.values())
            _mid = _max - _min
            # print _min, _max, _mid
            for key2 in vdict:
                vdict[key2] = (vdict[key2] - _min) / _mid
            return vdict

        self.vdict1 = mapminmax(self.vdict1)
        self.vdict2 = mapminmax(self.vdict2)

    # 利用余弦相似度计算文本相似度
    def similar(self):
        self.vector()
        self.mix()
        sum2 = 0
        for key in self.vdict1:
            sum2 += self.vdict1[key] * self.vdict2[key]
        A = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict1.values())))
        B = sqrt(reduce(lambda x, y: x + y, map(lambda x: x * x, self.vdict2.values())))
        return round(sum2 / (A * B), 2)


# 输入模块(命令行执行)
def main():
    start = time.process_time()
    test_ad = sys.argv[1]
    copy_ad = sys.argv[2]
    answer_ad = sys.argv[3]
    answer = open(answer_ad, 'w')
    data1 = []
    # 以utf-8格式，打开要测试的文件并按行读取拼接到data2列表中
    for line in open(test_ad, 'r', encoding='utf-8'):
        line = line.strip()
        if line != '\n':
            if line != '':
                data1.append(line)

    # 以utf-8格式，打开要测试的文件并按行读取拼接到data2列表中

    data2 = []
    for line in open(copy_ad, 'r', encoding='utf-8'):
        line = line.strip()
        if line != '\n':
            if line != '':
                data2.append(line)

    # 连接每个行使其成为一个完整的文本存入字符串中
    test1 = ''.join(data1)
    test2 = ''.join(data2)
    # 去符号
    # punc用来记录去符号的标志字符串
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“”：’；、。，？》《{}'
    test1 = re.sub(r'[%s]+' % punc, '', test1)
    test2 = re.sub(r'[%s]+' % punc, '', test2)

    topK = 1000
    s = Similarity(test1, test2, topK)
    total = s.similar()
    print(total)
    answer.write(str(total))
    end = time.process_time()
    print('Running time: %s Seconds' % (end - start))
    return 0


if __name__ == '__main__':
    main()
