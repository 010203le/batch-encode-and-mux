import vapoursynth as vs
core = vs.core


#BATCH
a = r".mkv"
s = r".ass"
#BATCH

clip = core.lsmas.LWLibavSource(a, threads=1)
clip = core.fmtc.bitdepth(clip, bits=10)
clip = core.vsfm.TextSubMod(clip,file=s)
clip.set_output()
