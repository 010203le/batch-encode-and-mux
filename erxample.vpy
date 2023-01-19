import vapoursynth as vs
core = vs.core
import kagefunc as kgf
import fvsfunc as fvf
import mvsfunc as mvf
import vsTAAmbk as taa
import havsfunc as haf

#BATCH
a = r""

#BATCH

clip = core.lsmas.LWLibavSource(a, threads=1)
clip = core.fmtc.bitdepth(clip, bits=10)
clip.set_output()
