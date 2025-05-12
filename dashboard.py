import streamlit as st
import os
import json

st.set_page_config(layout="wide")
st.title("MultiEdit: Controllable Image Editing via Sketch and Text")

# Load edit instructions
with open('edit_instructions.json', 'r') as f:
    edit_instructions = json.load(f)

# Define paths
original_path = "original_images"
sketch_path = "sketch_images" 
edited_path = "sketch_and_prompt_flat"
gt_path = "ground_truth"

# Get list of image files
image_files = sorted([f for f in os.listdir(original_path) if f.endswith('.png')])

# Create table
for idx, _ in enumerate(image_files):
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.image(os.path.join(original_path, f'{idx}.png'), caption="Original")
        
    with col2:
        st.image(os.path.join(sketch_path, f'{idx}.png'), caption="Sketch")
        
    with col3:
        st.write("Edit Instruction:")
        st.write(edit_instructions[idx])
        
    with col4:
        st.image(os.path.join(edited_path, f'{idx}.png'), caption="Edited")
        
    with col5:
        st.image(os.path.join(gt_path, f'{idx}.png'), caption="Ground Truth")
        
    st.markdown("---")
