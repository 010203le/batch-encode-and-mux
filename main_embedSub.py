import os

#path and encoder setup
mkvPath = r"C:\PT\XX\_source"
subPath = r"C:\PT\XX\_temp\CHS"
outPath = r"C:\PT\XX\_encode"
vpyPath = r"C:\PT\XX\main_embed.vpy"
temp = r"C:\PT\XX\_temp"
x264 = r"C:\PT\XX\bin\x264.exe"
x264P = '--preset veryslow --crf 18 --threads 16 --deblock -1:-1 --keyint 600 --min-keyint 1 --bframes 8 --ref 13 --qcomp 0.6 --no-mbtree --rc-lookahead 70 --aq-strength 0.8 --me tesa --psy-rd 0.6:0.0 --chroma-qp-offset -1 --no-fast-pskip --colormatrix bt709 --aq-mode 3'
VSPipe = r"C:\PT\XX\vapoursynth-R57.A6\VSPipe.exe"
mkvMerge = r"C:\PT\XX\bin\mkvtoolnix-64-bit-73.0.0\mkvmerge.exe"
ffmpeg = r"C:\PT\XX\bin\ffmpeg.exe"
#output video track information setup
trackName = 'lolice-EC'
videoLang = 'jpn'
fps = '24000/1001p'

mkvCount = 0
mkvList = []
subList = []
batList = []
mergeList = []
ffmpegList = []
for root, dirs, files in os.walk(mkvPath):
    for file in files:
        if file.endswith(".mkv"):
            mkv = os.path.join(root, file)
            mkvList.append(mkv)
            mkvCount = mkvCount + 1

for root, dirs, files in os.walk(subPath):
    for file in files:
        if file.endswith(".ass"):
            sub = os.path.join(root, file)
            subList.append(sub)

with open(vpyPath, 'r') as f:
    vpy = f.read()
    vpy = vpy.split('#BATCH')
    f.close()

for i in range(mkvCount):
    batList.append('"'+VSPipe+'"'+' "'+os.path.join(temp, 'batch'+str(i+1)+'.vpy')+'" - --y4m | '+'"'+x264+'" '+x264P+' --demuxer y4m -o "'+os.path.join(temp, 'batch'+str(i+1)+'_out.avc')+'" -')
    mergeList.append('"'+mkvMerge+'" -o "'+os.path.join(outPath, 'batch'+str(i+1)+'_out.mkv')+'" -D -S -T -M "'+mkvList[i]+'" "'+os.path.join(temp, 'batch'+str(i+1)+'_out.avc')+'" --language 0:"' + videoLang + '" --track-name 0:"' + trackName + '" --default-duration 0:'+fps)
    ffmpegList.append('"'+ffmpeg+'" -i "'+os.path.join(outPath, 'batch'+str(i+1)+'_out.mkv')+'" -c copy "'+os.path.join(outPath, 'batch'+str(i+1))+'_out.mp4'+'"')
    with open(os.path.join(temp, 'batch'+str(i+1)+'.vpy'), 'w') as f:
        f.write(vpy[0]+'\na=r"'+mkvList[i]+'"\ns=r"'+subList[i]+'"\n'+vpy[2])
        f.close()
        i=i+1

with open( 'batch.bat', 'w') as f:
    f.write('@echo off\n')
    for i in range(mkvCount):
        f.write(batList[i]+'\n')
        f.write(mergeList[i]+'\n')
        f.write(ffmpegList[i]+'\n')
        i=i+1
    f.write('\npause')
    f.close()
