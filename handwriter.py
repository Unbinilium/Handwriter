# -*- coding: utf-8 -*-
"""
Handwriter-python3 v0.5.0 Written by Unbinilium https://unbinilium.github.io/Handwriter
Requirements: uuid pillow twine setuptools wheel tox pytest handright
"""

import os
import sys

pythonver = sys.version_info.major
if pythonver < 3:
    print('Python3 or newer required! Please run "python3 ' + sys.argv[0] + '"again')
    sys.exit()

try:
    import uuid
    from PIL import Image, ImageFont
    from handright import Template, handwrite
except ImportError:
    os.system('pip3 install uuid pillow twine setuptools wheel tox pytest handright')
    print('Install dependencies finished! Please run "python3 ' + sys.argv[0] + '"again')
    sys.exit()

print('Please input text file path:')
textfilepath = input()
if not os.path.isfile(textfilepath):
    print('Text file "' + textfilepath + '" not found!')
    sys.exit()
    
print('Please input font file path:')
fontfilepath = input()
if not os.path.isfile(fontfilepath):
    print('Font file "' + fontfilepath + '" not found!')
    sys.exit()

print('Please input output path:')
outputpath = input()
if not os.path.isdir(outputpath):
    print('Output path "' + outputpath + '" not exist!')
    sys.exit()

texttemp = open(textfilepath, mode = 'r')
text = texttemp.read()
texttemp.close()

configuration = Template(
    background = Image.new(mode = "1", size = (2480, 3500), color = 1),
    font = ImageFont.truetype(fontfilepath),
    fill = 0,
    font_size = 60,
    font_size_sigma = 2,
    perturb_x_sigma = 1,
    perturb_y_sigma = 1,
    perturb_theta_sigma = 0.05,
    line_spacing = 60,
    line_spacing_sigma = 2,
    word_spacing = -20,
    word_spacing_sigma = 2,
    left_margin = 80,
    top_margin = 50,
    right_margin = 80,
    bottom_margin = 50,
    end_chars = "，。,.",
)
images = handwrite(text, configuration)
for i, im in enumerate(images):
    assert isinstance(im, Image.Image)
    im.save((outputpath + str(uuid.uuid4()) + ".webp").format(i))
