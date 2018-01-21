# CYCLONE
import math


# Define all data info of modules.
def modx_00():
    modvar_type = ['基本参数', '高级参数', '粒径分布']
    modvar_data = [
        {'id': 'q0', 'type': '基本参数', 'text':'标准状况下的体积流量', 'value': '', 'unit': 'Nm3/h', 'memo': '例如50000'},
        {'id': 't', 'type': '基本参数', 'text':'入口设定温度', 'value': '', 'unit': '℃', 'memo': '例如350'},
        {'id': 'vi', 'type': '基本参数', 'text':'旋风分离器入口气速', 'value': '', 'unit': 'm/s', 'memo': '一般可取入口速度为15~35m/s'},
        {'id': 'den_g', 'type': '基本参数', 'text':'标况下气体密度', 'value': '', 'unit': 'kg/Nm3', 'memo': '通常取1.34'},
        {'id': 'mu', 'type': '基本参数', 'text': '工作温度下气体黏度', 'value': '', 'unit': 'kg/(m▪s)', 'memo': '例如3e-5'},
        {'id': 'den_p', 'type': '基本参数', 'text': '工作温度下固体密度', 'value': '', 'unit': 'kg/m3', 'memo': '例如5000'},
        {'id': 'Nc', 'type': '高级参数', 'text': '旋风分离器中回路数', 'value': '', 'unit': '-', 'memo': '通常取1'},
        {'id': 'n', 'type': '高级参数', 'text': '速度分布指数 ', 'value': '', 'unit': '-', 'memo': '通常取0.5'},
        {'id': 'dp1', 'type': '粒径分布', 'text': '直径<1.5mm的粒径质量比例 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp2', 'type': '粒径分布', 'text': '直径<10mm的粒径质量比例 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp3', 'type': '粒径分布', 'text': '直径<50mm的粒径质量比例 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp4', 'type': '粒径分布', 'text': '直径<100mm的粒径质量比例 ', 'value': '', 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp5', 'type': '粒径分布', 'text': '直径<500mm的粒径质量比例 ', 'value': '', 'unit': '-', 'memo': '取0~1'}
    ]
    return [modvar_type, modvar_data]


# CYCLONE
def mody_00(x):
# 从字典提取变量
    q0 = float(x['q0'])
    t = float(x['t'])
    vi = float(x['vi'])
    mu = float(x['mu'])
    den_g = float(x['den_g'])
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
    den_gz = 1.34*273/(t+273)
    DP = Cof_ZL*vi**2/2*den_gz
    tmp1 = (4*9.8*mu*(den_g-den_gz)/(3*den_gz**2))**0.33
    Vs = 2.991*tmp1*((b/D0)**0.4/(1-b/D0)**0.33)*D0**0.067*vi**0.66
    Nc=4
    d50 = 10**6*(9*mu*b/(2*math.pi*Nc*vi*(den_g-den_gz)))**0.5
# 建立输出变量
    y = ({
        'Q': "%.3f" % q0,
        'T': "%.3f" % t,
        'V': "%.3f" % vi,
        'mu': "%.3f" % mu,
        'den': "%.3f" % den_g,
        'q': "%.3f" % q,
        'A': "%.3f" % A,
        'D0': "%.3f" % D0,
        'a': "%.3f" % a,
        'b': "%.3f" % b,
        'D': "%.3f" % D,
        'De': "%.3f" % De,
        'hc': "%.3f" % hc,
        'h': "%.3f" % h,
        'H': "%.3f" % H,
        'D2': "%.3f" % D2,
        'Cof_ZL': "%.3f" % Cof_ZL,
        'den_gz': "%.3f" % den_gz,
        'DP': "%.3f" % DP,
        'Vs': "%.3f" % Vs,
        'Nc': "%.3f" % Nc,
        'd50': "%.3f" % d50
        })

    modvar_type = ['基本参数', '尺寸参数', '评价参数']
    modvar_data = [
        {'id': 'q0', 'type': '基本参数', 'text': '标准状况下的体积流量', 'value': 0.0, 'unit': 'Nm3/h', 'memo': '例如50000'},
        {'id': 't', 'type': '基本参数', 'text': '入口设定温度', 'value': 0.0, 'unit': '℃', 'memo': '例如350'},
        {'id': 'vi', 'type': '基本参数', 'text': '旋风分离器入口气速', 'value': 0.0, 'unit': 'm/s', 'memo': '一般可取入口速度为15~35m/s'},
        {'id': 'den_g', 'type': '基本参数', 'text': '标况下气体密度', 'value': 0.0, 'unit': 'kg/Nm3', 'memo': '通常取1.34'},
        {'id': 'mu', 'type': '尺寸参数', 'text': '工作温度下气体黏度', 'value': 0.0, 'unit': 'kg/(m▪s)', 'memo': '例如3e-3'},
        {'id': 'den_p', 'type': '尺寸参数', 'text': '工作温度下固体密度', 'value': 0.0, 'unit': 'kg/m3', 'memo': '例如5000'},
        {'id': 'Nc', 'type': '尺寸参数', 'text': '旋风分离器中回路数', 'value': 0.0, 'unit': '-', 'memo': '通常取1'},
        {'id': 'n', 'type': '尺寸参数', 'text': '速度分布指数 ', 'value': 0.0, 'unit': '-', 'memo': '通常取0.5'},
        {'id': 'dp1', 'type': '尺寸参数', 'text': '直径<1.5mm的粒径质量比例 ', 'value': 0.0, 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp2', 'type': '尺寸参数', 'text': '直径<10mm的粒径质量比例 ', 'value': 0.0, 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp3', 'type': '尺寸参数', 'text': '直径<50mm的粒径质量比例 ', 'value': 0.0, 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp4', 'type': '尺寸参数', 'text': '直径<100mm的粒径质量比例 ', 'value': 0.0, 'unit': '-', 'memo': '取0~1'},
        {'id': 'dp5', 'type': '评价参数', 'text': '直径<500mm的粒径质量比例 ', 'value': 0.0, 'unit': '-', 'memo': '取0~1'}
    ]

    return [modvar_type, modvar_data]