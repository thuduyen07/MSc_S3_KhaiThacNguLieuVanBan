# DAAM Experience on sd-pokemon-diffusers

## How to run
### Install environment
```
    pip install -r ./requirements.txt
```
### Setup CPU/GPU device
- For Windows/Linux using:
```
    device = "cpu" if args.no_cuda else "cuda"
```
- For MacOS (Apple chips) using:
```
    device = "cpu" if args.no_cuda else "mps"
    if(device == "mps"):
        torch.mps.empty_cache()
```

### Login HuggingFace
1. Run the bellow command on Terminal/Cmd:
```
    huggingface-cli login
```
2. Get token from web browser 
3. Input the token to terminal

### Run demo 
```
    cd daam/run
    python demo.py 
```
Note: There are some flags options:
```
  -h, --help            show this help message and exit
  --model {v1,v2-base,v2-large,v2-1-base,v2-1-large,sd-pokemon-diffusers}, -m {v1,v2-base,v2-large,v2-1-base,v2-1-large,sd-pokemon-diffusers}
                        which diffusion model to use
  --seed SEED, -s SEED  the random seed
  --port PORT, -p PORT  the port to launch the demo
  --no-cuda             Use CPUs instead of GPUs
```

### Run for generation:
```
    cd daam/run
    python generate.py 
```
Note: There are some flags options:
```
    -h, --help            show this help message and exit
    --action {quickgen,prompt,coco,template,cconj,coco-unreal,stdin,regenerate}, -a {quickgen,prompt,coco,template,cconj,coco-unreal,stdin,regenerate}
    --low-memory
    --model {v1,v2-base,v2-large,v2-1-base,v2-1-large,sd-pokemon-diffusers}
    --output-folder OUTPUT_FOLDER, -o OUTPUT_FOLDER
    --input-folder INPUT_FOLDER, -i INPUT_FOLDER
    --seed SEED, -s SEED
    --gen-limit GEN_LIMIT
    --template TEMPLATE
    --template-data-file TEMPLATE_DATA_FILE, -tdf TEMPLATE_DATA_FILE
    --seed-offset SEED_OFFSET
    --num-timesteps NUM_TIMESTEPS, -n NUM_TIMESTEPS
    --all-heads
    --word WORD
    --random-seed
    --truth-only
    --save-heads
    --load-heads
```

## Run for eveluation:
```
    cd daam/run
    python evaluate.py 
```
Note: There are some flags options:
```
    -h, --help            show this help message and exit
    --input-folder INPUT_FOLDER, -i INPUT_FOLDER
    --pred-prefix PRED_PREFIX, -p PRED_PREFIX
    --mask-type {word,composite}, -m {word,composite}
    --eval-type {labeled,unlabeled,hungarian}, -e {labeled,unlabeled,hungarian}
    --restrict-set {none,coco27,coco80}, -r {none,coco27,coco80}
    --subtype SUBTYPE, -st SUBTYPE
```

### model
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
    lambdalabs/pokemon-blip-captions 
```
