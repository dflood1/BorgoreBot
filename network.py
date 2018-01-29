import sys
import numpy as np
from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, LSTM, Dropout, TimeDistributed
from keras.layers.core import Dense, Activation, Dropout, RepeatVector
from keras.optimizers import RMSprop
import pickle

def preprocess_line(x):
    return list(map((lambda y: "\n" if(y=="NEWLINE") else y),x.decode("utf-8").strip().split("BREAK")))

def build_data_and_labels(sequence_length):
    lyrics = list(map(preprocess_line,open(file_path,"r").readlines()))
    words = sorted(list(set([y for x in lyrics for y in x])))
    words_indices = dict((w,i) for i, w in enumerate(words))
    indices_words = dict((i,w) for i, w in enumerate(words))

    pre_data = [x[:-1] for x in lyrics]
    pre_labels = [x[-1] for x in lyrics]

    #print("len(pre_data): ", len(pre_data))
    #print("len(pre_labels): ", len(pre_labels))
    #print("pre_data[0]: ",pre_data[0])
    #print("pre_labels[0]: ",pre_labels[0])

    data = np.zeros((len(pre_data),int(sequence_length)-1,len(words)),dtype=np.bool)
    labels = np.zeros((len(pre_labels),len(words)),dtype=np.bool)

    print("data.shape: ", data.shape)
    #print("labels.shape: ", labels.shape)

    for i, d in enumerate(pre_data):
        for t, w in enumerate(d):
            data[i, t, words_indices[w]] = 1
        labels[i, words_indices[pre_labels[i]]] = 1

    #print("data[100]: ",data[0])
    #print("labels[100]: ",labels[0])

    return (data,labels)

def build_basic_model(data,labels):
    model = Sequential()
    model.add(LSTM(128,input_shape=(data.shape[1:])))
    model.add(Dropout(0.2))
    model.add(Dense(labels.shape[1],activation="softmax"))
    #model.add(Dense(len(data)))
    #model.add(Activation("softmax"))
    model.compile(loss="categorical_crossentropy",optimizer=RMSprop(lr=0.01),metrics=["accuracy"])
    history = model.fit(data,labels,validation_split=0.05,verbose=1,batch_size=128,epochs=20,shuffle=True).history
    return (model,history)

def save_model(model,model_path,history,history_path):
    model.save(model_path)
    pickle.dump(history,open(history_path,"wb"))

def load_model(model_path,history_path):
    model = load_model(model_path)
    history = pickle.load(open(history_path,"r"))
    return (model,history)

sequence_length = sys.argv[1]
base_path = "/home/eherbert/Misc/BorgoreBot/"
file_path = base_path + "data/encoded_" + sequence_length + "words.txt"
model_path = base_path + "models/model_" + sequence_length + "words.h5"
history_path = base_path + "history/history_" + sequence_length + "words.p"

(data,labels) = build_data_and_labels(sequence_length)
(model,history) = build_basic_model(data,labels)
save_model(model,model_path,history_history_path)
