# -*- coding: utf-8 -*-
"""
Handwriter-python3 v0.6.0 Written by Unbinilium https://unbinilium.github.io/Handwriter
Requirements: uuid pillow twine setuptools wheel tox pytest handright
"""

import os, sys, json

usage = '\nUsage: python3 ' + sys.argv[0] + ' <configuration file path>'

if sys.version_info.major < 3:
    print('Python3 or newer version required!', usage)
    os.system('python3 ' + sys.argv[0] + str('' if len(sys.argv) < 1 else sys.argv[1]))
    sys.exit()

try:
    import uuid
    from PIL import Image, ImageFont
    from handright import Template, handwrite
except ImportError:
    os.system('pip3 install uuid pillow twine setuptools wheel tox pytest handright')
    print('Install dependencies finished!', usage)
    os.system('python3 ' + sys.argv[0] + str('' if len(sys.argv) < 1 else sys.argv[1]))
    sys.exit()

text_file_path, font_file_path, output_path = '', '', ''

if len(sys.argv) < 2:
    while not os.path.isfile(text_file_path):
        print('Please input text file path:')
        text_file_path = input()
        if os.path.isfile(text_file_path):
            break
        else:
            print('Text file "' + text_file_path + '" not found!')

    while not os.path.isfile(font_file_path):
        print('Please input font file path:')
        font_file_path = input()
        if os.path.isfile(font_file_path):
            break
        else:
            print('Font file "' + font_file_path + '" not found!')

    while not os.path.isdir(font_file_path):
        print('Please input output path:')
        output_path = input()
        if os.path.isdir(output_path):
            break
        else:
            print('Output path "' + output_path + '" not exist!')

    template = Template(background = Image.new(mode = "1", size = (2480, 3500), color = 1), font = ImageFont.truetype(font_file_path), fill = 0, font_size = 80, font_size_sigma = 2, perturb_x_sigma = 1, perturb_y_sigma = 1, perturb_theta_sigma = 0.05, line_spacing = 80, line_spacing_sigma = 2, word_spacing = -20, word_spacing_sigma = 2, left_margin = 150, top_margin = 150, right_margin = 150, bottom_margin = 150, end_chars = "，。,.")
else:
    if os.path.isfile(sys.argv[1]):
        configuration_dict = json.loads(open(sys.argv[1], encoding='utf-8').readline())
        text_file_path = configuration_dict['text_file_path']
        output_path = configuration_dict['output_path'],
        background_color = configuration_dict['background_color']
        background_width = configuration_dict['background_width']
        background_hight = configuration_dict['background_hight']
        if os.path.isfile(background_color):
            background_temp = Image.open(background_color).resize(background_width, background_hight)
        else:
            background_temp = Image.new(mode = "CMYK", size = (background_width, background_hight), color = background_color)
        
        template = Template(background = background_temp, font = ImageFont.truetype(configuration_dict['font_file_path']), fill = configuration_dict['font_color'], font_size = configuration_dict['font_size'], font_size_sigma = configuration_dict['font_size_sigma'], perturb_x_sigma = configuration_dict['perturb_x_sigma'], perturb_y_sigma = configuration_dict['perturb_y_sigma'], perturb_theta_sigma = configuration_dict['perturb_theta_sigma'], line_spacing = configuration_dict['line_spacing'], line_spacing_sigma = configuration_dict['line_spacing_sigma'], word_spacing = configuration_dict['word_spacing'], word_spacing_sigma = configuration_dict['word_spacing_sigma'], left_margin = configuration_dict['left_margin'], top_margin = configuration_dict['top_margin'], right_margin = configuration_dict['right_margin'], bottom_margin = configuration_dict['bottom_margin'], end_chars = configuration_dict['end_chars'])

text = open(text_file_path, mode = 'r', encoding='utf-8').read()
images = handwrite(text, template)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.save((output_path + str(uuid.uuid4()) + ".webp").format(i))
