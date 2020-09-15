import sys
import re


# 输入模块(命令行执行)
def main():
    test_ad = sys.argv[1]
    copy_ad = sys.argv[2]
    # answer_ad = sys.argv[3]
    # answer = open(answer_ad, 'w')
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
    print(test1)
    print(test2)


main()
# 用余弦相似度计算文本相似度
