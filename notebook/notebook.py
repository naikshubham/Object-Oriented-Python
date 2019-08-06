import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
	'''Represent a note in the notebook. Match against a string in searches and store tags for each note'''
	def __init__(self, memo, tags=''):
		"""initialize a note with memo and optional space-seperated tags.Automatically set the note's creation date and a unique id"""
		self.memo = memo
		self.tags = tags 
		self.creation_date = datetime.date.today()
		global last_id
		last_id += 1
		self.id = last_id
		
	def match(self, filter):
		'''determine if the note matches the filter text.Return True 
		if it matches , false otherwise'''
	
		return filter in self.memo or filter in self.tags
		
		
class Notebook:
	'''Represents a collection of notes that can be tagged, modified & searched'''
	def __init__(self):
		self.notes= []
		
	def new_note(self, memo, tags=''):
		'''create a new note and add it to a list'''
		self.notes.append(Note(memo, tags))
	
	def modify_memo(self, note_id, memo):
		'''find the note with the given id and change its memo
		to the given value'''
		#self._find_note(note_id).memo = memo  ## optimized
		#OR
		note = self._find_note(note_id)
		if note:
			note.memo = memo
			return True
		return False
		#OR
		#for note in self.notes:
		#	if note.id == note_id:
		#		note.memo = memo
		#		break
	
	def modify_tags(self, note_id, tags):
		'''find the note with the given id and change its tags 
		to the given value'''
		for note in self.notes:
			if note.id == note_id:
				note.tags = tags
				break
				
	def search(self, filter):
		'''find all notes that match the given filter string'''
		return [note for note in self.notes if note.match(filter)]
				
	def _find_note(self, note_id):
		'''locate the note with the given id'''
		for note in self.notes:
			if str(note.id) == str(note_id):
				return note
		return None
		
	
		
