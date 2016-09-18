import os
import argparse
from PIL import Image


def resize_image(path_to_original, **kwargs):
    '''
    Kwargs are:
        - output
        - scale
        - width
        - height
    '''
    img = Image.open(path_to_original)
    width, height = img.size
    ratio = width / height

    if kwargs.get('scale', None):
        scale = kwargs['scale']
        width, height = int(width * scale), int(height * scale)
    elif kwargs.get('width', None) and kwargs.get('height', None):
        width, height = kwargs['width'], kwargs['height']
        if width / height != ratio:
            print('Resizing will change aspect ratio of the original image!')
    elif kwargs.get('width', None):
        width, height = kwargs['width'], int(kwargs['width'] / width * height)
    elif kwargs.get('height', None):
        width, height = int(kwargs['height'] / height * width), kwargs['height']

    if kwargs.get('output', None):
        path_to_result = kwargs['output']
    else:
        full_filename = path_to_original.split('/')[-1]
        filename, ext = full_filename.split('.')
        path_to_result = '{folder}/{filename}__{w}x{h}.{ext}'.format(
            folder=os.path.dirname(path_to_original),
            filename=filename,
            w=width,
            h=height,
            ext=ext,
        )

    img = img.resize((width, height), Image.ANTIALIAS)
    img.save(path_to_result, mode='RGBA')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--help', action='help', help='show this help message and exit')
    parser.add_argument('filename', type=str, help='Input filename')
    parser.add_argument('-s', '--scale', type=float, help='Increase image size in [scale] times')
    parser.add_argument('-w', '--width', type=int, help='Change image width')
    parser.add_argument('-h', '--height', type=int, help='Change image height')
    parser.add_argument('-o', '--output', type=str, help='Output filename')

    args = parser.parse_args()

    if args.scale and (args.width or args.height):
        print('You should use or scale, or width / height')
    else:
        resize_image(args.filename, **vars(args))
