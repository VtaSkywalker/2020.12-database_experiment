import sys
sys.path.append("../04-实现阶段/codes")

import numpy as np

from Login import *

D = np.loadtxt("test_Login.txt", dtype = str)
user = D[:, 0]
password = D[:, 1]
loginType = D[:, 2]
exceptResult = D[:, 3]
length_of_data = len(user)
for idx in range(length_of_data):
    if(Login.loginVerify("'" + user[idx] + "'", "'" + password[idx] + "'", loginType[idx])):
        actualResult = 1
    else:
        actualResult = 0
    if(str(actualResult) != exceptResult[idx]):
        print("[WRONG!]", end = "")
    print("user = %s, password = %s, loginType = %s, exceptResult = %s, actualResult = %d" % (user[idx], password[idx], loginType[idx], exceptResult[idx], actualResult))