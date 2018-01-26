# 水蒸气参数查询模块（IAPWS97）
from iapws import IAPWS97


# 定义算法信息
def modinfo_steam():
    mod_name = '水蒸气参数查询模块（依据IAPWS97）'
    mod_imageurl = '../static/image/iapws97.png'
    mod_info = '该模块用于水的各种相态下物性参数查询。'
    mod_desp = "该模块输入为以下参数组合：温度+干度  |  压力+干度  |  温度+压力"

    return [mod_name, mod_imageurl, mod_info, mod_desp]


# 定义输入变量，生成结构体.
def modx_steam():
    modvar_type = ['基本参数']
    modvar_data = [
        {'id': 'T', 'type': '基本参数', 'text': '温度', 'value': '', 'unit': '℃', 'memo': ''},
        {'id': 'P', 'type': '基本参数', 'text': '压力', 'value': '', 'unit': 'MPa', 'memo': ''},
        {'id': 'h', 'type': '基本参数', 'text': '焓值', 'value': '', 'unit': 'kJ/kg', 'memo': ''},
        {'id': 'x', 'type': '基本参数', 'text': '干度', 'value': '', 'unit': '-', 'memo': '取0~1'},
    ]
    return [modvar_type, modvar_data]


# 计算主体
def mody_steam(x):
    # 从字典提取变量
    T = 0 if x['T'] == '' else float(x['T'])+273.15
    P = 0 if x['P'] == '' else float(x['P'])
    xr = 0 if x['h'] == '' else float(x['h'])

    # 计算结果
    if T == 0:
        rlt = IAPWS97(P=P, x=xr)
    elif P == 0:
        rlt = IAPWS97(T=T, x=xr)
    elif T != 0 and P != 0:
        rlt = IAPWS97(T=T, P=P)
    else:
        rlt = '参数输入错误!'
    print([rlt.region,T,P,xr])
