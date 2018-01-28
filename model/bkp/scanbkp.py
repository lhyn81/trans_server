import os
import pythoncom
import win32com.client as win32

pythoncom.CoInitialize()

aspen = win32.Dispatch("Apwn.Document")
aspen.InitFromArchive2("biogasi01.bkp")

def prt_elem(obj, lv=0):
	try:
		if hasattr(obj, "Elements"):
			print("  "*lv, obj.Name)
			for o in obj.Elements:
				prt_elem(o, lv+1)
		else:
			print("!NO WAY!")
	except:
		print("  "*lv,obj.Name,"=",obj.Value)
		
def prt_node(obj, lv=0, uplm=5):
	if lv<uplm:
		try:
			if hasattr(obj, "Elements"):
				print("  "*lv, obj.Name)
				for o in obj.Elements:
					prt_node(o,lv=lv+1,uplm=uplm)
			else:
				print("!NO WAY!")
		except:
			pass

#prt_elem(aspen.Tree.Data)
#prt_node(aspen.Tree.Data,uplm=3)
#a = aspen.Tree.Findnode(r'\Data\Streams\BIOMASS\Input\ELEM\NCPSD\BIOMASS\PROXANAL\#3').Value
#str = r'\Data\Streams\BIOMASS\Input\TOTFLOW\NCPSD'

b = aspen.Tree.FindNode('\Data\Streams\OUTGAS\Output\MASSFLMX\$TOTAL').Value
print(b)