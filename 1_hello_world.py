import gradio as gr


# define a function to process your input and output
def greet(name):
    return "Hello " + name + "!"


# create input and output objects
input = gr.Textbox(placeholder="Enter name here...")
output = "text"

# create interface
demo = gr.Interface(fn=greet,
                    inputs=[input],
                    outputs=[output])

demo.launch()
