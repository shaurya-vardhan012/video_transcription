import os
def video_to_audio():
    # print("Inside the func")
    ouput_file="new1.wav"
    file=os.listdir("./")
    print(file)
    # cmd="ffmpeg -i {} {}".format(file[0],ouput_file)
    # os.popen(cmd)
    for f in file:
        if f.lower()[-3:]=="mp4":
            cmd="ffmpeg -i {} {}".format(f,ouput_file)
            os.popen(cmd)
# video_to_audio()