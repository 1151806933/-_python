"""Subclass of MyFrame2, which is generated by wxFormBuilder."""

import wx
import _2

# Implementing MyFrame2
class MyProject1MyFrame2( _2.MyFrame2 ):
	def __init__( self, parent ):
		_2.MyFrame2.__init__( self, parent )

	def onclick(self, event):
		#执行按钮，展示数据到文本框
		self.OutPutValue()

	#展示数据
	def OutPutValue(self):
		value = self.putValueInLable(self.m_textCtrl26)
		value1 = self.putValueInLable(self.m_textCtrl27)
		value2 = self.putValueInLable(self.m_textCtrl28)
		value3 = self.putValueInLable(self.m_textCtrl29)
		#获取输入框中的数据，执行要操作的程序，发送到文本展示框
		result0=self.TcpHostScan(value)
		result1=self.ServerScan(value1)
		result2 = self.SystemScan(value2)
		result3 = self.AllScan(value3)
		results = [result0,result1,result2,result3]
		for result in results:
			if result is not None:
				self.m_richText1.WriteText("====================")
				self.m_richText1.WriteText(str(result))
				self.m_richText1.WriteText("====================")
	#获得输入框
	def putValueInLable(self,name) -> str:
		self.name = name
		value = self.name.GetLineText(0)
		return value

	def TcpHostScan(self,pram):
		import sys
		import nmap
		nm = nmap.PortScanner()
		nm.scan(hosts=pram, arguments="-sT")
		a = []
		for host in nm.all_hosts():
			a.append("--------------"+
					("Host : %s(%s)" % (host, nm[host].hostname()))+
					("State:%s" % nm[host].state()))
		return a

	def ServerScan(self,pram):
		import nmap
		nm = nmap.PortScanner()
		nm.scan(hosts=pram, arguments="sV")
		for host in nm.all_hosts():
			for k, v in nm[host].items():
				if k == "tcp":
					print("-----------------tcp--------------------")
					b = []
					for proto in nm[host].all_protocols():
						lport = nm[host][proto].keys()
						for port in lport:
							b.append("port："+port+
								  "name:"+str(nm[host][proto][port]["name"])+
								  "product："+str(nm[host][proto][port]["product"])+
								  "version:"+str(nm[host][proto][port]["version"])+
								  "extrainfo:"+str(nm[host][proto][port]["extrainfo"])
								  +"cpe:"+str(nm[host][proto][port]["cpe"]))
					return b
				else:
					return (k, v)


	def SystemScan(self,pram):
		# 基于nmap的操作系统 的扫描
		import nmap
		nm = nmap.PortScanner()
		nm.scan(hosts=pram, arguments="-O")
		c=[]
		for host in nm.all_hosts():
			for k, v in nm[host].items():
				if k == "osmatch":
					dic = v[0]
					print("----------------------------------------------")
					for x, y in dic.items():
						if x == "osclass":
							c.append("=====================osclass==================")
							for m, n in y[0].items():
								c.append(str(m)+":"+str(n))
						else:
							c.append(str(x)+ ":"+str(y))
				else:
					...
			return c

	def AllScan(self,pram):
		import nmap
		d=[]
		nm = nmap.PortScanner()
		nm.scan(pram, "80")
		for host in nm.all_hosts():
			for name, stat in nm[host].items():
				d.append(str(name)+":"+str(stat))
		return d


from tools import tools
tools(MyProject1MyFrame2)