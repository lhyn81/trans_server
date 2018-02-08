# CYCLONE
import math

# 计算主体
def mody_cyclone(x):
    # 从字典提取变量
    q0 = float(x['q0'])
    t = float(x['t'])
    vi = float(x['vi'])
    den_g = float(x['den_g'])
    mu = float(x['mu'])
    den_p = float(x['den_p'])
    Nc = float(x['Nc'])
    n = float(x['n'])
    dp1 = float(x['dp1'])
    dp1_r = float(x['dp1_r'])
    dp2 = float(x['dp2'])
    dp2_r =float(x['dp2_r'])
    dp3 =float(x['dp3'])
    dp3_r =float(x['dp3_r'])
    dp4 = float(x['dp4'])
    dp4_r = float(x['dp4_r'])
    dp5 = float(x['dp5'])
    dp5_r = float(x['dp5_r'])

    # 计算结果
    q = q0*(t+273)/273
    A = q/3600/vi
    D0 = (q / 3600 / (1 * 0.44 * 0.21 * vi))**0.5
    a = D0*0.44
    b = D0*0.21
    D = 2*(A/math.pi)**0.5
    De = D0*0.4
    hc = D0*0.5
    h = D0*1.4
    H = D0*3
    D2 = D0*0.4
    Cof_ZL = 16*a*b/De**2
    den_gz = den_g*273/(t+273)
    DP = Cof_ZL*vi**2/2*den_gz
    tmp1 = (4*9.8*mu*(den_p-den_gz)/(3*den_gz**2))**0.33
    Vs = 2.991*tmp1*((b/D0)**0.4/(1-b/D0)**0.33)*D0**0.067*vi**0.66
    d50 = 10**6*(9*mu*b/(2*math.pi*Nc*vi*(den_p-den_gz)))**0.5
    dp1_tmp = dp1/d50
    dp2_tmp = dp2/d50
    dp3_tmp = dp3/d50
    dp4_tmp = dp4/d50
    dp5_tmp = dp5/d50
    dp1_tmp = 1-math.exp(-0.693*dp1_tmp**(1/(1+n)))
    dp2_tmp = 1-math.exp(-0.693*dp2_tmp**(1/(1+n)))
    dp3_tmp = 1-math.exp(-0.693*dp3_tmp**(1/(1+n)))
    dp4_tmp = 1-math.exp(-0.693*dp4_tmp**(1/(1+n)))
    dp5_tmp = 1-math.exp(-0.693*dp5_tmp**(1/(1+n)))
    dp1_tmp = dp1_tmp*dp1_r
    dp2_tmp = dp2_tmp*dp2_r
    dp3_tmp = dp3_tmp*dp3_r
    dp4_tmp = dp4_tmp*dp4_r
    dp5_tmp = dp5_tmp*dp5_r
    eff = dp1_tmp+dp2_tmp+dp3_tmp+dp4_tmp+dp5_tmp

# 建立输出变量，生成结构体
    modvar_data = [
        {'varID': 'A', 'varType': '尺寸参数', 'varName': '入口面积', 'varVal': "%.3f" % A, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'D0', 'varType': '尺寸参数', 'varName': '旋风分离器直径', 'varVal': "%.3f" % D0, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'a', 'varType': '尺寸参数', 'varName': '入口高', 'varVal': "%.3f" % a, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'b', 'varType': '尺寸参数', 'varName': '入口宽', 'varVal': "%.3f" % b, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'D', 'varType': '尺寸参数', 'varName': '入口当量直径', 'varVal': "%.3f" % D, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'De', 'varType': '尺寸参数', 'varName': '排气管直径', 'varVal': "%.3f" % De, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'hc', 'varType': '尺寸参数', 'varName': '排气管插入深度', 'varVal': "%.3f" % hc, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'h', 'varType': '尺寸参数', 'varName': '旋风分离器筒体高', 'varVal': "%.3f" % h, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'H', 'varType': '尺寸参数', 'varName': '旋风分离器总高', 'varVal': "%.3f" % H, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'D2', 'varType': '尺寸参数', 'varName': '排灰管直径', 'varVal': "%.3f" % D2, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'dp1_eff', 'varType': '评价参数', 'varName': '#1分离效率', 'varVal': "%.3f" % dp1_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp2_eff', 'varType': '评价参数', 'varName': '#2分离效率', 'varVal': "%.3f" % dp2_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp3_eff', 'varType': '评价参数', 'varName': '#3分离效率', 'varVal': "%.3f" % dp3_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp4_eff', 'varType': '评价参数', 'varName': '#4分离效率', 'varVal': "%.3f" % dp4_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp5_eff', 'varType': '评价参数', 'varName': '#5分离效率', 'varVal': "%.3f" % dp5_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'eff', 'varType': '评价参数', 'varName': '平均分离效率', 'varVal': "%.3f" % eff, 'varUnit': '-', 'varMemo': ''},
    ]

    return modvar_data