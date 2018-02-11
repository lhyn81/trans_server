# 该文件定义了：
# 1、所有算法的数据结构；
# 2、所有算法内输入变量的数据结构；

# 定义算法分组信息
modGroup = ['通用模型库','火电模型库','生物质模型库','环保模型库','设计工具集','其他']

# 定义算法总表
modItems = {
	'cyclone':{'modID':'cyclone','modName':'旋风分离器','modGroup':'通用模型库','modInfo':'','modVar':[],'modCalculator':'mody_cyclone'},
	'gasifi' :{'modID':'gasifi','modName':'生物质气化产物计算','modGroup':'生物质模型库','modInfo':'','modVar':[],'modCalculator':'mody_aspen'},
	'steam'  :{'modID':'steam','modName':'水蒸气参数查询','modGroup':'设计工具集','modInfo':'','modVar':[],'modCalculator':'mody_steam'},	
        'devnote':{'modID':'devnote','modName':'开发备忘','modGroup':'其他','modInfo':'','modVar':[],'modCalculator':''},        
        'stock':{'modID':'stock','modName':'股票信息检索','modGroup':'其他','modInfo':'','modVar':[],'modCalculator':''}        
}

# 定义旋风分离器的参数信息
modItems['cyclone']['modInfo'] = '旋风分离器计算模块描述'
modItems['cyclone']['modVar'] = [
        {'varID': 'q0', 'varType': '基本参数', 'varName':'标准状况下的体积流量', 'varVal': '50000', 'varUnit': 'Nm3/h', 'varMemo': '可尝试50000'},
        {'varID': 't', 'varType': '基本参数', 'varName':'入口设定温度', 'varVal': '350', 'varUnit': '℃', 'varMemo': '可尝试350'},
        {'varID': 'vi', 'varType': '基本参数', 'varName':'旋风分离器入口气速', 'varVal': '15', 'varUnit': 'm/s', 'varMemo': '一般可取入口速度为15~35m/s'},
        {'varID': 'den_g', 'varType': '基本参数', 'varName':'标况下气体密度', 'varVal': '1.34', 'varUnit': 'kg/Nm3', 'varMemo': '通常取1.34'},
        {'varID': 'mu', 'varType': '基本参数', 'varName': '工作温度下气体黏度', 'varVal': '3e-5', 'varUnit': 'kg/(m▪s)', 'varMemo': '可尝试3e-5'},
        {'varID': 'den_p', 'varType': '基本参数', 'varName': '工作温度下固体密度', 'varVal': '2500', 'varUnit': 'kg/m3', 'varMemo': '可尝试2500'},
        {'varID': 'Nc', 'varType': '基本参数', 'varName': '旋转回数', 'varVal': '4', 'varUnit': '-', 'varMemo': '按入口气体速度选取，可尝试4'},
        {'varID': 'n', 'varType': '基本参数', 'varName': '速度分布指数 ', 'varVal': '0.5', 'varUnit': '-', 'varMemo': '根据计算模型选取，可尝试0.5'},
        {'varID': 'dp1', 'varType': '粒径分布', 'varName': '#1平均粒径', 'varVal': '1', 'varUnit': 'mm', 'varMemo': '#1平均粒径'},
        {'varID': 'dp1_r', 'varType': '粒径分布', 'varName': '#1平均粒径质量分数 ', 'varVal': '0.1', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp2', 'varType': '粒径分布', 'varName': '#2平均粒径', 'varVal': '15', 'varUnit': 'mm', 'varMemo': '#2平均粒径'},
        {'varID': 'dp2_r', 'varType': '粒径分布', 'varName': '#2平均粒径质量分数 ', 'varVal': '0.8', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp3', 'varType': '粒径分布', 'varName': '#3平均粒径', 'varVal': '300', 'varUnit': 'mm', 'varMemo': '#3平均粒径'},
        {'varID': 'dp3_r', 'varType': '粒径分布', 'varName': '#3平均粒径质量分数 ', 'varVal': '0.1', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp4', 'varType': '粒径分布', 'varName': '#4平均粒径', 'varVal': '0', 'varUnit': 'mm', 'varMemo': '#4平均粒径'},
        {'varID': 'dp4_r', 'varType': '粒径分布', 'varName': '#4平均粒径质量分数 ', 'varVal': '0', 'varUnit': '-', 'varMemo': '取0~1'},
        {'varID': 'dp5', 'varType': '粒径分布', 'varName': '#5平均粒径', 'varVal': '0', 'varUnit': 'mm', 'varMemo': '#5平均粒径'},
        {'varID': 'dp5_r', 'varType': '粒径分布', 'varName': '#5平均粒径质量分数 ', 'varVal': '0', 'varUnit': '-', 'varMemo': '取0~1'},
 ]

# 定义生物质气化算法参数信息
modItems['gasifi']['modInfo'] = '模型算法依据吉布斯自由能最小化原理编写'
modItems['gasifi']['modVar'] = [
        {'varID': 'ar_w', 'varType': '原料工业分析', 'varName':'收到基水分', 'varVal': '4.87', 'varUnit': '%', 'varMemo': ''},
        {'varID': 'ar_v', 'varType': '原料工业分析', 'varName':'收到基挥发分', 'varVal': '71.95', 'varUnit': '%', 'varMemo': ''},
        {'varID': 'ar_fc', 'varType': '原料工业分析', 'varName':'收到基固定碳', 'varVal': '17.25', 'varUnit': '%', 'varMemo':''},
        {'varID': 'ad_C', 'varType': '原料元素分析', 'varName':'干燥无灰基C', 'varVal': '44.25', 'varUnit': '%', 'varMemo': ''},
        {'varID': 'ad_H', 'varType': '原料元素分析', 'varName': '干燥无灰基H', 'varVal': '5.62', 'varUnit': '%', 'varMemo': ''},
        {'varID': 'ad_O', 'varType': '原料元素分析', 'varName': '干燥无灰基O', 'varVal': '43.22', 'varUnit': '%', 'varMemo': ''},
        {'varID': 'feed', 'varType': '模型参数设定', 'varName': '进料量', 'varVal': '4000', 'varUnit': 'kg/hr', 'varMemo': ''},
        {'varID': 'air', 'varType': '模型参数设定', 'varName': '进空气量', 'varVal': '5000', 'varUnit': 'm3/hr', 'varMemo': ''},
        {'varID': 'temp', 'varType': '模型参数设定', 'varName': '气化温度', 'varVal': '600', 'varUnit': '℃', 'varMemo': ''},
]

# 定义水蒸气计算参数信息
modItems['steam']['modInfo'] = '<p>该模块为IAPWS97水蒸气计算模块。</p><p>只输入压力或温度查询饱和态参数；<p>输入温度与压力查询指定状态参数。</p>'
modItems['steam']['modVar'] = [
        {'varID': 'T', 'varType': '基本参数', 'varName': '温度', 'varVal': '', 'varUnit': '℃', 'varMemo': ''},
        {'varID': 'P', 'varType': '基本参数', 'varName': '压力', 'varVal': '', 'varUnit': 'MPa', 'varMemo': ''},
]

# Debug
#print(modItems['cyclone']['modVar'])