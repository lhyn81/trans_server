import os
import win32com.client as win32
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

aspen = win32.Dispatch('Apwn.Document')
aspen.InitFromArchive2(os.path.abspath('D:\\DEV\\Python\\Aspen\\rb.bkp'))
feed = aspen.Tree.FindNode('\Data\Results Summary\Stream-Sum\Stream-Sum\Table\(  H2,4)').Value
Airflow = np.linspace(5, 20, 10)
CO_frac, H2_frac = [], []
for airflow in Airflow:
    #aspen.Tree.FindNode('\Data\Streams\3\Input\TOTFLOW\MIXED').Value = airflow
    aspen.Tree.Data.Streams.AIRIN.Input.TOTFLOW.MIXED.Value = airflow
    aspen.Engine.Run2()
    CO_frac.append(aspen.Tree.FindNode('\Data\Results Summary\Stream-Sum\Stream-Sum\Table\(  CO,4)').Value)
    H2_frac.append(aspen.Tree.FindNode('\Data\Results Summary\Stream-Sum\Stream-Sum\Table\(  H2,4)').Value)
aspen.Close()
plot(Airflow,CO_frac)
plot(Airflow,H2_frac)
savefig("..//static//image//aspen//rlt.png", dpi=72)
#show()