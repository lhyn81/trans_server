# CYCLONE
import math


def modinfo_01():
    mod_name = '旋风分离器'
    mod_imageurl = 'https://gss1.bdstatic.com/-vo3dSag_xI4khGkpoWK1HF6hhy/baike/w%3D268%3Bg%3D0/sign=61a8537408e9390156028a3843d733da/1f178a82b9014a90eb72ade9a0773912b31bee12.jpg'
    mod_info = '旋风分离器，是用于气固体系或者液固体系的分离的一种设备。工作原理为靠气流切向引入造成的旋转运动，使具有较大惯性离心力的固体颗粒或液滴甩向外壁面分开。旋风分离器的主要特点是结构简单、操作弹性大、效率较高、管理维修方便，价格低廉，用于捕集直径5～10μm以上的粉尘，广泛应用于制药工业中，特别适合粉尘颗粒较粗，含尘浓度较大，高温、高压条件下，也常作为流化床反应器的内分离装置，或作为预分离器使用，是工业上应用很广的一种分离设备。'
    mod_desp = '模型算法依据：岑可法等《循环硫化床锅炉理论、设计与运行》北京：中国电力出版社.1997'

    return [mod_name, mod_imageurl, mod_info, mod_desp]


# 定义输入变量，生成结构体.
def modx_01():
    modvar_type = ['基本参数', '粒径分布']
    modvar_data = [
        {'id': 'q0', 'type': '基本参数', 'text':'标准状况下的体积流量', 'value': '', 'unit': 'Nm3/h', 'memo': '可尝试50000'},
        {'id': 't', 'type': '基本参数', 'text':'入口设定温度', 'value': '', 'unit': '℃', 'memo': '可尝试350'},
        {'id': 'vi', 'type': '基本参数', 'text':'旋风分离器入口气速', 'value': '', 'unit': 'm/s', 'memo': '一般可取入口速度为15~35m/s'},
        {'id': 'den_g', 'type': '基本参数', 'text':'标况下气体密度', 'value': '1.34', 'unit': 'kg/Nm3', 'memo': '通常取1.34'},
        {'id': 'mu', 'type': '基本参数', 'text': '工作温度下气体黏度', 'value': '', 'unit': 'kg/(m▪s)', 'memo': '可尝试3e-5'},
        {'id': 'den_p', 'type': '基本参数', 'text': '工作温度下固体密度', 'value': '', 'unit': 'kg/m3', 'memo': '可尝试2500'},
        {'id': 'Nc', 'type': '基本参数', 'text': '旋转回数', 'value': '', 'unit': '-', 'memo': '按入口气体速度选取，可尝试4'},
        {'id': 'n', 'type': '基本参数', 'text': '速度分布指数 ', 'value': '', 'unit': '-', 'memo': '根据计算模型选取，可尝试0.5'},
        {'id': 'dp1', 'type': '粒径分布', 'text': '#1平均粒径', 'value': '', 'unit': 'mm', 'memo': '#1平均粒径'},
        {'id': 'dp1_r', 'type': '粒径分布', 'text': '#1平均粒径质量分数 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp2', 'type': '粒径分布', 'text': '#2平均粒径', 'value': '', 'unit': 'mm', 'memo': '#2平均粒径'},
        {'id': 'dp2_r', 'type': '粒径分布', 'text': '#2平均粒径质量分数 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp3', 'type': '粒径分布', 'text': '#3平均粒径', 'value': '', 'unit': 'mm', 'memo': '#3平均粒径'},
        {'id': 'dp3_r', 'type': '粒径分布', 'text': '#3平均粒径质量分数 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp4', 'type': '粒径分布', 'text': '#4平均粒径', 'value': '', 'unit': 'mm', 'memo': '#4平均粒径'},
        {'id': 'dp4_r', 'type': '粒径分布', 'text': '#4平均粒径质量分数 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp5', 'type': '粒径分布', 'text': '#5平均粒径', 'value': '', 'unit': 'mm', 'memo': '#5平均粒径'},
        {'id': 'dp5_r', 'type': '粒径分布', 'text': '#5平均粒径质量分数 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
    ]
    return [modvar_type, modvar_data]


# 计算主体
def mody_01(x):
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
        # {'id': 'q0', 'type': '输入参数', 'text': '标准状况下的体积流量', 'value': "%.3f" % q0, 'unit': 'Nm3/h', 'memo': ''},
        # {'id': 't', 'type': '输入参数', 'text': '入口设定温度', 'value': "%.3f" % t, 'unit': '℃', 'memo': ''},
        # {'id': 'vi', 'type': '输入参数', 'text': '旋风分离器入口气速', 'value': "%.3f" % vi, 'unit': 'm/s', 'memo': ''},
        # {'id': 'mu', 'type': '输入参数', 'text': '工作温度下气体黏度', 'value': "%.3f" % mu, 'unit': 'kg/(m▪s)', 'memo': ''},
        # {'id': 'den_g', 'type': '输入参数', 'text': '工作温度下固体密度', 'value': "%.3f" % den_g, 'unit': 'kg/m3', 'memo': ''},
        {'id': 'A', 'type': '尺寸参数', 'text': '入口面积', 'value': "%.3f" % A, 'unit': 'm', 'memo': ''},
        {'id': 'D0', 'type': '尺寸参数', 'text': '旋风分离器直径', 'value': "%.3f" % D0, 'unit': 'm', 'memo': ''},
        {'id': 'a', 'type': '尺寸参数', 'text': '入口高', 'value': "%.3f" % a, 'unit': 'm', 'memo': ''},
        {'id': 'b', 'type': '尺寸参数', 'text': '入口宽', 'value': "%.3f" % b, 'unit': 'm', 'memo': ''},
        {'id': 'D', 'type': '尺寸参数', 'text': '入口当量直径', 'value': "%.3f" % D, 'unit': 'm', 'memo': ''},
        {'id': 'De', 'type': '尺寸参数', 'text': '排气管直径', 'value': "%.3f" % De, 'unit': 'm', 'memo': ''},
        {'id': 'hc', 'type': '尺寸参数', 'text': '排气管插入深度', 'value': "%.3f" % hc, 'unit': 'm', 'memo': ''},
        {'id': 'h', 'type': '尺寸参数', 'text': '旋风分离器筒体高', 'value': "%.3f" % h, 'unit': 'm', 'memo': ''},
        {'id': 'H', 'type': '尺寸参数', 'text': '旋风分离器总高', 'value': "%.3f" % H, 'unit': 'm', 'memo': ''},
        {'id': 'D2', 'type': '尺寸参数', 'text': '排灰管直径', 'value': "%.3f" % D2, 'unit': 'm', 'memo': ''},
        {'id': 'dp1_eff', 'type': '评价参数', 'text': '#1分离效率', 'value': "%.3f" % dp1_tmp, 'unit': '-', 'memo': ''},
        {'id': 'dp2_eff', 'type': '评价参数', 'text': '#2分离效率', 'value': "%.3f" % dp2_tmp, 'unit': '-', 'memo': ''},
        {'id': 'dp3_eff', 'type': '评价参数', 'text': '#3分离效率', 'value': "%.3f" % dp3_tmp, 'unit': '-', 'memo': ''},
        {'id': 'dp4_eff', 'type': '评价参数', 'text': '#4分离效率', 'value': "%.3f" % dp4_tmp, 'unit': '-', 'memo': ''},
        {'id': 'dp5_eff', 'type': '评价参数', 'text': '#5分离效率', 'value': "%.3f" % dp5_tmp, 'unit': '-', 'memo': ''},
        {'id': 'eff', 'type': '评价参数', 'text': '平均分离效率', 'value': "%.3f" % eff, 'unit': '-', 'memo': ''},
    ]

    return [modvar_type, modvar_data]