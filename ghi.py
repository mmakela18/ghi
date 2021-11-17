### ghi: generate html image ###
## The absolute dumbest way to display an image. Don't ask why. ##
## Doesn't scale well to huge images. Lube your CPU and use at your own risk. ##
# Supports only images where color-mode is either RGB or RGBA #

from PIL import Image

OUTFILE = "testing.html"

img = Image.open("alfamakke.png")

img.show()

print(img.format)
print(img.mode)

pixel_rgb = img.getpixel((0,0))

# Load image

# Gather pixel tuples in a list

pixel_values = list(img.getdata())
print(pixel_values[1])

# Generate beginning of html from begin.template
out_buffer = ""
begin = open("begin.template.html","r")
out_buffer += begin.read()
begin.close()

# Begin table
out_buffer += "\t<table>\n"
out_buffer += "\t\t<tbody>\n"
# First row
# Generate actual table
print(pixel_values[0])
index = 0
for i in range(0, img.height):
  out_buffer += "\t\t\t<tr>\n"
  for j in range(0, img.width):
    print(str(index) + " vs " + str(len(pixel_values)))
    out_buffer += "\t\t\t\t<td class=\"pixel\" style=\"background-color:rgb(" + \
      str(pixel_values[index][0]) + "," + str(pixel_values[index][1]) + "," + \
      str(pixel_values[index][2]) + ");\"></td>\n"
    index += 1
  out_buffer += "\t\t\t</tr>\n"
# End table
out_buffer += "\t\t</tbody>\n"
out_buffer += "\t</table>\n"
# Generate end of html from end.template
end = open("end.template.html", "r")
out_buffer += end.read()

out = open(OUTFILE, "w")
out.write(out_buffer)
out.close()
