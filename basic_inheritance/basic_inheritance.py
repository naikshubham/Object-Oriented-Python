		
class ContactList(list):
	def search(self, name):
		'''return all contacts that contain the search value in their name'''
		self.matching_contacts = []
		for contact in self:
			if name in contact.name:
				self.matching_contacts.append(contact)
		return self.matching_contacts
		
class Contact:
	#all_contacts = []
	all_contacts = ContactList()
	
	def __init__(self, name, email):
		self.name = name
		self.email = email
		#Contact.all_contacts.append(self)
		self.all_contacts.append(self)

class Supplier(Contact):
	def order(self, order):
		print("If this were a real system we would send {} order to {}".format(order, self.name))
		
