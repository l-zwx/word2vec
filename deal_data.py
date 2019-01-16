import jieba
#获得各类数据
sport=[]
entertainment=[]
file_soprts = open(r'C:\Users\nlp\Desktop\toutiao-text-classfication-dataset-master\toutiao-text-classfication-dataset-master\toutiao_cat_data\toutiao_cat_data-a-sports-cut.txt', 'a+', encoding='utf-8')
file_entertainment = open(r'C:\Users\nlp\Desktop\toutiao-text-classfication-dataset-master\toutiao-text-classfication-dataset-master\toutiao_cat_data\toutiao_cat_data-a-entertainment-cut.txt', 'a+', encoding='utf-8')
stop_words_file='data\stop_words.txt'
stopwords_set = set()
#加载停用词
with open(stop_words_file, 'r', encoding='utf-8') as stop_words:
    for word in stop_words:
        stopwords_set.add(word.strip('\n'))

with open(r'C:\Users\nlp\Desktop\toutiao-text-classfication-dataset-master\toutiao-text-classfication-dataset-master\toutiao_cat_data\toutiao_cat_data-a.txt', 'r', encoding='utf-8') as f:
    for line in f:
        lineList = line.split('_!_')
        if(lineList[0]=='sports'):
            sport.append(lineList[1])
        if(lineList[0]=='entertainment'):
            entertainment.append(lineList[1])
for data in entertainment:
    # print(data)
    line_words = jieba.cut(data)
    for new_word in line_words:
        if new_word not in stopwords_set:
            if new_word > u'\u4e00' and new_word <= u'\u9fa5':
                file_entertainment.write(new_word+" ")

    file_entertainment.write('\n')
# for data in entertainment:
#     print(data)
#     file_entertainment.write(data+ '\n')

