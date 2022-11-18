import cv2
import gradio as gr

examples = ["./resources/sunflower.jpg", "./resources/cat.jpg", "./resources/bee.jpg", "./resources/lemon.jpg"]


def convert_photo_to_sketch(image, k_sz):
    # invert grey scale image
    invert_img = 255 - image
    # Gaussian fun to blur the image
    blur_img = cv2.GaussianBlur(invert_img, (int(k_sz), int(k_sz)), 0)
    # invert the blur image
    inverted_blurred_img = 255 - blur_img
    # sketch the image
    sketch_img = cv2.divide(image, inverted_blurred_img, scale=256.0)
    # return the final sketched image
    return sketch_img


demo = gr.Blocks(title="Sketching")

with demo:
    with gr.Row(elem_id="sketch_image"):
        imagein = gr.Image(image_mode="L", label='Original image')
        imageout = gr.Image(interactive=False, label="Sketched image")
    with gr.Row():
        gr.Examples(examples, inputs=imagein)
        with gr.Column():
            gr.Markdown("This could be a description of what the slider does. It's in Markdown.")
            kernel_size = gr.Slider(minimum=3, maximum=51, step=2, value=21, label="kernel size").style(container=False)

    imagein.change(fn=convert_photo_to_sketch, inputs=[imagein, kernel_size], outputs=[imageout])
    kernel_size.change(fn=convert_photo_to_sketch, inputs=[imagein, kernel_size], outputs=[imageout])

demo.launch()
