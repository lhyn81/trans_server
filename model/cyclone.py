# CYCLONE
import math


def modinfo_cyclone():
    mod_name = '旋风分离器'
    mod_imageurl = 'https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=61a8537408e9390156028a3843d733da/1f178a82b9014a90eb72ade9a0773912b31bee12.jpg'
    mod_info = '旋风分离器，是用于气固体系或者液固体系的分离的一种设备。工作原理为靠气流切向引入造成的旋转运动，使具有较大惯性离心力的固体颗粒或液滴甩向外壁面分开。旋风分离器的主要特点是结构简单、操作弹性大、效率较高、管理维修方便，价格低廉，用于捕集直径5～10μm以上的粉尘，广泛应用于制药工业中，特别适合粉尘颗粒较粗，含尘浓度较大，高温、高压条件下，也常作为流化床反应器的内分离装置，或作为预分离器使用，是工业上应用很广的一种分离设备。'
    mod_desp = '模型算法依据：岑可法等《循环硫化床锅炉理论、设计与运行》北京：中国电力出版社.1997'

    return [mod_name, mod_imageurl, mod_info, mod_desp]


# 定义输入变量，生成结构体.
def modx_cyclone():
    modvar_type = ['基本参数', '粒径分布']
    modvar_data = [
        {'varID': 'q0', 'type': '基本参数', 'varName':'标准状况下的体积流量', 'varVal': '', 'varUnit': 'Nm3/h', 'varMemo': '可尝试50000'},
        {'varID': 't', 'type': '基本参数', 'varName':'入口设定温度', 'varVal': '', 'varUnit': '℃', 'varMemo': '可尝试350'},
        {'varID': 'vi', 'type': '基本参数', 'varName':'旋风分离器入口气速', 'varVal': '', 'varUnit': 'm/s', 'varMemo': '一般可取入口速度为15~35m/s'},
        {'varID': 'den_g', 'type': '基本参数', 'varName':'标况下气体密度', 'varVal': '1.34', 'varUnit': 'kg/Nm3', 'varMemo': '通常取1.34'},
        {'varID': 'mu', 'type': '基本参数', 'varName': '工作温度下气体黏度', 'varVal': '', 'varUnit': 'kg/(m▪s)', 'varMemo': '可尝试3e-5'},
        {'varID': 'den_p', 'type': '基本参数', 'varName': '工作温度下固体密度', 'varVal': '', 'varUnit': 'kg/m3', 'varMemo': '可尝试2500'},
        {'varID': 'Nc', 'type': '基本参数', 'varName': '旋转回数', 'varVal': '', 'varUnit': '-', 'varMemo': '按入口气体速度选取，可尝试4'},
        {'varID': 'n', 'type': '基本参数', 'varName': '速度分布指数 ', 'varVal': '', 'varUnit': '-', 'varMemo': '根据计算模型选取，可尝试0.5'},
        {'varID': 'dp1', 'type': '粒径分布', 'varName': '#1平均粒径', 'varVal': '', 'varUnit': 'mm', 'varMemo': '#1平均粒径'},
        {'varID': 'dp1_r', 'type': '粒径分布', 'varName': '#1平均粒径质量分数 ', 'varVal': '', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp2', 'type': '粒径分布', 'varName': '#2平均粒径', 'varVal': '', 'varUnit': 'mm', 'varMemo': '#2平均粒径'},
        {'varID': 'dp2_r', 'type': '粒径分布', 'varName': '#2平均粒径质量分数 ', 'varVal': '', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp3', 'type': '粒径分布', 'varName': '#3平均粒径', 'varVal': '', 'varUnit': 'mm', 'varMemo': '#3平均粒径'},
        {'varID': 'dp3_r', 'type': '粒径分布', 'varName': '#3平均粒径质量分数 ', 'varVal': '', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp4', 'type': '粒径分布', 'varName': '#4平均粒径', 'varVal': '', 'varUnit': 'mm', 'varMemo': '#4平均粒径'},
        {'varID': 'dp4_r', 'type': '粒径分布', 'varName': '#4平均粒径质量分数 ', 'varVal': '', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp5', 'type': '粒径分布', 'varName': '#5平均粒径', 'varVal': '', 'varUnit': 'mm', 'varMemo': '#5平均粒径'},
        {'varID': 'dp5_r', 'type': '粒径分布', 'varName': '#5平均粒径质量分数 ', 'varVal': '', 'varUnit': '-', 'varMemo': '取0~1'},
    ]
    return [modvar_type, modvar_data]


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
    modvar_type = ['尺寸参数', '评价参数']
    modvar_data = [
        # {'varID': 'q0', 'type': '输入参数', 'varName': '标准状况下的体积流量', 'varVal': "%.3f" % q0, 'varUnit': 'Nm3/h', 'varMemo': ''},
        # {'varID': 't', 'type': '输入参数', 'varName': '入口设定温度', 'varVal': "%.3f" % t, 'varUnit': '℃', 'varMemo': ''},
        # {'varID': 'vi', 'type': '输入参数', 'varName': '旋风分离器入口气速', 'varVal': "%.3f" % vi, 'varUnit': 'm/s', 'varMemo': ''},
        # {'varID': 'mu', 'type': '输入参数', 'varName': '工作温度下气体黏度', 'varVal': "%.3f" % mu, 'varUnit': 'kg/(m▪s)', 'varMemo': ''},
        # {'varID': 'den_g', 'type': '输入参数', 'varName': '工作温度下固体密度', 'varVal': "%.3f" % den_g, 'varUnit': 'kg/m3', 'varMemo': ''},
        {'varID': 'A', 'type': '尺寸参数', 'varName': '入口面积', 'varVal': "%.3f" % A, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'D0', 'type': '尺寸参数', 'varName': '旋风分离器直径', 'varVal': "%.3f" % D0, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'a', 'type': '尺寸参数', 'varName': '入口高', 'varVal': "%.3f" % a, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'b', 'type': '尺寸参数', 'varName': '入口宽', 'varVal': "%.3f" % b, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'D', 'type': '尺寸参数', 'varName': '入口当量直径', 'varVal': "%.3f" % D, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'De', 'type': '尺寸参数', 'varName': '排气管直径', 'varVal': "%.3f" % De, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'hc', 'type': '尺寸参数', 'varName': '排气管插入深度', 'varVal': "%.3f" % hc, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'h', 'type': '尺寸参数', 'varName': '旋风分离器筒体高', 'varVal': "%.3f" % h, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'H', 'type': '尺寸参数', 'varName': '旋风分离器总高', 'varVal': "%.3f" % H, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'D2', 'type': '尺寸参数', 'varName': '排灰管直径', 'varVal': "%.3f" % D2, 'varUnit': 'm', 'varMemo': ''},
        {'varID': 'dp1_eff', 'type': '评价参数', 'varName': '#1分离效率', 'varVal': "%.3f" % dp1_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp2_eff', 'type': '评价参数', 'varName': '#2分离效率', 'varVal': "%.3f" % dp2_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp3_eff', 'type': '评价参数', 'varName': '#3分离效率', 'varVal': "%.3f" % dp3_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp4_eff', 'type': '评价参数', 'varName': '#4分离效率', 'varVal': "%.3f" % dp4_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'dp5_eff', 'type': '评价参数', 'varName': '#5分离效率', 'varVal': "%.3f" % dp5_tmp, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'eff', 'type': '评价参数', 'varName': '平均分离效率', 'varVal': "%.3f" % eff, 'varUnit': '-', 'varMemo': ''},
    ]

    # return [modvar_type, modvar_data]
    return modvar_data