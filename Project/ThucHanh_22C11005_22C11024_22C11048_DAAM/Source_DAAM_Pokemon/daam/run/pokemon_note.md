## model
```
'sd-pokemon-diffusers': 'lambdalabs/sd-pokemon-diffusers'
```

## sample prompts
```
           with gr.Column():
                dropdown = gr.Dropdown([
                    'A brown pokemon in a green field',
                    'A blue pokemon on the beach',
                    'A white pikachu in a flower garden',
                ], label='Examples', value='A brown pokemon in a green field')

                text = gr.Textbox(label='Prompt', value='A brown pokemon in a green field')

                with gr.Row():
                    doc = cached_nlp('A brown pokemon in a green field')
                    tokens = [''] + [x.text for x in doc if x.pos_ == 'ADJ']
                    dropdown2 = gr.Dropdown(tokens, label='Adjective to replace', interactive=True)
                    text2 = gr.Textbox(label='New adjective', value='')

                checkbox = gr.Checkbox(value=False, label='Random seed')
                slider1 = gr.Slider(15, 30, value=25, interactive=True, step=1, label='Inference steps')

                submit_btn = gr.Button('Submit', elem_id='submit-btn')
                viz = gr.HTML(dependency('A brown pokemon in a green field'), elem_id='viz')
```

## data
```

```
