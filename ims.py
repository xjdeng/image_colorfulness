from Easy_Image import imagesearch
try:
    from . import main
except ImportError:
    import main
default_columns = ['file','mtime','timestamp','colorfulness']
import time
    
def calc_colorfulness(f, fpath, mtime):
    score = main.image_colorfulness(fpath)
    return [[fpath, mtime, time.time(), score]]

def run(start = "./", outfile = "image_colorfulness.csv", batch = 10000):
    imagesearch.run_meta(calc_colorfulness, default_columns, outfile, start, batch)