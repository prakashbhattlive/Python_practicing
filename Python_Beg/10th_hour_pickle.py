import pickle
#l = [10,30,50,70]
#file = open("write_data.txt","wb")
#pickle.dump(l,file)
#file.close()

file1 = open("write_data.txt","rb")
l1 = pickle.load(file1)
print(l1)