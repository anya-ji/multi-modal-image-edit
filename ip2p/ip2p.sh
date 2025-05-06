accelerate launch --mixed_precision="fp16" \
    ../../diffusers/examples/instruct_pix2pix/train_instruct_pix2pix.py \
    --pretrained_model_name_or_path=stabilityai/stable-diffusion-2-1 \
    --dataset_name=anya-ji/multi-modal-image-edit \
    --enable_xformers_memory_efficient_attention \
    --resolution=512 --random_flip \
    --train_batch_size=16 --gradient_accumulation_steps=4 --gradient_checkpointing \
    --max_train_steps=200 \
    --checkpointing_steps=50 --checkpoints_total_limit=1 \
    --learning_rate=5e-05 --max_grad_norm=1 --lr_warmup_steps=20 \
    --conditioning_dropout_prob=0.1 \
    --mixed_precision=fp16 \
    --seed=42 \
    --report_to=wandb \
    --output_dir=output \
    --original_image_column=original_image \
    --edit_prompt=edit_instruction \
    --edited_image=edited_image