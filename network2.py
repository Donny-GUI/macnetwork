import os
from sh import arp



class NetworkComputer:
	
	def __init__(self, computer_name, address, mac, interface, connection_type):
		
		self.computer_name = computer_name
		self.address = address
		self.mac = mac
		self.interface = interface
		self.connection_type = connection_type

class Network:
	
	def __init__(self):

		self.network_file = ".network"
		self.get_user_command = "'arp -a' > .network"
		self.update()
		self.arp = arp("-a")
		self.computers = {}

		for x in self.arp:
			y = str(x)
			y.strip()
			properties = y.split(" ")
			connection = None
			for prop in properties:
				if prop.startswith("perm"):
					connection = "permanent ethernet"
			name = properties[0]
			address = properties[2][1:-1]
			mac = properties[4]
			interface = properties[6]
			if connection is None:
				connection = properties[6]
			self.computers[name] = NetworkComputer(name, address, mac, interface, connection)

	def update(self):

		try:os.system("rm -r .network")
		except:pass
		os.system(f"{self.get_user_command}")
		with open(self.network_file, "r") as wfile:
			lines = wfile.readlines()
		for line in lines:lines.split(" ")
		mylines = lines
		for line in lines:
			for word in line:
				match word:
					case "at":mylines.remove(word)
					case "on":mylines.remove(word)
					case "ifscope":mylines.remove(word)
					case _:continue
		for line in mylines:
			user = NetworkComputer(line[0],line[1],line[2], line[3], line[4])
			self.computers[line[0]] = user


	def show(self,what="address"):

		computers = self.computers.keys()
		for x in computers:
			print(x)

network = Network()
network.show()

pprint(network.computers)
