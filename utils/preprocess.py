# -*- coding: utf-8 -*-
import os
import codecs
import jieba

SEP = os.sep
DATAPATH = './data'
EXAMPLEFILE = '赌局.txt'
STOPWORDSFILE = './stopwords.txt'

def echo():
    print("hey what's up?")

# =============================================================================
# 读取一个文件的数据   
# =============================================================================
def read_data(data_file=EXAMPLEFILE):
    fp = codecs.open(os.path.join(DATAPATH, data_file), 'r', encoding='utf-8')
    lines = fp.readlines()
    fp.close()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
#    return ''.join(raw_data)
    return ''.join(lines)

# =============================================================================
# 读取所有文件的数据
# =============================================================================
def read_data_all(data_path=DATAPATH):
    raw_data = []
    files = os.listdir(data_path)
    for file in files:
         data = read_data(file)
         raw_data.append(data)
    return raw_data

# =============================================================================
# 将 lines 进行切词和去除停用词
# =============================================================================
def cut_and_delete(lines, sw_path=STOPWORDSFILE):
    stopwords = []
    if(os.path.exists(sw_path)):
        fp_sw = codecs.open(sw_path, 'r', encoding='utf-8')
        stopwords = fp_sw.readlines()
        fp_sw.close()
    
    for i in range(len(stopwords)):
        stopwords[i] = stopwords[i].strip()
    
    lines_cd = []
    for line in lines:    
        segments = jieba.lcut(line.strip(), cut_all=False)   
        segment_cd = []
        for segment in segments:
            if(segment not in stopwords):
                segment_cd.append(segment)
        lines_cd.append(segment_cd)
    return lines_cd