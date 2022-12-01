import pvleopard
import csv
#import cv2
import pandas as pd
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip


def show():
      dfi = pd.read_csv('transcript.csv')
      dfi['word']=dfi.iloc[:,0]
      dfi['start']=dfi.iloc[:,1]
      dfi['end']=dfi.iloc[:,2]
      dfi['confidence']=dfi.iloc[:,3]
      dfi['start']=dfi['start'].round(decimals=2)
      dfi['end']=dfi['end'].round(decimals=2) 

      # texts = dfi.word
      # length=len(texts)
      # t=0
      # txt_clips = []
      # for text,i in zip(texts,range(0,length)):
      #       txt_clip = TextClip(text,fontsize = 40, color='black',bg_color='white')
      #       txt_clip = txt_clip.set_start(dfi.start[i])
      #       txt_clip = txt_clip.set_pos('top').set_duration(dfi.end[i])
      #       #txt_clips.append(txt_clip) 
      #       final=CompositeVideoClip([final,txt_clip])
      # #final=CompositeVideoClip([c1,txt_clips[0],txt_clips[1],txt_clips[2],txt_clips[3],txt_clips[4],txt_clips[5],txt_clips[6],txt_clips[7],txt_clips[8],txt_clips[9],txt_clips[10]])
      
      # final.write_videofile("TEXT.mp4")
      

      generator = lambda txt: TextClip(txt, font='Arial', fontsize=24, color='black',bg_color='white')
      #subs = [((0, 4), 'subs1'),((4, 9), 'subs2'),((9, 12), 'subs3'),((12, 16), 'subs4')]
      subs = []
      # print(dfi)
      for i in range(0,len(dfi.index)):
                  k=((dfi.iloc[i,1],dfi.iloc[i,2]),dfi.iloc[i,0])
                  subs.append(k)
                  # print(k)
      subtitles = SubtitlesClip(subs, generator)

      video = VideoFileClip("lec.mp4")
      result = CompositeVideoClip([video, subtitles.set_pos(('top'))])

      result.write_videofile("TEXT.mp4")


def audio_to_text():
      leopard=pvleopard.create(access_key="p0UW7GnskdeCe9pFxV7N+6aOaQgUu++EbUFgE80k6M1dWcWZzhKlpw==")
      transcript, words=leopard.process_file("C:\\Users\\Shaurya Vardhan\\Desktop\\Project\\MinorProject\\new1.wav")
      with open("transcript.csv",'w',newline="") as f:
        writer=csv.writer(f)
        writer.writerow(["word","start","end","confidence"])
        for word in words:
              writer.writerow([word.word,word.start_sec,word.end_sec,word.confidence])
              # sec=sec+(word.end_sec-word.start_sec)
              # print(
              # "{word=\"%s\" start_sec=%.2f end_sec=%.2f confidence=%.2f}"
              # % (word.word, word.start_sec, word.end_sec, word.confidence)) 

      leopard.delete();

# audio_to_text()    

# show()
