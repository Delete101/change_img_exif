from exif import Image, DATETIME_STR_FORMAT
import json

# Read JSON
with open('data_file.json', 'r') as f:
    json_text = json.load(f)

for txt in json_text['datetime']:
    date = str(txt['date'])
    time = str(txt['time'])

# Print datetime
datetime = f'{date[:4]}:{date[4:6]}:{date[6:8]} {time[:2]}:{time[2:4]}:{time[4:6]}'
print(f'Дата для ввода : {datetime}')

# Read IMG
with open('C:\\Users\\owner\\PycharmProjects\\change_exif\\img_1.jpg', 'rb') as jpg_f:
    img_1 = Image(jpg_f)

img_1.datetime_original = datetime

print(f'List EXIF for IMG1: {img_1.list_all()}')
print(f'DateTime for IMG1: {img_1.datetime_original}')

# with open('C:\\Users\\owner\\PycharmProjects\\change_exif\\img_2.jpg', 'wb') as new_jpg_f:
#     new_jpg_f.write(img_1.get_file())

with open('C:\\Users\\owner\\PycharmProjects\\test_py\\img_2.jpg', 'rb') as new_img_:
    img_1_ = Image(new_img_)
    print(f'Datetime for IMG2 : {img_1_.datetime_original}')

