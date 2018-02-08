# TEST
from iapws import IAPWS97

# 计算主体
def mody_steam(x):
    
    # 从字典提取变量
    # mod = x['mod']
    # pass
    # # 计算结果
    # if mod == 'TP':
    #     T = 0 if x['T'] == '' else float(x['T']) + 273.15
    #     P = 0 if x['P'] == '' else float(x['P'])
    #     rlt = IAPWS97(P=P, T=T)
    # elif mod == 'T':
    #     T = 0 if x['T'] == '' else float(x['T']) + 273.15
    #     rlt = IAPWS97(T=T, x=0.5)
    # elif mod == 'P':
    #     P = 0 if x['P'] == '' else float(x['P'])
    #     rlt = IAPWS97(P=P, x=0.5)
    # elif mod == 'Th':
    #     T = 0 if x['T'] == '' else float(x['T']) + 273.15
    #     h = 0 if x['h'] == '' else float(x['h'])
    #     rlt = IAPWS97(T=T, h=h)
    # elif mod == 'Ph':
    #     P = 0 if x['P'] == '' else float(x['P'])
    #     h = 0 if x['h'] == '' else float(x['h'])
    #     rlt = IAPWS97(P=P, h=h)
    # else:
    #     rlt = '参数输入错误!'

    T = 0 if x['T'] == '' else float(x['T']) + 273.15
    P = 0 if x['P'] == '' else float(x['P'])

    if T==0 and P==0:
        stat = '输入错误！'
    elif T==0 and P!=0:
        rlt = IAPWS97(P=P,x=0.5)
    elif T!=0 and P==0:
        rlt = IAPWS97(T=T,x=0.5)
    elif T!=0 and P!=0:
        rlt = IAPWS97(P=P, T=T)

