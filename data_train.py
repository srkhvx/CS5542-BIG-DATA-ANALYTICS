filename = 'Flickr8k/Flickr_8k.trainImages.txt'

def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

doc = load_doc(filename)
train = list()
for line in doc.split('\n'):
    identifier = line.split('.')[0]
    train.append(identifier)
print('Dataset: %d' % len(train))


doc = load_doc('descriptions.txt')
train_descriptions = dict()
for line in doc.split('\n'):
    # split line by white space
    tokens = line.split()

    # split id from description
    image_id, image_desc = tokens[0], tokens[1:]

    # skip images not in the set
    if image_id in dataset:
        if image_id not in descriptions:
            train_descriptions[image_id] = list()

        # wrap description in tokens
        desc = 'startseq ' + ' '.join(image_desc) + ' endseq'

        # store
        train_descriptions[image_id].append(desc)

        print('Descriptions: train=%d' % len(train_descriptions))