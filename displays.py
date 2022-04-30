"""displays image given description """

import requests
import json
import os
import subprocess
import sys
import time
import argparse



def get_image(image_url):
    """
    Gets image from url
    """
    image_data = requests.get(image_url)
    return image_data.content


def get_image_info(image_data):
    """
    Gets image info from image data
    """
    image_info = json.loads(image_data)
    return image_info


def get_image_url(image_info):
    """
    Gets image url from image info
    """
    image_url = image_info['url']
    return image_url


def get_image_path(image_info):
    """
    Gets image path from image info
    """
    image_path = image_info['path']
    return image_path


def get_image_name(image_info):
    """
    Gets image name from image info
    """
    image_name = image_info['name']
    return image_name


def get_image_size(image_info):
    """
    Gets image size from image info
    """
    image_size = image_info['size']
    return image_size


def get_image_type(image_info):
    """
    Gets image type from image info
    """
    image_type = image_info['type']
    return image_type


def get_image_format(image_info):
    """
    Gets image format from image info
    """
    image_format = image_info['format']
    return image_format


def get_image_width(image_info):
    """
    Gets image width from image info
    """
    image_width = image_info['width']
    return image_width


def get_image_height(image_info):
    """
    Gets image height from image info
    """
    image_height = image_info['height']
    return image_height


def get_image_colors(image_info):
    """
    Gets image colors from image info
    """
    image_colors = image_info['colors']
    return image_colors

# shows image
def show_image(image_data):
    """
    Shows image
    """
    subprocess.call(['display', '-resize', '50%', '-', '-'], stdin=image_data)



def main():
    """
    Main function
    """
    parser = argparse.ArgumentParser(description='Displays image given description')
    parser.add_argument('image_description', help='image description')
    args = parser.parse_args()
    image_description = args.image_description
    image_url = 'http://api.screenshotmachine.com/?key=b645b8&size=X&format=json&url=' + image_description
    image_data = get_image(image_url)
    image_info = get_image_info(image_data)
    image_url = get_image_url(image_info)
    image_path = get_image_path(image_info)
    image_name = get_image_name(image_info)
    image_size = get_image_size(image_info)
    image_type = get_image_type(image_info)
    image_format = get_image_format(image_info)
    image_width = get_image_width(image_info)
    image_height = get_image_height(image_info)
    image_colors = get_image_colors(image_info)
    print('Image URL: ' + image_url)
    print('Image Path: ' + image_path)
    print('Image Name: ' + image_name)
    print('Image Size: ' + image_size)
    print('Image Type: ' + image_type)
    print('Image Format: ' + image_format)
    print('Image Width: ' + image_width)
    print('Image Height: ' + image_height)
    print('Image Colors: ' + image_colors)
    image_data = get_image(image_url)
    show_image(image_data)

if __name__ == '__main__':
    main()
