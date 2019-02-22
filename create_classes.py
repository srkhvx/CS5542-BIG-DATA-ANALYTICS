import shutil, os

filename = "Description.txt"
file = open(filename, 'r')
doc = file.read()

# Creating Dictionary
descriptions = dict()
kids_file=open("playing.txt","w")
flower_file=open("flower.txt","w")
men_file=open("men.txt","w")
dog_file=open("dog.txt","w")
sport_file=open("sport.txt","w")
for line in doc.split('\n'):
    if(len(line)==0):
        break
    file_name=line.split(" ")[0]
    if(("boy" in str(line)) & ("play" in str(line)) | ("girl" in str(line)) & ("play" in str(line)) | ("people" in str(line)) & ("play" in str(line))):
        print(line)
        kids_file.write(line+"\n")
        shutil.copy("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/"+file_name+".jpg", "C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/train/playing")  if os.path.isfile("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name+ ".jpg") else None
    if (("man" in str(line)) | ("men" in str(line)) | ("guys" in str(line))):
        print(line)
        men_file.write(line+"\n")
        shutil.copy("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name + ".jpg", "C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/train/men")  if os.path.isfile("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name+ ".jpg") else None
    if ((("dog" in str(line)) & ("play" in str(line))) | (("dog" in str(line)) | ("run" in str(line))) | ("dog" in str(line)) & ("run" in str(line))):
        print(line)
        dog_file.write(line+"\n")
        shutil.copy("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name + ".jpg","C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/train/dog")  if os.path.isfile("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name+ ".jpg") else None
    if (("rose" in str(line)) | (("flower" in str(line) )&("dress" not in str(line))) | ("tulip" in str(line))):
        print(line)
        flower_file.write(line+"\n")
        shutil.copy("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name + ".jpg","C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/train/flower")  if os.path.isfile("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name+ ".jpg") else None
    if (("sport" in str(line)) & (("hockey" in str(line) )|("football" not in str(line))) | (("soccer" in str(line)) & ("game" in str(line)))):
        print(line)
        sport_file.write(line+"\n")
        shutil.copy("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name + ".jpg","C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/train/sport") if os.path.isfile("C:/Users/srkro/Desktop/Big Data/Lab Assignment 1/LAB 1/Flickr8k/Flicker8k_Dataset/" + file_name + ".jpg") else None


flower_file.close()
men_file.close()
dog_file.close()
kids_file.close()
sport_file.close()