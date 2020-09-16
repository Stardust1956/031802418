import unittest
from main import Similarity
import time
import re


def yuchuli(position1, position2):
    test_ad = position1
    copy_ad = position2
    data1 = []
    # 以utf-8格式，打开要测试的文件并按行读取拼接到data2列表中
    file1 = open(test_ad, 'r', encoding='utf-8')
    file2 = open(copy_ad, 'r', encoding='utf-8')
    for line in file1:
        line = line.strip()
        if line != '\n':
            if line != '':
                data1.append(line)

    # 以utf-8格式，打开要测试的文件并按行读取拼接到data2列表中

    data2 = []
    for line in file2:
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
    file1.close()
    file2.close()
    return test1, test2


class Testformain(unittest.TestCase):

    def test_itself(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test1")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_add(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_add.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test2")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_del(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_del.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test3")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_dis_1(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_dis_1.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test4")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_dis_3(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_dis_3.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test5")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_dis_7(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_dis_7.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test6")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_dis_10(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_dis_10.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test7")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_dis_15(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_dis_15.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test8")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_mix(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_mix.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test9")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_rep(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\orig.txt", "D:\\sim\orig_0.8_rep.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Test10")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_my1(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\mytest1.txt", "D:\\sim\mytest1_1.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Myest_1")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_my2(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\mytest2.txt", "D:\\sim\mytest2_2.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Myest_2")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_my3(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\mytest3.txt", "D:\\sim\mytest3_3.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Myest_3")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()

    def test_my4(self):
        start = time.process_time()
        t1, t2 = yuchuli("D:\\sim\mytest4.txt", "D:\\sim\mytest4_4.txt")
        s = Similarity(t1, t2, int(len(t1)))
        print("Myest_4")
        print(s.similar())
        end = time.process_time()
        print('Running time: %s Seconds' % (end - start))
        print()


if __name__ == '__main__':
    unittest.main()
