from PIL import Image, ImageDraw, ImageFont
import os
memes = os.listdir('шаблоны')

top_text = ""
bottom_text = ""
print("Генератор мемов запущен!")
is_valid = False
while not is_valid:
    text_type = input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: ")
    try:
        text_type = int(text_type)
    except ValueError:
        print('Невверный ввод')
        continue
    if text_type == 1:
        bottom_text = input('Введите нижний текст: ')
        is_valid = True
        break
    elif text_type == 2:
        top_text = input('Введите верхний текст: ')
        bottom_text = input('Введите нижний текст: ')
        is_valid = True
        break
    else:
        print('неправильный режим')
print('Ввыберите картинку: ')
for meme in memes:
    print(f'{memes.index(meme)}{meme}')

index = int(input('Введите номер картинки: '))
print(top_text, bottom_text)
meme = Image.open(f'шаблоны/{memes[index]}')
canvas = ImageDraw.Draw(meme)

width, height = meme.size

font = ImageFont.truetype('impact.ttf', size = 90)

bbox_top = canvas.textbbox((0, 0), top_text, font = font)
bbox_bottom = canvas.textbbox((0, 0), bottom_text, font = font)

x_top = (width - bbox_top[2]) // 2
x_bot = (width - bbox_bottom[2]) // 2
y_top = 10
y_bot = height - bbox_bottom[3] - 10

canvas.text((x_top, y_top), top_text, font = font, stroke_width=2, stroke_fill='black')
canvas.text((x_bot, y_bot), bottom_text, font = font, stroke_width=2, stroke_fill='black')

meme.show()
meme.save('my_meme.png')