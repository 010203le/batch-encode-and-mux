import vapoursynth as vs
core = vs.core


#BATCH
a = r""

#BATCH

clip = core.lsmas.LWLibavSource(a, threads=1)
clip = core.fmtc.bitdepth(clip, bits=10)
clip.set_output()
