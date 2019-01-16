from gensim.models import FastText
sentences = [["你", "是", "谁"], ["我", "是", "中国人"]]
model = FastText(sentences,  size=4, window=3, min_count=1, iter=10,min_n = 3 , max_n = 6,word_ngrams = 1)
#print(model.wv.most_similar("中国"))
print(model.wv.__getitem__('中国'))
print(model.wv.__getitem__('中国人'))
