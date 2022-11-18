import cv2
import gradio as gr


def convert_photo_to_sketch(image):
    # invert grey scale image
    invert_img = 255 - image
    # Gaussian fun to blur the image
    blur_img = cv2.GaussianBlur(invert_img, (21, 21), 0)
    # invert the blur image
    inverted_blurred_img = 255 - blur_img
    # sketch the image
    sketch_img = cv2.divide(image, inverted_blurred_img, scale=256.0)
    # return the final sketched image
    return sketch_img


# built interface with gradio to test the function
imagein = gr.Image(image_mode="L", label='Original Image')
imageout = "image"
gr.Interface(fn=convert_photo_to_sketch,
             inputs=imagein,
             outputs=imageout,
             title='Convert RGB Image to Sketch').launch()
