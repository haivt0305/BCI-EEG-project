from pylsl import StreamInlet, resolve_stream

def get_response():
	# first resolve an EEG stream on the lab network
	print("looking for an EEG stream...")
	streams = resolve_stream('type', 'EEG')
	
	# create a new inlet to read from the stream
	inlet = StreamInlet(streams[0])

	while True:
		# get a new sample (you can also omit the timestamp part if you're not
		# interested in it)
		sample, timestamp = inlet.pull_sample()
		yield timestamp, sample

if __name__ == '__main__':
	for timestamp, sample in get_response():
		print(sample)
		