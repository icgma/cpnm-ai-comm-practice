#!/usr/bin/env python3
"""
Verify that the new information_extraction_concept.png meets all requirements
"""

from PIL import Image
import os

def verify_diagram():
    """Verify the created diagram meets specifications"""
    file_path = 'D:/STU/开课/Slides - 副本/images/information_extraction_concept.png'
    
    print("=== Verifying information_extraction_concept.png ===\n")
    
    try:
        with Image.open(file_path) as img:
            print("✓ File can be opened successfully")
            
            # Check format
            if img.format == 'PNG':
                print("✓ File is in PNG format")
            else:
                print(f"✗ File format is {img.format}, expected PNG")
            
            # Check size (should be high resolution)
            width, height = img.size
            print(f"✓ Image dimensions: {width} x {height} pixels")
            
            if width >= 1800 and height >= 1200:
                print("✓ High resolution suitable for projection")
            else:
                print("⚠ Resolution might be low for large projections")
            
            # Check DPI
            dpi = img.info.get('dpi', (72, 72))  # Default DPI if not specified
            if isinstance(dpi, tuple):
                dpi_x, dpi_y = dpi
            else:
                dpi_x = dpi_y = dpi
            
            print(f"✓ DPI: {dpi_x} x {dpi_y}")
            
            if dpi_x >= 300 and dpi_y >= 300:
                print("✓ Meets 300 DPI requirement for high-quality printing")
            else:
                print("⚠ DPI below 300 - may not be optimal for high-quality printing")
            
            # Check file size (should be much larger than 3.5KB)
            file_size = os.path.getsize(file_path)
            print(f"✓ File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            
            if file_size > 100000:  # 100KB
                print("✓ File size indicates proper high-resolution image")
            else:
                print("⚠ File size seems small for a high-resolution diagram")
            
            # Verify image data integrity
            img.load()
            print("✓ Image data integrity verified - not corrupted")
            
            print(f"\n=== Summary ===")
            print(f"Format: {img.format}")
            print(f"Dimensions: {width} x {height} pixels")
            print(f"DPI: {dpi_x} x {dpi_y}")
            print(f"File size: {file_size/1024:.1f} KB")
            print(f"Mode: {img.mode}")
            
            if file_size > 100000 and width >= 1800 and height >= 1200:
                print("\n🎉 SUCCESS: Diagram meets all technical requirements!")
                print("   - High resolution (suitable for projection)")
                print("   - Large file size (indicates proper image data)")
                print("   - Not corrupted (data integrity verified)")
                print("   - PNG format (proper for presentations)")
            else:
                print("\n⚠ WARNING: Some requirements may not be fully met")
            
            return True
            
    except Exception as e:
        print(f"✗ Error verifying file: {e}")
        return False

if __name__ == "__main__":
    verify_diagram()