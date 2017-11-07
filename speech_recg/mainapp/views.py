# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import os
from django.shortcuts import render_to_response 
from wordcloud import WordCloud, STOPWORDS
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from summarizer import summarize
import glob 

from textblob import TextBlob



file_path="/home/deepika/djando-project/speech_recg/mainapp/audio"

# Create your views here.
def getlist(request):
    files = (file for file in os.listdir(file_path) if os.path.isfile(os.path.join(file_path, file)))
    return render_to_response('index.html',{'files':files})



def getfilename(request):
    fname = request.GET.get('select')
    search_text=request.GET.get('search_text')
    search_text =  search_text.encode(encoding='UTF-8')
    #result_dict = {"f" : ["first chunk text in file one jfedvdfsdfwfwf wefewfewfefffef ewfdewfweffffffffihuegftey gftgygsuyfgdsyfyfgsu yfgyufgeyfgefgeyf gewuyfgewyfgew ugfewyfgewugfewyfg yufguyfg ewuygfewyfg","second chunk text in file one"],"e" : ["first chunk text in file second","second chunk text in file second"]}
    
    result_dict = search(fname,search_text)
    return render_to_response('display.html',{'result':result_dict.items()})

def goaction(request):
    fname = request.GET.get('yo')
    print fname
    if(fname):
      action =  fname.split()[0]
      file_name = fname.split()[1]
      print 'D' * 100
      print fname
      print action

  
      if(action == "Translate"):
          print "we will show image of sentiment analysis"
          return render(request,'Translate.html')

      if(action == "Word_Cloud"):
          get_wordcloud(file_name)
          print "we will show image of sentiment analysis"
          return render(request,'Word_Cloud.html')

      if(action == "Summarize"):
          summaryList = summ(file_name)
          print summaryList
          return render_to_response('Summarize.html',{'summaryList':summaryList})

      if(action == "Sentiment_Analysis"):
          #get_sentiment(file_name)
          print "we will show image of sentiment analysis" 
          return render(request,'Sentiment_Analysis.html')
  
def get_wordcloud(filename):
    #answer = open("/home/deepika/djando-project/speech_recg/mainapp/audio/"+filename.split('.')[0]+"/"+filename.split('.')[0]+".txt",'r')
    with open("/home/deepika/djando-project/speech_recg/mainapp/audio/"+filename.split('.')[0]+"/"+filename.split('.')[0]+".txt",'r') as myFile:
      data = myFile.read().replace('\n',' ')
    wordcloud = WordCloud(stopwords=STOPWORDS,background_color='white',width=800,height=600).generate(str(data))

    fig = plt.figure(1)
    plt.imshow(wordcloud)
    plt.axis('off')
#   plt.show()
    fig.savefig("/home/deepika/djando-project/speech_recg/mainapp/static/images/wordCloud.png")
    return

def summ(filename):
    title = "Test"	

    with open("/home/deepika/djando-project/speech_recg/mainapp/audio/"+filename.split('.')[0]+"/"+filename.split('.')[0]+".txt",'r') as myFile:
      data = myFile.read().replace('\n',' ')
    answer = summarize(title,data)
    return answer


def get_dictlist(dir_name,filename,find):
    #print dir_name
    result = []
    os.chdir("/home/deepika/djando-project/speech_recg/mainapp/audio/"+dir_name)
    directory = "/home/deepika/djando-project/speech_recg/mainapp/audio/" + dir_name
    #print directory
    for searchfile in glob.glob(directory+ "/*.chunk*.txt"):
      #print searchfile
      with open(searchfile,'r') as f:
        for line in f:
          #print find
          if find in line:
            #print line
            result.append(line)
    return result

def search(filename,find):
  result = []
  response = {}
  directory = "/home/deepika/djando-project/speech_recg/mainapp/audio/"
  if filename=="ALL":
    for dir_name in os.listdir(directory): 
      if os.path.isdir("/home/deepika/djando-project/speech_recg/mainapp/audio/"+dir_name):
        temp = get_dictlist(dir_name,filename,find)
        if temp:
          response[dir_name] = temp
  else:
    dir_name = filename.split('.')[0]
    response[filename] = get_dictlist(dir_name,filename,find) 
  return response


def get_sentiment(filename):
    #with open(filename, 'r') as myfile:
    with open("/home/deepika/djando-project/speech_recg/mainapp/audio/"+filename.split('.')[0]+"/"+filename.split('.')[0]+".txt",'r') as myFile:
     text = myFile.read().replace('\n', '')
    blob = TextBlob(text)
    total = 0
    positive = 0
    negative = 0
    for sentence in blob.sentences:
        total += abs(sentence.sentiment.polarity)
        if sentence.sentiment.polarity > 0:
            positive += sentence.sentiment.polarity
        else:
            negative += abs(sentence.sentiment.polarity)
    positive_sentiment =  (positive / total) * 100
    negative_sentiment = (negative / total) * 100
    answer = []
    answer.append(positive_sentiment)
    answer.append(negative_sentiment)
    labels = ['Positive', 'Negative']
    sizes = answer
    colors = ['blue','red']
    patches, texts = plt.pie(sizes, colors=colors, shadow=True, startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig("/home/deepika/djando-project/speech_recg/mainapp/static/Sentiment.png")
