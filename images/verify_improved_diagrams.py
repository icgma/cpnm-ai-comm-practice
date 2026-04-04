#!/usr/bin/env python3
"""
Verification script for improved information extraction diagrams
"""

import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image

def verify_diagrams():
    """Verify all improved diagrams are created and displayable"""
    
    # List of expected diagrams
    expected_diagrams = [
        'structured_vs_unstructured_data.png',
        'information_extraction_pipeline.png',
        'ner_example.png',
        'relation_extraction_example.png',
        'event_extraction_example.png',
        'output_formats_comparison.png',
        'prompt_formula.png'
    ]
    
    print("=== Information Extraction Diagrams Verification ===\n")
    
    # Check if all diagrams exist
    images_dir = 'D:/STU/开课/Slides - 副本/images/'
    missing_diagrams = []
    existing_diagrams = []
    
    for diagram in expected_diagrams:
        filepath = os.path.join(images_dir, diagram)
        if os.path.exists(filepath):
            existing_diagrams.append(diagram)
            # Get file info
            file_size = os.path.getsize(filepath)
            file_size_mb = file_size / (1024 * 1024)
            
            # Check image properties
            try:
                with Image.open(filepath) as img:
                    width, height = img.size
                    format_type = img.format
                    print(f"OK {diagram}")
                    print(f"  Size: {file_size_mb:.1f} MB")
                    print(f"  Dimensions: {width}×{height} pixels")
                    print(f"  Format: {format_type}")
                    print()
            except Exception as e:
                print(f"ERROR {diagram} - Error reading image: {e}")
                missing_diagrams.append(diagram)
        else:
            print(f"ERROR {diagram} - File not found")
            missing_diagrams.append(diagram)
    
    # Summary
    print("=== Verification Summary ===")
    print(f"Total expected diagrams: {len(expected_diagrams)}")
    print(f"Successfully created: {len(existing_diagrams)}")
    print(f"Missing or problematic: {len(missing_diagrams)}")
    
    if missing_diagrams:
        print("\nMissing diagrams:")
        for diagram in missing_diagrams:
            print(f"  - {diagram}")
    else:
        print("\nSUCCESS: All diagrams successfully created!")
    
    # Quality check
    print("\n=== Quality Check ===")
    quality_issues = []
    
    for diagram in existing_diagrams:
        filepath = os.path.join(images_dir, diagram)
        try:
            with Image.open(filepath) as img:
                width, height = img.size
                
                # Check resolution (should be at least 1200x800 for good quality)
                if width < 1200 or height < 800:
                    quality_issues.append(f"{diagram}: Low resolution ({width}×{height})")
                
                # Check aspect ratio (should be reasonable for presentations)
                aspect_ratio = width / height
                if aspect_ratio < 1.2 or aspect_ratio > 2.0:
                    quality_issues.append(f"{diagram}: Unusual aspect ratio ({aspect_ratio:.2f})")
                
                # Check file size (should be reasonable - not too small or too large)
                file_size = os.path.getsize(filepath)
                file_size_mb = file_size / (1024 * 1024)
                if file_size_mb < 0.1:
                    quality_issues.append(f"{diagram}: Very small file size ({file_size_mb:.1f} MB)")
                elif file_size_mb > 5.0:
                    quality_issues.append(f"{diagram}: Very large file size ({file_size_mb:.1f} MB)")
                    
        except Exception as e:
            quality_issues.append(f"{diagram}: Error checking quality - {e}")
    
    if quality_issues:
        print("Quality issues found:")
        for issue in quality_issues:
            print(f"  WARNING: {issue}")
    else:
        print("OK: All diagrams meet quality standards!")
    
    return len(missing_diagrams) == 0 and len(quality_issues) == 0

def display_sample_diagrams():
    """Display a few sample diagrams for quick verification"""
    images_dir = 'D:/STU/开课/Slides - 副本/images/'
    sample_diagrams = [
        'structured_vs_unstructured_data.png',
        'information_extraction_pipeline.png',
        'ner_example.png'
    ]
    
    print("\n=== Sample Diagrams Preview ===")
    print("(Close the windows to continue)")
    
    for i, diagram in enumerate(sample_diagrams):
        filepath = os.path.join(images_dir, diagram)
        if os.path.exists(filepath):
            try:
                img = mpimg.imread(filepath)
                plt.figure(figsize=(12, 8))
                plt.imshow(img)
                plt.title(f"Sample {i+1}: {diagram}")
                plt.axis('off')
                plt.tight_layout()
                plt.show()
            except Exception as e:
                print(f"Could not display {diagram}: {e}")
        else:
            print(f"Sample diagram not found: {diagram}")

if __name__ == "__main__":
    # Run verification
    success = verify_diagrams()
    
    # Ask if user wants to see sample diagrams
    if success:
        response = input("\nWould you like to see sample diagrams? (y/n): ").lower()
        if response == 'y':
            display_sample_diagrams()
    
    print("\nVerification complete!")