# 参数二次处理
    if rlt.region == 1:
        stat = '液态'
        modvar_data = [
            {'id': 'stat', 'type': '物性参数', 'text': '状态', 'value': stat, 'unit': '-', 'memo': ''},
            {'id': 'P', 'type': '物性参数', 'text': '压力', 'value': "%.3f" % rlt.P, 'unit': 'MPa', 'memo': ''},
            {'id': 'T', 'type': '物性参数', 'text': '温度', 'value': "%.3f" % (rlt.T - 273.15), 'unit': '℃', 'memo': ''},
            {'id': 'v', 'type': '物性参数', 'text': '比容', 'value': "%.3f" % rlt.v, 'unit': 'm³/kg', 'memo': ''},
            {'id': 'rho', 'type': '物性参数', 'text': '密度', 'value': "%.3f" % rlt.rho, 'unit': 'kg/m³', 'memo': ''},
            {'id': 'h', 'type': '物性参数', 'text': '焓', 'value': "%.3f" % rlt.h, 'unit': 'kJ/kg', 'memo': ''},
            {'id': 's', 'type': '物性参数', 'text': '熵', 'value': "%.3f" % rlt.s, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cp', 'type': '物性参数', 'text': '定压比热容', 'value': "%.3f" % rlt.cp, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cv', 'type': '物性参数', 'text': '定容比热容', 'value': "%.3f" % rlt.cv, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'mu', 'type': '物性参数', 'text': '动力粘度', 'value': format(rlt.mu,'e'), 'unit': 'Pa·s', 'memo': ''},
            {'id': 'nu', 'type': '物性参数', 'text': '运动粘度', 'value': format(rlt.nu,'e'), 'unit': 'm²/s', 'memo': ''},
        ]

    elif rlt.region == 2:
        stat = '汽态'
        modvar_data = [
            {'id': 'stat', 'type': '物性参数', 'text': '状态', 'value': stat, 'unit': '-', 'memo': ''},
            {'id': 'P', 'type': '物性参数', 'text': '压力', 'value': "%.3f" % rlt.P, 'unit': 'MPa', 'memo': ''},
            {'id': 'T', 'type': '物性参数', 'text': '温度', 'value': "%.3f" % (rlt.T - 273.15), 'unit': '℃', 'memo': ''},
            {'id': 'v', 'type': '物性参数', 'text': '比容', 'value': "%.3f" % rlt.v, 'unit': 'm³/kg', 'memo': ''},
            {'id': 'rho', 'type': '物性参数', 'text': '密度', 'value': "%.3f" % rlt.rho, 'unit': 'kg/m³', 'memo': ''},
            {'id': 'h', 'type': '物性参数', 'text': '焓', 'value': "%.3f" % rlt.h, 'unit': 'kJ/kg', 'memo': ''},
            {'id': 's', 'type': '物性参数', 'text': '熵', 'value': "%.3f" % rlt.s, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cp', 'type': '物性参数', 'text': '定压比热容', 'value': "%.3f" % rlt.cp, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cv', 'type': '物性参数', 'text': '定容比热容', 'value': "%.3f" % rlt.cv, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'mu', 'type': '物性参数', 'text': '动力粘度', 'value': format(rlt.mu,'e'), 'unit': 'Pa·s', 'memo': ''},
            {'id': 'nu', 'type': '物性参数', 'text': '运动粘度', 'value': format(rlt.nu,'e'), 'unit': 'm²/s', 'memo': ''},
        ]

    elif rlt.region == 3:
        stat = '超临界'
        modvar_data = [
            {'id': 'stat', 'type': '物性参数', 'text': '状态', 'value': stat, 'unit': '-', 'memo': ''},
            {'id': 'P', 'type': '物性参数', 'text': '压力', 'value': "%.3f" % rlt.P, 'unit': 'MPa', 'memo': ''},
            {'id': 'T', 'type': '物性参数', 'text': '温度', 'value': "%.3f" % (rlt.T - 273.15), 'unit': '℃', 'memo': ''},
            {'id': 'v', 'type': '物性参数', 'text': '比容', 'value': "%.3f" % rlt.v, 'unit': 'm³/kg', 'memo': ''},
            {'id': 'rho', 'type': '物性参数', 'text': '密度', 'value': "%.3f" % rlt.rho, 'unit': 'kg/m³', 'memo': ''},
            {'id': 'h', 'type': '物性参数', 'text': '焓', 'value': "%.3f" % rlt.h, 'unit': 'kJ/kg', 'memo': ''},
            {'id': 's', 'type': '物性参数', 'text': '熵', 'value': "%.3f" % rlt.s, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cp', 'type': '物性参数', 'text': '定压比热容', 'value': "%.3f" % rlt.cp, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cv', 'type': '物性参数', 'text': '定容比热容', 'value': "%.3f" % rlt.cv, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'mu', 'type': '物性参数', 'text': '动力粘度', 'value': format(rlt.mu,'e'), 'unit': 'Pa·s', 'memo': ''},
            {'id': 'nu', 'type': '物性参数', 'text': '运动粘度', 'value': format(rlt.nu,'e'), 'unit': 'm²/s', 'memo': ''},
        ]

    elif rlt.region == 4:
        stat = '两相'
        modvar_data = [
            {'id': 'stat', 'type': '物性参数', 'text': '状态', 'value': stat, 'unit': '-', 'memo': ''},
            {'id': 'P', 'type': '物性参数', 'text': '压力', 'value': "%.3f" % rlt.P, 'unit': 'MPa', 'memo': ''},
            {'id': 'T', 'type': '物性参数', 'text': '温度', 'value': "%.3f" % (rlt.T - 273.15), 'unit': '℃', 'memo': ''},
            {'id': 'v', 'type': '物性参数', 'text': '液态比容', 'value': "%.3f" % rlt.Liquid.v, 'unit': 'm³/kg', 'memo': ''},
            {'id': 'rho', 'type': '物性参数', 'text': '液态密度', 'value': "%.3f" % rlt.Liquid.rho, 'unit': 'kg/m³', 'memo': ''},
            {'id': 'h', 'type': '物性参数', 'text': '液态焓', 'value': "%.3f" % rlt.Liquid.h, 'unit': 'kJ/kg', 'memo': ''},
            {'id': 's', 'type': '物性参数', 'text': '液态熵', 'value': "%.3f" % rlt.Liquid.s, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cp', 'type': '物性参数', 'text': '液态定压比热容', 'value': "%.3f" % rlt.Liquid.cp, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cv', 'type': '物性参数', 'text': '液态定容比热容', 'value': "%.3f" % rlt.Liquid.cv, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'mu', 'type': '物性参数', 'text': '液态动力粘度', 'value': format(rlt.Liquid.mu,'e'), 'unit': 'Pa·s', 'memo': ''},
            {'id': 'nu', 'type': '物性参数', 'text': '液态运动粘度', 'value': format(rlt.Liquid.nu,'e'), 'unit': 'm²/s', 'memo': ''},
            {'id': 'v', 'type': '物性参数', 'text': '汽态比容', 'value': "%.3f" % rlt.Vapor.v, 'unit': 'm³/kg', 'memo': ''},
            {'id': 'rho', 'type': '物性参数', 'text': '汽态密度', 'value': "%.3f" % rlt.Vapor.rho, 'unit': 'kg/m³', 'memo': ''},
            {'id': 'h', 'type': '物性参数', 'text': '汽态焓', 'value': "%.3f" % rlt.Vapor.h, 'unit': 'kJ/kg', 'memo': ''},
            {'id': 's', 'type': '物性参数', 'text': '汽态熵', 'value': "%.3f" % rlt.Vapor.s, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cp', 'type': '物性参数', 'text': '汽态定压比热容', 'value': "%.3f" % rlt.Vapor.cp, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'cv', 'type': '物性参数', 'text': '汽态定容比热容', 'value': "%.3f" % rlt.Vapor.cv, 'unit': 'kJ/kg·K', 'memo': ''},
            {'id': 'mu', 'type': '物性参数', 'text': '汽态动力粘度', 'value': format(rlt.Vapor.mu, 'e'), 'unit': 'Pa·s', 'memo': ''},
            {'id': 'nu', 'type': '物性参数', 'text': '汽态运动粘度', 'value': format(rlt.Vapor.nu, 'e'), 'unit': 'm²/s', 'memo': ''},
        ]
    else:
        stat = 'error'
        modvar_data = []

# 建立输出变量，生成结构体
    modvar_type = ['物性参数']

    return [modvar_type, modvar_data]