from pypdf import PdfReader
from gtts import gTTS
from pydub import AudioSegment
from io import BytesIO
import threading


def text_to_speech(text,result_list):
    index=text[0]
    audio=gTTS(text=text[1],lang="en",slow=False)
    audio_bytes = BytesIO()
    audio.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    result_list.append([index,AudioSegment.from_file(audio_bytes, format="mp3")])

reader = PdfReader("../concall_pdfs/globusSprits2024Concalltransscript.pdf")
number_of_pages = len(reader.pages)

pages_list=[]
for i in range(0,number_of_pages):
    pages_list.append(reader.pages[i])
    
pages_text=[]
for i in range(0,number_of_pages):
    pages_text.append(pages_list[i].extract_text().replace("\n",""))


pages_text_With_index=[]
counter=0
for i in pages_text:
    pages_text_With_index.append([counter,i])
    counter+=1

result_list=[]
threads=[]
text_text=[[0,"hello Nice to meet you Yashas"],[1,"Today is a nice day"],[2,"What do you mean"],[3,"by all that you say"]]
for i in pages_text_With_index:
    t=threading.Thread(target=text_to_speech,args=(i,result_list))
    threads.append(t)
    t.start()
for thread in threads:
    thread.join()

result_list.sort()

audio_list=[]
for i in result_list:
    audio_list.append(i[1])

a=AudioSegment.silent(duration=0)
for i in audio_list:
    a=a+i
