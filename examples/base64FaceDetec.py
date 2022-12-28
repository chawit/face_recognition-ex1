import urllib.request as ur
import face_recognition as fr
image = 'Input image file is base64 encoded'
decoded= ur.urlopen(image)
image_loaded = fr.load_image_file(decoded)
face_locations = fr.face_locations(image_loaded)
print("I found {} face(s) in this photograph.".format(len(face_locations)))