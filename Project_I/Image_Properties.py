from PIL import Image
from PIL.ExifTags import TAGS

imagePath = "E://20200312_114906.jpg"
image = Image.open(imagePath)


info_dict = {

        "FileName" : image.filename,
        "Image Size" : image.size,
        "Image Height" : image.height,
        "Image Width" : image.width,
        "Image Format" : image.format,
        "Image Mode": image.mode,
        "Image is Animated": getattr(image, "is_animated",False),
        "Frames in Image": getattr(image,"n_frames",1),
}


for label, value in info_dict.items():
    print(f"{label}:{value}")

exifdata = image.getexif()

for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")
  

print(exifdata)