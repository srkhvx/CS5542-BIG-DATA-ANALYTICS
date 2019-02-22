import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
filename = "Flickr8k/Flickr8k.token.txt"
file = open(filename, 'r')
doc = file.read()

# Creating Dictionary
descriptions = dict()
for line in doc.split('\n'):
    # split line by white space
    if(line==" "):
        break
    tokens = line.split()
    # take the first token as image id, the rest as description
    if len(tokens)==0:
        break
    image_id, image_desc = tokens[0], tokens[1:]
    #print(image_id," ",image_desc )
    # extract filename from image id
    image_id = image_id.split('.')[0]

    # convert description tokens back to string
    image_desc = ' '.join(image_desc)
    if image_id not in descriptions:
        descriptions[image_id] = list()
    descriptions[image_id].append(image_desc)


# prepare translation table for removing punctuation
table = str.maketrans('', '', string.punctuation)
for key, desc_list in descriptions.items():
    for i in range(len(desc_list)):
        desc = desc_list[i]
        # tokenize
        desc = desc.split()
        # convert to lower case
        desc = [word.lower() for word in desc]
        # remove punctuation from each token
        desc = [w.translate(table) for w in desc]
        # remove hanging 's' and 'a'
        desc = [word for word in desc if len(word)>1]
        # remove tokens with numbers in them
        desc = [word for word in desc if word.isalpha()]
        # store as string
        desc_list[i] =  ' '.join(desc)


# Create a list of all the training captions
all_train_captions = []
for key, val in descriptions.items():
    for cap in val:
        example_sent = str(cap)
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(example_sent)
        porter = PorterStemmer()

        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        cap = ""
        for w in word_tokens:
            if w not in stop_words:
                if w is str.isalpha():
                    cap+=porter.stem(str(w).lower())+","
        all_train_captions.append(str(key)+" " +cap)

descrip=open("Description.txt","w")
descrip.write("\n".join(all_train_captions))
descrip.close()

