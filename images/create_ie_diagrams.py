#!/usr/bin/env python3
"""
Create educational diagrams for Information Extraction presentation
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Arrow
import numpy as np

def create_information_extraction_pipeline():
    """Create a pipeline diagram for information extraction"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(7, 7.5, 'Information Extraction Pipeline', fontsize=20, fontweight='bold', 
            ha='center', va='center')
    
    # Input box
    input_box = FancyBboxPatch((0.5, 5), 2.5, 1.5, 
                               boxstyle="round,pad=0.1", facecolor='lightblue', 
                               edgecolor='navy', linewidth=2)
    ax.add_patch(input_box)
    ax.text(1.75, 5.75, 'Unstructured\nText Input', fontsize=12, ha='center', va='center')
    
    # Arrow 1
    ax.arrow(3.2, 5.75, 0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # NER box
    ner_box = FancyBboxPatch((4, 5), 2.5, 1.5, 
                            boxstyle="round,pad=0.1", facecolor='lightgreen', 
                            edgecolor='darkgreen', linewidth=2)
    ax.add_patch(ner_box)
    ax.text(5.25, 5.75, 'Named Entity\nRecognition\n(NER)', fontsize=12, ha='center', va='center')
    
    # Arrow 2
    ax.arrow(6.7, 5.75, 0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Relation Extraction box
    rel_box = FancyBboxPatch((7.5, 5), 2.5, 1.5, 
                            boxstyle="round,pad=0.1", facecolor='lightyellow', 
                            edgecolor='orange', linewidth=2)
    ax.add_patch(rel_box)
    ax.text(8.75, 5.75, 'Relation\nExtraction', fontsize=12, ha='center', va='center')
    
    # Arrow 3
    ax.arrow(10.2, 5.75, 0.6, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    # Output box
    output_box = FancyBboxPatch((11, 5), 2.5, 1.5, 
                               boxstyle="round,pad=0.1", facecolor='lightcoral', 
                               edgecolor='darkred', linewidth=2)
    ax.add_patch(output_box)
    ax.text(12.25, 5.75, 'Structured\nKnowledge', fontsize=12, ha='center', va='center')
    
    # Example text below
    example_text = "Example: 'Apple Inc. was founded by Steve Jobs in Cupertino.'"
    ax.text(7, 4.2, example_text, fontsize=11, ha='center', va='center', style='italic')
    
    # Entity examples
    ax.text(1.75, 3.5, 'Raw Text', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(5.25, 3.5, 'Entities: [Apple Inc.], [Steve Jobs], [Cupertino]', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(8.75, 3.5, 'Relations: (founder_of), (location_of)', fontsize=11, ha='center', va='center', fontweight='bold')
    ax.text(12.25, 3.5, 'Knowledge Graph', fontsize=11, ha='center', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/information_extraction_pipeline.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_ner_example():
    """Create a NER example visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')
    
    # Title
    ax.text(6, 5.5, 'Named Entity Recognition (NER) Example', fontsize=16, fontweight='bold', 
            ha='center', va='center')
    
    # Original sentence
    sentence = "Barack Obama was born in Hawaii and worked as President of the United States."
    ax.text(6, 4.5, f'Input: "{sentence}"', fontsize=12, ha='center', va='center')
    
    # Color-coded entities
    entities = [
        ("Barack Obama", "PERSON", "lightblue"),
        ("Hawaii", "LOCATION", "lightgreen"),
        ("President", "TITLE", "lightyellow"),
        ("United States", "LOCATION", "lightgreen")
    ]
    
    y_pos = 3.5
    ax.text(1, y_pos, 'Entities Found:', fontsize=12, fontweight='bold', ha='left', va='center')
    
    for i, (entity, label, color) in enumerate(entities):
        # Entity box
        entity_box = Rectangle((2 + i*2.2, y_pos-0.2), 1.8, 0.4, 
                              facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(entity_box)
        ax.text(2.9 + i*2.2, y_pos, f'{entity}', fontsize=10, ha='center', va='center')
        
        # Label below
        ax.text(2.9 + i*2.2, y_pos-0.5, f'({label})', fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Legend
    legend_items = [
        ("PERSON", "People's names", "lightblue"),
        ("LOCATION", "Places", "lightgreen"),
        ("TITLE", "Job titles", "lightyellow")
    ]
    
    ax.text(6, 2, 'Common NER Labels:', fontsize=12, fontweight='bold', ha='center', va='center')
    for i, (label, desc, color) in enumerate(legend_items):
        legend_box = Rectangle((3 + i*2, 1.3), 1.5, 0.4, 
                              facecolor=color, edgecolor='black', linewidth=1)
        ax.add_patch(legend_box)
        ax.text(3.75 + i*2, 1.5, f'{label}', fontsize=10, ha='center', va='center')
        ax.text(3.75 + i*2, 0.9, f'{desc}', fontsize=8, ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/ner_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_structured_vs_unstructured():
    """Create structured vs unstructured data comparison"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(7, 7.5, 'Structured vs Unstructured Data', fontsize=18, fontweight='bold', 
            ha='center', va='center')
    
    # Structured Data Column
    struct_box = Rectangle((0.5, 4), 6, 3, facecolor='lightblue', 
                          edgecolor='navy', linewidth=2)
    ax.add_patch(struct_box)
    ax.text(3.5, 6.8, 'STRUCTURED DATA', fontsize=14, fontweight='bold', 
            ha='center', va='center')
    
    struct_items = [
        "✓ Organized in tables/rows/columns",
        "✓ Follows predefined schema",
        "✓ Easy to search and query",
        "✓ Examples: databases, spreadsheets",
        "✓ Financial transactions, sensor data"
    ]
    
    for i, item in enumerate(struct_items):
        ax.text(0.7, 6.2 - i*0.3, item, fontsize=10, ha='left', va='center')
    
    # Unstructured Data Column
    unstruct_box = Rectangle((7.5, 4), 6, 3, facecolor='lightcoral', 
                           edgecolor='darkred', linewidth=2)
    ax.add_patch(unstruct_box)
    ax.text(10.5, 6.8, 'UNSTRUCTURED DATA', fontsize=14, fontweight='bold', 
            ha='center', va='center')
    
    unstruct_items = [
        "✗ No predefined organization",
        "✗ Requires advanced processing",
        "✗ Difficult to search directly",
        "✗ Examples: text, images, videos",
        "✗ Social media, emails, documents"
    ]
    
    for i, item in enumerate(unstruct_items):
        ax.text(7.7, 6.2 - i*0.3, item, fontsize=10, ha='left', va='center')
    
    # Information Extraction bridge
    ax.text(7, 3.5, 'Information Extraction', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='purple')
    ax.arrow(6.5, 3.2, -0.8, 0, head_width=0.1, head_length=0.1, fc='purple', ec='purple')
    ax.arrow(7.5, 3.2, 0.8, 0, head_width=0.1, head_length=0.1, fc='purple', ec='purple')
    
    # Transformation visualization
    ax.text(7, 2.8, 'Transforms unstructured → structured', fontsize=11, 
            ha='center', va='center', style='italic', color='purple')
    
    # Examples at bottom
    ax.text(3.5, 2, 'Structured Examples:', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(3.5, 1.6, 'Excel tables, SQL databases, CSV files', fontsize=10, ha='center', va='center')
    
    ax.text(10.5, 2, 'Unstructured Examples:', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(10.5, 1.6, 'News articles, social media, images, videos', fontsize=10, ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/structured_vs_unstructured_data.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_relation_extraction_example():
    """Create relation extraction visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Relation Extraction Example', fontsize=16, fontweight='bold', 
            ha='center', va='center')
    
    # Input sentence
    sentence = "Microsoft acquired LinkedIn for $26.2 billion in 2016."
    ax.text(6, 6.8, f'Input: "{sentence}"', fontsize=12, ha='center', va='center')
    
    # Entities
    ax.text(3, 6, 'Entities Detected:', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Microsoft entity
    ms_box = Rectangle((1, 5.2), 2, 0.6, facecolor='lightblue', edgecolor='navy', linewidth=2)
    ax.add_patch(ms_box)
    ax.text(2, 5.5, 'Microsoft\n(Organization)', fontsize=10, ha='center', va='center')
    
    # LinkedIn entity
    li_box = Rectangle((4, 5.2), 2, 0.6, facecolor='lightgreen', edgecolor='darkgreen', linewidth=2)
    ax.add_patch(li_box)
    ax.text(5, 5.5, 'LinkedIn\n(Organization)', fontsize=10, ha='center', va='center')
    
    # Relation arrow
    ax.arrow(3.2, 5.5, 0.6, 0, head_width=0.1, head_length=0.1, fc='red', ec='red', linewidth=3)
    ax.text(3.5, 5.8, 'acquired', fontsize=11, fontweight='bold', ha='center', va='center', color='red')
    
    # Additional info
    ax.text(8, 5.5, 'Additional Info:', fontsize=12, fontweight='bold', ha='center', va='center')
    ax.text(8, 5, '$26.2 billion', fontsize=10, ha='center', va='center', color='purple')
    ax.text(8, 4.5, '2016 (Date)', fontsize=10, ha='center', va='center', color='purple')
    
    # Relation types
    ax.text(6, 3.8, 'Common Relation Types:', fontsize=12, fontweight='bold', ha='center', va='center')
    
    relation_types = [
        ("works_at", "Person → Organization"),
        ("founder_of", "Person → Organization"),
        ("acquired", "Organization → Organization"),
        ("located_in", "Organization → Location"),
        ("born_in", "Person → Location")
    ]
    
    for i, (rel_type, description) in enumerate(relation_types):
        x_pos = 2 + (i % 3) * 3
        y_pos = 3.2 - (i // 3) * 0.6
        
        rel_box = Rectangle((x_pos-0.8, y_pos-0.2), 1.6, 0.4, 
                           facecolor='lightyellow', edgecolor='orange', linewidth=1)
        ax.add_patch(rel_box)
        ax.text(x_pos, y_pos, rel_type, fontsize=9, ha='center', va='center', fontweight='bold')
        ax.text(x_pos, y_pos-0.3, description, fontsize=8, ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/relation_extraction_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_event_extraction_diagram():
    """Create event extraction visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(6, 7.5, 'Event Extraction Example', fontsize=16, fontweight='bold', 
            ha='center', va='center')
    
    # Input text
    text = "Apple will launch the new iPhone 15 at a special event in Cupertino next month."
    ax.text(6, 6.8, f'Input: "{text}"', fontsize=11, ha='center', va='center')
    
    # Event components
    ax.text(6, 6.2, 'Event Components:', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Event trigger
    trigger_box = Rectangle((2, 5.2), 2, 0.6, facecolor='red', alpha=0.3, 
                           edgecolor='darkred', linewidth=2)
    ax.add_patch(trigger_box)
    ax.text(3, 5.5, 'Event Trigger:\n"launch"', fontsize=10, ha='center', va='center', fontweight='bold')
    
    # Event arguments
    arguments = [
        ("Apple", "Agent", "lightblue", 5, 5.2),
        ("iPhone 15", "Product", "lightgreen", 8, 5.2),
        ("Cupertino", "Location", "lightyellow", 2, 4.2),
        ("next month", "Time", "lightcoral", 5, 4.2)
    ]
    
    for i, (arg, role, color, x, y) in enumerate(arguments):
        arg_box = Rectangle((x-0.8, y), 1.6, 0.6, facecolor=color, 
                           edgecolor='black', linewidth=1)
        ax.add_patch(arg_box)
        ax.text(x, y+0.3, arg, fontsize=9, ha='center', va='center', fontweight='bold')
        ax.text(x, y-0.1, f'({role})', fontsize=8, ha='center', va='center')
    
    # Event structure
    ax.text(6, 3.2, 'Extracted Event Structure:', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Event frame
    event_frame = Rectangle((3, 2.2), 6, 0.8, facecolor='lightgray', 
                           edgecolor='black', linewidth=2)
    ax.add_patch(event_frame)
    ax.text(6, 2.6, 'Event: Product Launch', fontsize=12, ha='center', va='center', fontweight='bold')
    
    # Event details
    details = [
        "Agent: Apple",
        "Product: iPhone 15", 
        "Location: Cupertino",
        "Time: next month"
    ]
    
    for i, detail in enumerate(details):
        ax.text(4 + (i % 2) * 3, 2 + (i // 2) * 0.3, f"• {detail}", 
                fontsize=9, ha='left', va='center')
    
    # Event types
    ax.text(6, 1, 'Common Event Types:', fontsize=12, fontweight='bold', ha='center', va='center')
    
    event_types = ["Business", "Politics", "Sports", "Technology", "Medical", "Legal"]
    
    for i, event_type in enumerate(event_types):
        x_pos = 2 + i * 1.6
        type_box = Rectangle((x_pos-0.6, 0.3), 1.2, 0.4, 
                           facecolor='lightsteelblue', edgecolor='navy', linewidth=1)
        ax.add_patch(type_box)
        ax.text(x_pos, 0.5, event_type, fontsize=8, ha='center', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/event_extraction_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

# Create all diagrams
print("Creating information extraction diagrams...")
create_information_extraction_pipeline()
print("Created information extraction pipeline diagram")

create_ner_example()
print("Created NER example diagram")

create_structured_vs_unstructured()
print("Created structured vs unstructured data comparison")

create_relation_extraction_example()
print("Created relation extraction example")

create_event_extraction_diagram()
print("Created event extraction diagram")

print("\nAll diagrams created successfully!")
print("Files saved to: D:/STU/开课/Slides - 副本/images/")