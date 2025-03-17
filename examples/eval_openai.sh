#! /bin/bash

export OPENAI_API_KEY="your_openai_api_key"
export OPENAI_BASE_URL="your_openai_base_url"

# Maximum number of concurrent API requests to OpenAI
export OPENAI_CONCURRENCY=3

MODEL="chatgpt-4o-latest"
OUTPUT_DIR=eval_results/openai/$MODEL
base_url=$OPENAI_BASE_URL/chat/completions

lm_eval --model openai-chat-completions \
    --model_args "model=$MODEL,api_key=$OPENAI_API_KEY,base_url=$base_url" \
    --gen_kwargs "max_gen_toks=16384" \
    --tasks gpqa_astro,super_gpqa_astro \
    --output_path $OUTPUT_DIR \
    --log_samples \
    --include_path ./tasks \
    --num_fewshot 0 \
    --apply_chat_template