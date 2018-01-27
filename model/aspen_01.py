import os
import win32com.client as win32
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import time


def modinfo_aspen():
    mod_name = '生物质气化模型'
    mod_imageurl = ''
    mod_info = '生物质气化模型'
    mod_desp = '模型算法依据吉布斯自由能最小化原理编写'
    return [mod_name, mod_imageurl, mod_info, mod_desp]

# 定义输入变量，生成结构体.
def modx_aspen():
    modvar_type = ['原料工业分析', '原料元素分析','模型参数设定']
    modvar_data = [
        {'id': 'ar_w', 'type': '原料工业分析', 'text':'收到基水分', 'value': '4.87', 'unit': '1', 'memo': 'Disabled'},
        {'id': 'ar_v', 'type': '原料工业分析', 'text':'收到基挥发分', 'value': '71.95', 'unit': '1', 'memo': 'Disabled'},
        {'id': 'ar_fc', 'type': '原料工业分析', 'text':'收到基固定碳', 'value': '17.25', 'unit': '1', 'memo':'Disabled'},
        {'id': 'ad_C', 'type': '原料元素分析', 'text':'干燥无灰基C', 'value': '44.25', 'unit': '1', 'memo': 'Disabled'},
        {'id': 'ad_H', 'type': '原料元素分析', 'text': '干燥无灰基H', 'value': '5.62', 'unit': '1', 'memo': 'Disabled'},
        {'id': 'ad_O', 'type': '原料元素分析', 'text': '干燥无灰基O', 'value': '43.22', 'unit': '1', 'memo': 'Disabled'},
        # {'id': 'ad_N', 'type': '原料元素分析', 'text': '干燥无灰基N', 'value': '', 'unit': '1', 'memo': ''},
        # {'id': 'ad_S', 'type': '原料元素分析', 'text': '干燥无灰基S ', 'value': '', 'unit': '1', 'memo': ''},
        {'id': 'feed', 'type': '模型参数设定', 'text': '进料量', 'value': '4000', 'unit': 'kg/hr', 'memo': 'Enabled'},
        {'id': 'air', 'type': '模型参数设定', 'text': '进空气量', 'value': '5000', 'unit': 'm3/hr', 'memo': 'Enabled'},
        {'id': 'temp', 'type': '模型参数设定', 'text': '气化温度', 'value': '600', 'unit': '℃', 'memo': 'Enabled'},
    ]
    return [modvar_type, modvar_data]


def mody_aspen(x):
    import pythoncom
    pythoncom.CoInitialize()

    feed = float(x['feed'])
    air = float(x['air'])
    temp = float(x['temp'])

    aspen = win32.Dispatch('Apwn.Document')
    #time.sleep(3)
    # bkp.InitFromArchive2(os.path.abspath('Aspen\\rb.bkp'))
    # feed = bkp.Tree.FindNode('\Data\Results Summary\Stream-Sum\Stream-Sum\Table\(  H2,4)').Value
    # Airflow = np.linspace(5, 20, 10)
    # CO_frac, H2_frac = [], []
    # for airflow in Airflow:
    #     #bkp.Tree.FindNode('\Data\Streams\3\Input\TOTFLOW\MIXED').Value = airflow
    #     bkp.Tree.Data.Streams.AIRIN.Input.TOTFLOW.MIXED.Value = airflow
    #     bkp.Engine.Run2()
    #     CO_frac.append(bkp.Tree.FindNode('\Data\Results Summary\Stream-Sum\Stream-Sum\Table\(  CO,4)').Value)
    #     H2_frac.append(bkp.Tree.FindNode('\Data\Results Summary\Stream-Sum\Stream-Sum\Table\(  H2,4)').Value)
    # bkp.Close()
    # plot(Airflow,CO_frac)
    # plot(Airflow,H2_frac)
    # savefig("..//static//image//bkp//rlt.png", dpi=72)
    # #show()

    aspen.InitFromArchive2(os.path.abspath('model\\bkp\\biogasi01.bkp'))
    aspen.Tree.Data.Streams.BIOMASS.Input.TOTFLOW.NCPSD.Value = feed
    aspen.Tree.Data.Streams.O2.Input.TOTFLOW.MIXED.Value = air
    aspen.Tree.Data.Blocks.B8.Input.TEMP.Value = temp + 273
    aspen.run2()

    CO_frac = aspen.Tree.Data.Streams.OUTGAS.Output.MOLEFRAC.MIXED.CO.Value
    H2_frac = aspen.Tree.Data.Streams.OUTGAS.Output.MOLEFRAC.MIXED.H2.Value
    O2_frac = aspen.Tree.Data.Streams.OUTGAS.Output.MOLEFRAC.MIXED.O2.Value
    CH4_frac = aspen.Tree.Data.Streams.OUTGAS.Output.MOLEFRAC.MIXED.CH4.Value
    CO2_frac = aspen.Tree.Data.Streams.OUTGAS.Output.MOLEFRAC.MIXED.CO2.Value
    MassFlow = aspen.Tree.FindNode('\Data\Streams\OUTGAS\Output\MASSFLMX\$TOTAL').Value
    aspen.Close()
    #
    modvar_type = ['气体组分', '产气量']
    modvar_data = [
        {'id': 'CO_frac', 'type': '气体组分', 'text': 'CO', 'value': "%.3f" % CO_frac, 'unit': '-', 'memo': ''},
        {'id': 'H2_frac', 'type': '气体组分', 'text': 'H2', 'value': "%.3f" % H2_frac, 'unit': '-', 'memo': ''},
        {'id': 'O2_frac', 'type': '气体组分', 'text': 'O2', 'value': "%.3f" % O2_frac, 'unit': '-', 'memo': ''},
        {'id': 'CH4_frac', 'type': '气体组分', 'text': 'CH4', 'value': "%.3f" % CH4_frac, 'unit': '-', 'memo': ''},
        {'id': 'CO2_frac', 'type': '气体组分', 'text': 'CO2', 'value': "%.3f" % CO2_frac, 'unit': '-', 'memo': ''},
        {'id': 'MassFlow', 'type': '产气量', 'text': '生物质气产量', 'value': "%.3f" % MassFlow, 'unit': 'kg/hr', 'memo': ''},
    ]

    return [modvar_type, modvar_data]


