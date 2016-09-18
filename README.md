# 12_image_resize

## Usage

 - Run `python image_resize.py <path_to_original_file> <options>`

## Options:

name | type | key |
--- | --- | --- |
**Scale** | float | `-s, --scale`
**Width** | int | `-w, --width`
**Height** | int | `-h, --height`
**Output** | string | `-o, --output`

Help will be displayed by `--help` key

Note that you can't use both scale and width / height options  
If output is not specified, output file will be   `<original_filename>__<width>x<height>.<original_extension>`