# 参数二次处理
    if rlt.region == 1:
        stat = '液态'
        modvar_data = [
            {'varID': 'stat', 'varType': '物性参数', 'varName': '状态', 'varVal': stat, 'varUnit': '-', 'varMemo': ''},
            {'varID': 'P', 'varType': '物性参数', 'varName': '压力', 'varVal': "%.3f" % rlt.P, 'varUnit': 'MPa', 'varMemo': ''},
            {'varID': 'T', 'varType': '物性参数', 'varName': '温度', 'varVal': "%.3f" % (rlt.T - 273.15), 'varUnit': '℃', 'varMemo': ''},
            {'varID': 'v', 'varType': '物性参数', 'varName': '比容', 'varVal': "%.3f" % rlt.v, 'varUnit': 'm³/kg', 'varMemo': ''},
            {'varID': 'rho', 'varType': '物性参数', 'varName': '密度', 'varVal': "%.3f" % rlt.rho, 'varUnit': 'kg/m³', 'varMemo': ''},
            {'varID': 'h', 'varType': '物性参数', 'varName': '焓', 'varVal': "%.3f" % rlt.h, 'varUnit': 'kJ/kg', 'varMemo': ''},
            {'varID': 's', 'varType': '物性参数', 'varName': '熵', 'varVal': "%.3f" % rlt.s, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cp', 'varType': '物性参数', 'varName': '定压比热容', 'varVal': "%.3f" % rlt.cp, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cv', 'varType': '物性参数', 'varName': '定容比热容', 'varVal': "%.3f" % rlt.cv, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'mu', 'varType': '物性参数', 'varName': '动力粘度', 'varVal': format(rlt.mu,'e'), 'varUnit': 'Pa·s', 'varMemo': ''},
            {'varID': 'nu', 'varType': '物性参数', 'varName': '运动粘度', 'varVal': format(rlt.nu,'e'), 'varUnit': 'm²/s', 'varMemo': ''},
        ]

    elif rlt.region == 2:
        stat = '汽态'
        modvar_data = [
            {'varID': 'stat', 'varType': '物性参数', 'varName': '状态', 'varVal': stat, 'varUnit': '-', 'varMemo': ''},
            {'varID': 'P', 'varType': '物性参数', 'varName': '压力', 'varVal': "%.3f" % rlt.P, 'varUnit': 'MPa', 'varMemo': ''},
            {'varID': 'T', 'varType': '物性参数', 'varName': '温度', 'varVal': "%.3f" % (rlt.T - 273.15), 'varUnit': '℃', 'varMemo': ''},
            {'varID': 'v', 'varType': '物性参数', 'varName': '比容', 'varVal': "%.3f" % rlt.v, 'varUnit': 'm³/kg', 'varMemo': ''},
            {'varID': 'rho', 'varType': '物性参数', 'varName': '密度', 'varVal': "%.3f" % rlt.rho, 'varUnit': 'kg/m³', 'varMemo': ''},
            {'varID': 'h', 'varType': '物性参数', 'varName': '焓', 'varVal': "%.3f" % rlt.h, 'varUnit': 'kJ/kg', 'varMemo': ''},
            {'varID': 's', 'varType': '物性参数', 'varName': '熵', 'varVal': "%.3f" % rlt.s, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cp', 'varType': '物性参数', 'varName': '定压比热容', 'varVal': "%.3f" % rlt.cp, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cv', 'varType': '物性参数', 'varName': '定容比热容', 'varVal': "%.3f" % rlt.cv, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'mu', 'varType': '物性参数', 'varName': '动力粘度', 'varVal': format(rlt.mu,'e'), 'varUnit': 'Pa·s', 'varMemo': ''},
            {'varID': 'nu', 'varType': '物性参数', 'varName': '运动粘度', 'varVal': format(rlt.nu,'e'), 'varUnit': 'm²/s', 'varMemo': ''},
        ]

    elif rlt.region == 3:
        stat = '超临界'
        modvar_data = [
            {'varID': 'stat', 'varType': '物性参数', 'varName': '状态', 'varVal': stat, 'varUnit': '-', 'varMemo': ''},
            {'varID': 'P', 'varType': '物性参数', 'varName': '压力', 'varVal': "%.3f" % rlt.P, 'varUnit': 'MPa', 'varMemo': ''},
            {'varID': 'T', 'varType': '物性参数', 'varName': '温度', 'varVal': "%.3f" % (rlt.T - 273.15), 'varUnit': '℃', 'varMemo': ''},
            {'varID': 'v', 'varType': '物性参数', 'varName': '比容', 'varVal': "%.3f" % rlt.v, 'varUnit': 'm³/kg', 'varMemo': ''},
            {'varID': 'rho', 'varType': '物性参数', 'varName': '密度', 'varVal': "%.3f" % rlt.rho, 'varUnit': 'kg/m³', 'varMemo': ''},
            {'varID': 'h', 'varType': '物性参数', 'varName': '焓', 'varVal': "%.3f" % rlt.h, 'varUnit': 'kJ/kg', 'varMemo': ''},
            {'varID': 's', 'varType': '物性参数', 'varName': '熵', 'varVal': "%.3f" % rlt.s, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cp', 'varType': '物性参数', 'varName': '定压比热容', 'varVal': "%.3f" % rlt.cp, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cv', 'varType': '物性参数', 'varName': '定容比热容', 'varVal': "%.3f" % rlt.cv, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'mu', 'varType': '物性参数', 'varName': '动力粘度', 'varVal': format(rlt.mu,'e'), 'varUnit': 'Pa·s', 'varMemo': ''},
            {'varID': 'nu', 'varType': '物性参数', 'varName': '运动粘度', 'varVal': format(rlt.nu,'e'), 'varUnit': 'm²/s', 'varMemo': ''},
        ]

    elif rlt.region == 4:
        stat = '饱和态'
        modvar_data = [
            {'varID': 'stat', 'varType': '物性参数', 'varName': '状态', 'varVal': stat, 'varUnit': '-', 'varMemo': ''},
            {'varID': 'P', 'varType': '物性参数', 'varName': '压力', 'varVal': "%.3f" % rlt.P, 'varUnit': 'MPa', 'varMemo': ''},
            {'varID': 'T', 'varType': '物性参数', 'varName': '温度', 'varVal': "%.3f" % (rlt.T - 273.15), 'varUnit': '℃', 'varMemo': ''},
            {'varID': 'v', 'varType': '物性参数', 'varName': '液态比容', 'varVal': "%.3f" % rlt.Liquid.v, 'varUnit': 'm³/kg', 'varMemo': ''},
            {'varID': 'rho', 'varType': '物性参数', 'varName': '液态密度', 'varVal': "%.3f" % rlt.Liquid.rho, 'varUnit': 'kg/m³', 'varMemo': ''},
            {'varID': 'h', 'varType': '物性参数', 'varName': '液态焓', 'varVal': "%.3f" % rlt.Liquid.h, 'varUnit': 'kJ/kg', 'varMemo': ''},
            {'varID': 's', 'varType': '物性参数', 'varName': '液态熵', 'varVal': "%.3f" % rlt.Liquid.s, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cp', 'varType': '物性参数', 'varName': '液态定压比热容', 'varVal': "%.3f" % rlt.Liquid.cp, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cv', 'varType': '物性参数', 'varName': '液态定容比热容', 'varVal': "%.3f" % rlt.Liquid.cv, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'mu', 'varType': '物性参数', 'varName': '液态动力粘度', 'varVal': format(rlt.Liquid.mu,'e'), 'varUnit': 'Pa·s', 'varMemo': ''},
            {'varID': 'nu', 'varType': '物性参数', 'varName': '液态运动粘度', 'varVal': format(rlt.Liquid.nu,'e'), 'varUnit': 'm²/s', 'varMemo': ''},
            {'varID': 'v', 'varType': '物性参数', 'varName': '汽态比容', 'varVal': "%.3f" % rlt.Vapor.v, 'varUnit': 'm³/kg', 'varMemo': ''},
            {'varID': 'rho', 'varType': '物性参数', 'varName': '汽态密度', 'varVal': "%.3f" % rlt.Vapor.rho, 'varUnit': 'kg/m³', 'varMemo': ''},
            {'varID': 'h', 'varType': '物性参数', 'varName': '汽态焓', 'varVal': "%.3f" % rlt.Vapor.h, 'varUnit': 'kJ/kg', 'varMemo': ''},
            {'varID': 's', 'varType': '物性参数', 'varName': '汽态熵', 'varVal': "%.3f" % rlt.Vapor.s, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cp', 'varType': '物性参数', 'varName': '汽态定压比热容', 'varVal': "%.3f" % rlt.Vapor.cp, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'cv', 'varType': '物性参数', 'varName': '汽态定容比热容', 'varVal': "%.3f" % rlt.Vapor.cv, 'varUnit': 'kJ/kg·K', 'varMemo': ''},
            {'varID': 'mu', 'varType': '物性参数', 'varName': '汽态动力粘度', 'varVal': format(rlt.Vapor.mu, 'e'), 'varUnit': 'Pa·s', 'varMemo': ''},
            {'varID': 'nu', 'varType': '物性参数', 'varName': '汽态运动粘度', 'varVal': format(rlt.Vapor.nu, 'e'), 'varUnit': 'm²/s', 'varMemo': ''},
        ]
    else:
        stat = '区域错误'
        modvar_data = [
            {'varID': 'stat', 'varType': '物性参数', 'varName': '状态', 'varVal': stat, 'varUnit': '-', 'varMemo': ''},
        ]

# 建立输出变量，生成结构体

    return modvar_data
