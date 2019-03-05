import time

class timer():
	def start(self):
		timestamp1 = time.time()
		self.start = round(timestamp1)
	def stop(self):
		timestamp2 = time.time()
		self.stop = round(timestamp2)
	def get_time(self):
		process_time = self.stop - self.start
		return process_time