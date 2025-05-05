import os
import json
from glob import glob
from pathlib import Path

def create_dataset_json(output_file="dataset.json"):
    dataset = []
    
    inpainted_dirs = glob(os.path.join("inpainted", "*"))
    
    for inpainted_dir in inpainted_dirs:
        folder_id = os.path.basename(inpainted_dir)
        sampled_dir = os.path.join("sampled", folder_id)
        instruction_file = os.path.join("instructions", f"{folder_id}.txt")
        
        if not os.path.exists(sampled_dir) or not os.path.exists(instruction_file):
            print(f"Missing data for ID {folder_id}, skipping...")
            continue
        
        original_images = glob(os.path.join(inpainted_dir, "*.jpg")) + glob(os.path.join(inpainted_dir, "*.png"))
        if not original_images:
            print(f"No original image found in {inpainted_dir}, skipping...")
            continue
        original_image_path = original_images[0]
        
        sketch_images = glob(os.path.join(sampled_dir, "*sketch*"))
        ground_truth_images = glob(os.path.join(sampled_dir, "*photo*"))
        
        if not sketch_images or not ground_truth_images:
            print(f"Missing sketch or ground truth image in {sampled_dir}, skipping...")
            continue
            
        sketch_image_path = sketch_images[0]
        target_image_path = ground_truth_images[0]
        
        with open(instruction_file, 'r', encoding='utf-8') as f:
            instructions = f.read().strip().split('\n')
        
        # Create one datapoint for each instruction
        for idx, instruction in enumerate(instructions):
            datapoint = {
                "original_image_path": os.path.abspath(original_image_path),
                "sketch_image_path": os.path.abspath(sketch_image_path),
                "target_image_path": os.path.abspath(target_image_path),
                "edit_text": instruction,
                "id": f"{folder_id}_{idx}"
            }
            dataset.append(datapoint)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(dataset, f, indent=2)
    
    print(f"Dataset created with {len(dataset)} datapoints and saved to {output_file}")
    return dataset

if __name__ == "__main__":
    create_dataset_json() 