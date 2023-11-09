from typing import Any

import cairo
import logging
from datetime import datetime
import math



_OUTPUTFILE = "output_dir/"

surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 800, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()



