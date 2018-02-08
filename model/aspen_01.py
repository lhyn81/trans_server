import os
import win32com.client as win32
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
import time

def mody_aspen(x):

    import pythoncom
    pythoncom.CoInitialize()

    ar_w = float(x['ar_w'])
    ar_v = float(x['ar_v'])
    ar_fc = float(x['ar_fc'])
    ad_C = float(x['ad_C'])
    ad_H = float(x['ad_H'])
    ad_O = float(x['ad_O'])

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
    # 设置工业分析
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\PROXANAL\#0').Value = ar_w
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\PROXANAL\#1').Value = ar_fc
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\PROXANAL\#2').Value = ar_v
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\PROXANAL\#3').Value = 100 - ar_w - ar_fc - ar_v

    # 设置元素分析
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\ULTANAL\#6').Value = ad_O
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\ULTANAL\#1').Value = ad_C
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\ULTANAL\#2').Value = ad_H
    aspen.Tree.FindNode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\ULTANAL\#0').Value = 100 - ad_C - ad_H - ad_O

    # 设置输入参数
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
    modvar_data = [
        {'varID': 'CO_frac', 'varType': '气体组分', 'varName': 'CO含量', 'varVal': "%.3f" % CO_frac, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'H2_frac', 'varType': '气体组分', 'varName': 'H2含量', 'varVal': "%.3f" % H2_frac, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'O2_frac', 'varType': '气体组分', 'varName': 'O2含量', 'varVal': "%.3f" % O2_frac, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'CH4_frac', 'varType': '气体组分', 'varName': 'CH4含量', 'varVal': "%.3f" % CH4_frac, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'CO2_frac', 'varType': '气体组分', 'varName': 'CO2含量', 'varVal': "%.3f" % CO2_frac, 'varUnit': '-', 'varMemo': ''},
        {'varID': 'MassFlow', 'varType': '产气量', 'varName': '生物质气产量', 'varVal': "%.3f" % MassFlow, 'varUnit': 'kg/hr', 'varMemo': ''},
    ]

    return modvar_data


