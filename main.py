import os

mkvPath = r"C:\PT\XX\_source"
outPath = r"C:\PT\XX\_encode"
vpyPath = r"C:\PT\XX\main.vpy"
temp = r"C:\PT\XX\_temp"
x265 = r"C:\PT\XX\x265.exe"
x265P = '--crf 14.5 --preset slower --tune lp++ --output-depth 10 --profile main10 --level-idc 4.1 --rd 5 --psy-rd 1.8 --rskip 0 --ctu 32 --limit-tu 2 --cutree-strength 1.75 --no-rect --no-amp --aq-mode 5 --qg-size 8 --aq-strength 0.8 --qcomp 0.65 --cbqpoffs -2 --crqpoffs -2 --vbv-bufsize 30000 --vbv-maxrate 30000 --pbratio 1.2 --hme-range 16,24,40 --merange 38 --bframes 8 --rc-lookahead 60 --ref 4 --min-keyint 1 --no-open-gop --deblock -1:-1 --no-sao --no-strong-intra-smoothing'
VSPipe = r"C:\PT\XX\vapoursynth-R57.A6\VSPipe.exe"
mkvMerge = r"C:\PT\XX\mkvtoolnix-64-bit-73.0.0\mkvmerge.exe"


mkvCount = 0
mkvList = []
batList = []
mergeList = []
for root, dirs, files in os.walk(mkvPath):
    for file in files:
        if file.endswith(".mkv"):
            mkv = os.path.join(root, file)
            mkvList.append(mkv)
            mkvCount = mkvCount + 1
            
with open(vpyPath, 'r') as f:
    vpy = f.read()
    vpy = vpy.split('#BATCH')
    f.close()

for i in range(mkvCount):
    batList.append('"'+VSPipe+'"'+' "'+os.path.join(temp, 'batch'+str(i+1)+'.vpy')+'" - --y4m | '+'"'+x265+'" '+x265P+' --y4m --output "'+os.path.join(temp, 'batch'+str(i+1)+'_out.hevc')+'" -')
    mergeList.append('"'+mkvMerge+'" -o "'+os.path.join(outPath, 'batch'+str(i+1)+'_out.mkv')+'" -D "'+mkvList[i]+'" "'+os.path.join(temp, 'batch'+str(i+1)+'_out.hevc')+'" -s 0 --language 0:jpn --track-name 0:"encode" --default-duration 0:24000/1001p')
    with open(os.path.join(temp, 'batch'+str(i+1)+'.vpy'), 'w') as f:
        f.write(vpy[0]+'\na=r"'+mkvList[i]+'"'+vpy[2])
        f.close()
        i=i+1

with open( 'batch.bat', 'w') as f:
    f.write('@echo off\n')
    for i in range(mkvCount):
        f.write(batList[i]+'\n')
        f.write(mergeList[i]+'\n')
        i=i+1
    f.write('\npause')
    f.close()
