#一、完成Python的安装，输出“Hello ML”，截图写入报告。
print("Hello ML")


#二、完成NumPy的安装，并编程完成下面任务：
import numpy as np

array1 = np.array([[1,2,3],[2,3,4],[3,4,5]])
array2 = np.array([[11,21,31],[21,31,41],[31,41,51]])

#求数组的总和：
print('sum1 =',np.sum(array1))
print('sum2 =',np.sum(array2))
    

#求数组的均值：
print('mean1 =',np.mean(array1))
print('mean2 =',np.mean(array2))

#求数组的标准差：
print('std1 =',np.std(array1))
print('std2 =',np.std(array2))
