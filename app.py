from PIL import Image
import numpy as np
import argparse

DEFAULT_INPUT = 'input.bmp'
DEFAULT_OUTPUT = 'output.bmp'

def convertImageToIndexedChannel(image):
    img = image.convert('L')
    
    threshold_value = 200
    binary_image = image.point(lambda p: p > threshold_value and 255)
    indexed_image = binary_image.convert('1')
    return indexed_image

def convertImagePixels(image):
    data = np.asarray(image)
    inverted_img = np.bitwise_not(data)
    im = Image.fromarray(inverted_img)
    return im

def resizeImage(image, args):
    if args.size_output:
        output_image = image.resize(args.size_output)

        if args.verbose:
            print(f'Image redimensioned to {args.size_output}')

        return output_image
    else:
        return image

def app(args):
    input_image = Image.open(args.image_in)
    
    if args.verbose:
        print(f'Processing image {args.image_in}')
    
    output_image = resizeImage(input_image, args)
    
    if output_image.mode != '1':
        output_image = convertImageToIndexedChannel(output_image)

        if args.verbose:
            print('Converted image to indexed format')

    if args.invert_pixels:
        if args.verbose:
            print('Converting image pixels...')
        
        output_image = convertImagePixels(image)

    if args.verbose:
        print('Image processing is done')

    output_image.save(args.image_output, mode='1')
    
    if args.verbose:
        print(f'Result saved at: {args.image_output}')

    output_image.close()
    input_image.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Fusion Image Converter', description='Convert a image to the proper format for using the fusion printer')
    parser.add_argument('-I','--image-in', default=DEFAULT_INPUT, help='Image input path and name\nDefault path: ./input.bmp')
    parser.add_argument('-O', '--image-output', default=DEFAULT_OUTPUT, help='Image ouput path and name\nDefault path: ./ouput.bmp')
    parser.add_argument('-V', '--verbose', action='store_true', default=False)
    parser.add_argument('-R','--invert-pixels', action='store_true', default=False, help='Invert image pixel colors')
    parser.add_argument('-S', '--size-output', type=int, nargs=2, required=False, metavar=('width', 'height'), help='Set image size')
    
    args = parser.parse_args()

    app(args)
