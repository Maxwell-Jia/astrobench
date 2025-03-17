#! /bin/bash

export CUDA_VISIBLE_DEVICES=7

MODEL="Qwen/Qwen2.5-1.5B-Instruct"
OUTPUT_DIR=eval_results/$MODEL

lm_eval --model vllm \
    --model_args "pretrained=$MODEL,tensor_parallel_size=1" \
    --gen_kwargs "max_gen_toks=8192" \
    --tasks gpqa_astro \
    --output_path $OUTPUT_DIR \
    --log_samples \
    --include_path ./tasks \
    --num_fewshot 0 \
    --apply_chat_template \
    --batch_size 8