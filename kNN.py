"""
kNN: k近邻算法

优点：精度高，对异常值不敏感，无数据输入假定
缺点：计算复杂度高，空间复杂度高
适用范围：数值型和标称型

"""

import numpy as np
import operator

def createDataSet():
    group=np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels=['A','A','B','B']
    return group,labels
