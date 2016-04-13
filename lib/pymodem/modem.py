"""
AUTHORS: Abdoulaye KAMA <abdoulayekama@gmail.com>

"""

from serial import Serial

class Modem:
	def __init__(self, port="/dev/ttyUSB0", baudrate=9600, timeout=1):
		self.port = port
		self.baudrate = baudrate
		self.timeout = timeout
		self.modem = ""

	def open(self):
		try:
			if self.port != "":
				self.modem = Serial(self.port, baudrate=self.baudrate, timeout=self.timeout)
		except:
			print "impossible de se connecter\n"
		
	def close(self):
		try:
			if self.modem != "":
				self.modem.close()
		except:
			print "impossible de fermer le port"
	def write(self, commande):
		if self.modem != "":
			commande = commande + "\r\n"
			self.modem.write(commande)
			self.modem.flush()
	def readLine(self):
		data = ""
		while self.modem.isWaiting()>0:
			data += self.modem.readline()
		return data
			

	def sendSMS(self, msg="", destinataire=""):
		self.write("AT+CMGF=1")
		self.write("AT+CMGS=\"" + destinataire + "\"")
		self.write(msg)
		self.write(ch(26))

	def getSMS(self, id_sms):
		self.write("AT+CMGF=1")
		self.write("AT+CMGR="+id_sms)

	def getAllSMS(self):
		self.write("AT+CMGF=1")
		self.write("AT+CMGL=\"ALL\"")
		msgs = self.readLine()
		print msgs
		return msgs

	def getUnreadSMS(self):
		self.write("AT+CMGF=1")
                self.write("AT+CMGL=\"REC UNREAD\"")
                msgs = self.readLine()
                print msgs
                return msgs

	def getReadSMS(self):
		self.write("AT+CMGF=1")
                self.write("AT+CMGL=\"REC READ\"")
                msgs = self.readLine()
                print msgs
                return msgs

	def getSentSMS(self):
		self.write("AT+CMGF=1")
                self.write("AT+CMGL=\"STO SENT\"")
                msgs = self.readLine()
                print msgs
                return msgs
	
	def getUnSentSMS(self):
                self.write("AT+CMGF=1")
                self.write("AT+CMGL=\"STO UNSENT\"")
                msgs = self.readLine()
                print msgs
                return msgs

	def deleteSMS(self, index, storage=0):
		self.write("AT+CMGF=1")
                self.write("AT+CMGD=" + index + "," + storage)
                msgs = self.readLine()
                print msgs
                return msgs

	def deleteAllSMS(self, index, storage=0):
                self.write("AT+CMGF=1")
                self.write("AT+CMGD=1,4")
                msgs = self.readLine()
                print msgs
                return msgs
	def getIMEI(self):
		self.write("AT+CGSN")
		msg = self.readLine()
		print msg
		return msg

	def getIMSI(self):
		self.write("AT+CIMI")
		msg = self.readLine()
                return msg
	def getCID(self):
		self.write("AT+CCID")
		return self.readLine()

	def getManufacturerId(self):
		self.write("AT+CGMI")
		return self.readLine()

	def getModelId(self):
		self.write("AT+CGMM")
		return self.readLine()
	
	def getRevisionSoft(self):
		"""la version du logiciel"""
		self.write("AT+CGMR")
		return self.readLine()

	def getFunctions(self):
		"""les fonctionnalites supportees par le modem"""
		self.write("AT+GCAP")
		return self.readLine()

	
	def getNumber(self):
		"""numero de telephone"""
		self.write("AT+CNUM")
		return self.readLine()	

	def enterPin(self, pin="", puk=""):
		if pin != "":
			self.write("AT+CPIN="+pin)	
			return self.readLine()
		else:
			return "pas de pin"


class GPSModem(Modem):
	def __init__(self, port="/dev/ttyUSB0", baudrate=9600, timeout=1):
		GPSModem.__init__(self, port, baudrate, timeout)

	def 
	
	
