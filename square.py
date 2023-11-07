
import cairo

# Set up surface
surface = cairo.ImageSurface(cairo.FORMAT_RGB24, 600, 400)
ctx = cairo.Context(surface)
ctx.set_source_rgb(0.8, 0.8, 0.8)
ctx.paint()

# Draw a red square
ctx.rectangle(150, 100, 100, 100)  # (x, y, width, height)
ctx.set_source_rgb(1, 0, 0)
ctx.fill()

surface.write_to_png("output_dir/output_image.png")