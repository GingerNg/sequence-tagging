# -*- coding: utf-8 -*-
"""
# @Time    : 2018/5/26 下午5:13
# @Author  : zhanzecheng
# @File    : simhash.py.py
# @Software: PyCharm
"""

# from model import TrieNode
# from utils import stopword, word_freq, generate_ngram
import jieba


# 定义取TOP5个
# from model import TrieNode
# from src.utils import stopword, word_freq, generate_ngram
from tools_wordstoken.Chinese_segment_augment.src.model import TrieNode
from tools_wordstoken.Chinese_segment_augment.src.utils import word_freq, generate_ngram, stopword

N = 5

# 加载数据集
data = []
with open('../data/demo1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = [x for x in jieba.cut(line, cut_all=False) if x not in stopword]
        data.append(line)




print('------> 初始化字典树')
root = TrieNode('*', word_freq)

print('------> 插入节点')
for i in data:
    tmp = generate_ngram(i, 3)
    for d in tmp:
        root.add(d)

result, add_word = root.wordFind(5)
print(result)
print(add_word)

print('增加了%d个新词, 词语和得分分别为' % len(add_word))
print('#############################')
for word, score in add_word.items():
    print(word + ' ---->  ', score)
print('#############################')

# 如果想要调试和选择其他的阈值，可以print result来调整
# print(result)

# test = '熊猫债发行制度进一步完善。2月1日，据中国银行间市场交易商协会公告，《境外非金融企业债务融资工具业务指引（试行）》（下称《指引》）正式发布。'
test = '近日，深圳海关首度成功应用来往粤港澳大湾区跨界车辆信息管理综合服务平台，办理了广东省内来往香港货运车辆申报备案这标志着海关打通与公安交管部门的数据通道，为交管业务和海关备案业务线上申报提供了平台支撑，为年内实现粤港澳大湾区跨境车辆业务全程“网上办”、“协同办”创造条件平台近期将会向公众推出'
print('添加前：')
print("".join([(x + '/ ') for x in jieba.cut(test, cut_all=False) if x not in stopword]))

for word, score in add_word.items():
    jieba.add_word(word)
print("添加后：")
print("".join([(x + '/ ') for x in jieba.cut(test, cut_all=False) if x not in stopword]))






