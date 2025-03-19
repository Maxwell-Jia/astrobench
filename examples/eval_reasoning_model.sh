#! /bin/bash

export OPENAI_API_KEY="your_openai_api_key"
export OPENAI_BASE_URL="your_openai_base_url"

# Maximum number of concurrent API requests to OpenAI
export NUM_CONCURRENCY=3

MODEL="deepseek-r1"
OUTPUT_DIR=eval_results/deepseek-ai/$MODEL

lm_eval --model openai-reasoning-completions \
    --model_args "model=$MODEL,api_key=$OPENAI_API_KEY,base_url=$OPENAI_BASE_URL,num_concurrent=$NUM_CONCURRENCY" \
    --gen_kwargs "max_tokens=32768" \
    --tasks gpqa_astro \
    --output_path $OUTPUT_DIR \
    --log_samples \
    --include_path ./tasks \
    --num_fewshot 0 \
    --apply_chat_template \
    --use_cache $OUTPUT_DIR/cache/ \
    --cache_requests true