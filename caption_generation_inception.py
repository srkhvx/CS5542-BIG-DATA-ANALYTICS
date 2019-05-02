from pickle import load

from keras import Model
from keras.layers import Add
from numpy import argmax
from keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras.applications import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img


# extract features from each photo in the directory
def extract_features(filename):
	# load the model
	#model = VGG16()
	model=InceptionV3()
	# load the photo

	image=load_img(filename,target_size=(299, 299))
	# convert the image pixels to a numpy array
	image = img_to_array(image)
	# reshape data for the model
	image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
	# prepare the image for the VGG model
	image = preprocess_input(image)
	# get features
	feature = model.predict(image, verbose=0)
	return feature

# map an integer to a word
def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None

# generate a description for an image
def generate_desc(model, tokenizer, photo, max_length):
	# seed the generation process
	in_text = 'startseq'
	# iterate over the whole length of the sequence
	for i in range(max_length):
		# integer encode input sequence
		sequence = tokenizer.texts_to_sequences([in_text])[0]
		# pad input
		sequence = pad_sequences([sequence], maxlen=max_length)
		# predict next word
		yhat = model.predict([photo,sequence], verbose=0)
		# convert probability to integer
		yhat = argmax(yhat)
		# map integer to word
		word = word_for_id(yhat, tokenizer)
		# stop if we cannot map the word
		if word is None:
			break
		# append as input for generating the next word
		in_text += ' ' + word
		# stop if we predict the end of the sequence
		if word == 'endseq':
			break
	return in_text

# load the tokenizer
tokenizer = load(open("tokenizer.pkl", 'rb'))
# pre-define the max sequence length (from training)
max_length = 34
# load the model
model = load_model("model_inception1.h5")
model2 = load_model("model_inception2.h5")
model3 = load_model("model_inception3.h5")
model4 = load_model("model_inception4.h5")
model5 = load_model("model_inception5.h5")
model6 = load_model("model_inception6.h5")
model7 = load_model("model_inception7.h5")
model8 = load_model("model_inception8.h5")
model9 = load_model("model_inception9.h5")
model10 = load_model("model_inception10.h5")
model11 = load_model("model_inception11.h5")
model12 = load_model("model_inception12.h5")
model13 = load_model("model_inception13.h5")
model14 = load_model("model_inception14.h5")
model15 = load_model("model_inception15.h5")
model16 = load_model("model_inception16.h5")
model17 = load_model("model_inception17.h5")
model18 = load_model("model_inception18.h5")
model19 = load_model("model_inception19.h5")


# load and prepare the photograph
photo = extract_features("example1.jpg")
# generate description
description = generate_desc(model, tokenizer, photo, max_length)
description2 = generate_desc(model2, tokenizer, photo, max_length)
description3 = generate_desc(model3, tokenizer, photo, max_length)
description4 = generate_desc(model4, tokenizer, photo, max_length)
description5 = generate_desc(model5, tokenizer, photo, max_length)
description6 = generate_desc(model6, tokenizer, photo, max_length)
description7 = generate_desc(model7, tokenizer, photo, max_length)
description8 = generate_desc(model8, tokenizer, photo, max_length)
description9 = generate_desc(model9, tokenizer, photo, max_length)
description10 = generate_desc(model10, tokenizer, photo, max_length)
description11 = generate_desc(model11, tokenizer, photo, max_length)
description12 = generate_desc(model12, tokenizer, photo, max_length)
description13 = generate_desc(model13, tokenizer, photo, max_length)
description14 = generate_desc(model14, tokenizer, photo, max_length)
description15 = generate_desc(model15, tokenizer, photo, max_length)
description16 = generate_desc(model16, tokenizer, photo, max_length)
description17 = generate_desc(model17, tokenizer, photo, max_length)
description18 = generate_desc(model18, tokenizer, photo, max_length)
description19 = generate_desc(model19, tokenizer, photo, max_length)
print("mode 1: ",description)
print("mode 2: ",description2)
print("mode 3: ",description3)
print("mode 4: ",description4)
print("mode 5: ",description5)
print("mode 6: ",description6)
print("mode 7: ",description7)
print("mode 8: ",description8)
print("mode 9: ",description9)
print("mode 10: ",description10)
print("mode 11: ",description11)
print("mode 12: ",description12)
print("mode 13: ",description13)
print("mode 14: ",description14)
print("mode 15: ",description15)
print("mode 16: ",description16)
print("mode 17: ",description17)
print("mode 18: ",description18)
print("mode 19: ",description19)
print("mode 19: ",description19)