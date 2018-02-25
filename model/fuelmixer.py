# FuelMixer
import math

# 计算主体
def mody_fuelmixer(x):
    # 从字典提取变量
    data = [0]*100
    for k,v in x.items():
        head=k[:-1]
        num=int(k[-1])
        if head=='F': data[(num-1)*9]=v
        elif head == 'C': data[(num-1)*9+1]=v
        elif head == 'H': data[(num-1)*9+2]=v
        elif head == 'O': data[(num-1)*9+3]=v
        elif head == 'N': data[(num-1)*9+4]=v
        elif head == 'S': data[(num-1)*9+5]=v
        elif head == 'CL': data[(num-1)*9+6]=v
        elif head == 'A': data[(num-1)*9+7]=v
        elif head == 'W': data[(num-1)*9+8]=v
    # print(data)
    TF=C=H=O=N=S=CL=A=W=0
    for i in range(0,90,9):
        TF = TF + float(data[i])
        C=C+float(data[i])*float(data[i+1])
        H=H+float(data[i])*float(data[i+2])
        O=O+float(data[i])*float(data[i+3])
        N=N+float(data[i])*float(data[i+4])
        S=S+float(data[i])*float(data[i+5])
        CL=CL+float(data[i])*float(data[i+6])
        A=A+float(data[i])*float(data[i+7])
        W=W+float(data[i])*float(data[i+8])
        Total=C+H+O+N+S+CL+A+W

# 建立输出变量，生成结构体
    modvar_data = [
        {'varID': 'TF', 'varType': '燃料数据', 'varName': '混合原料质量总量', 'varVal': "%.5f" % TF, 'varUnit': '1', 'varMemo': '应为1.0'},
        {'varID': 'C', 'varType': '燃料数据', 'varName': '混合原料C质量分数', 'varVal': "%.5f" % C, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'H', 'varType': '燃料数据', 'varName': '混合原料H质量分数', 'varVal': "%.5f" % H, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'O', 'varType': '燃料数据', 'varName': '混合原料O质量分数', 'varVal': "%.5f" % O, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'N', 'varType': '燃料数据', 'varName': '混合原料N质量分数', 'varVal': "%.5f" % N, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'S', 'varType': '燃料数据', 'varName': '混合原料S质量分数', 'varVal': "%.5f" % S, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'CL', 'varType': '燃料数据', 'varName': '混合原料CL质量分数', 'varVal': "%.5f" % CL, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'A', 'varType': '燃料数据', 'varName': '混合原料A质量分数', 'varVal': "%.5f" % A, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'W', 'varType': '燃料数据', 'varName': '混合原料W质量分数', 'varVal': "%.5f" % W, 'varUnit': '1', 'varMemo': '0到1之间'},
        {'varID': 'Total', 'varType': '燃料数据', 'varName': '混合原料元素总量', 'varVal': "%.5f" % Total, 'varUnit': '1', 'varMemo': '0到1之间'}
    ]

    return modvar_data