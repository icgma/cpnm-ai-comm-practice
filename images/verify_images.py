#!/usr/bin/env python3
"""
Verify that all images are properly created and accessible
"""

import os
from PIL import Image
import matplotlib.pyplot as plt

def verify_image(image_path):
    """Verify an image file is valid and displayable"""
    try:
        img = Image.open(image_path)
        print(f"OK {os.path.basename(image_path)}: {img.size} ({img.format}) - {os.path.getsize(image_path)} bytes")
        img.close()
        return True
    except Exception as e:
        print(f"ERROR {os.path.basename(image_path)}: ERROR - {e}")
        return False

def main():
    images_dir = "D:/STU/开课/Slides - 副本/images"
    
    # List of expected images
    expected_images = [
        "information_extraction_pipeline.png",
        "ner_example.png", 
        "structured_vs_unstructured_data.png",
        "relation_extraction_example.png",
        "event_extraction_example.png",
        "knowledge_graph_example.png",
        "nlp_pipeline_diagram.png",
        "text_mining_overview.png",
        "data_transformation_before_after.png",
        "information_extraction_concept.png",
        "output_formats_comparison.png",
        "challenge_timer.png",
        "prompt_formula.png"
    ]
    
    print("Verifying Information Extraction Images")
    print("=" * 50)
    
    valid_count = 0
    total_count = len(expected_images)
    
    for image_name in expected_images:
        image_path = os.path.join(images_dir, image_name)
        if os.path.exists(image_path):
            if verify_image(image_path):
                valid_count += 1
        else:
            print(f"ERROR {image_name}: MISSING")
    
    print("\n" + "=" * 50)
    print(f"Summary: {valid_count}/{total_count} images are valid and accessible")
    
    if valid_count == total_count:
        print("All images are ready for use in presentations!")
    else:
        print(f"Warning: {total_count - valid_count} images have issues")

if __name__ == "__main__":
    main()