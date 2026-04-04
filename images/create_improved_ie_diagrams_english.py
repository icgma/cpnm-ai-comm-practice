#!/usr/bin/env python3
"""
Create improved educational diagrams for Information Extraction presentation
Focused on financial report examples for undergraduate students (English version)
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Arrow
import numpy as np

def create_improved_structured_vs_unstructured():
    """Create educational comparison with financial report examples"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'From Unstructured to Structured: Financial Report Extraction', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Unstructured Data (Left side)
    unstruct_box = FancyBboxPatch((0.5, 5.5), 7, 3.5, 
                                  boxstyle="round,pad=0.2", facecolor='#FFE5CC', 
                                  edgecolor='#E67E22', linewidth=3)
    ax.add_patch(unstruct_box)
    ax.text(4, 8.5, 'UNSTRUCTURED TEXT', fontsize=16, fontweight='bold', 
            ha='center', va='center', color='#E67E22')
    
    # Financial report text example
    report_text = """Company A released Q2 2025 earnings report today.
Revenue reached $50 billion, up 15% YoY, beating expectations.
AI hardware "Stardust" series sales hit $10 billion.
CEO Li Ming stated: "We are confident in Stardust's long-term potential."
Following the report, stock fell 3% in after-hours trading."""
    
    ax.text(0.7, 8.2, 'Original Report:', fontsize=12, fontweight='bold', ha='left', va='top')
    ax.text(0.7, 7.8, report_text, fontsize=10, ha='left', va='top', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Structured Data (Right side)
    struct_box = FancyBboxPatch((8.5, 5.5), 7, 3.5, 
                               boxstyle="round,pad=0.2", facecolor='#D5F4E6', 
                               edgecolor='#27AE60', linewidth=3)
    ax.add_patch(struct_box)
    ax.text(12, 8.5, 'STRUCTURED DATA', fontsize=16, fontweight='bold', 
            ha='center', va='center', color='#27AE60')
    
    # Structured table example
    table_data = [
        ['Entity Type', 'Entity Name', 'Value/Description'],
        ['Company', 'Company A', 'Revenue: $50B'],
        ['Product', 'Stardust Series', 'Sales: $10B'],
        ['Person', 'CEO Li Ming', 'Positive outlook'],
        ['Financial Metric', 'Revenue', 'Growth: 15%'],
        ['Market Response', 'Stock Price', 'After-hours: -3%']
    ]
    
    # Draw table
    for i, row in enumerate(table_data):
        for j, cell in enumerate(row):
            x_pos = 8.7 + j * 2.2
            y_pos = 8.2 - i * 0.4
            
            # Header row
            if i == 0:
                cell_box = Rectangle((x_pos-0.1, y_pos-0.15), 2.0, 0.3, 
                                   facecolor='#27AE60', alpha=0.3)
                ax.add_patch(cell_box)
                fontweight = 'bold'
                fontsize = 10
            else:
                fontweight = 'normal'
                fontsize = 9
            
            ax.text(x_pos, y_pos, cell, fontsize=fontsize, ha='left', va='center', 
                   fontweight=fontweight)
    
    # Information Extraction arrow and process
    ax.arrow(7.5, 7.25, 1, 0, head_width=0.2, head_length=0.1, 
             fc='#3498DB', ec='#3498DB', linewidth=4)
    ax.text(8, 6.8, 'Information Extraction', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#3498DB')
    
    # Benefits section
    benefits_box = FancyBboxPatch((2, 2.5), 12, 2.5, 
                                  boxstyle="round,pad=0.3", facecolor='#EBF5FB', 
                                  edgecolor='#3498DB', linewidth=2, linestyle='--')
    ax.add_patch(benefits_box)
    
    ax.text(8, 4.5, 'Benefits of Structured Data', fontsize=16, fontweight='bold', 
            ha='center', va='center', color='#3498DB')
    
    benefits = [
        '✓ Quick Query & Analysis',
        '✓ Easy Data Visualization',
        '✓ Automated Processing',
        '✓ Simple Comparison'
    ]
    
    for i, benefit in enumerate(benefits):
        x_pos = 3 + (i % 2) * 6
        y_pos = 4.1 - (i // 2) * 0.4
        ax.text(x_pos, y_pos, benefit, fontsize=12, ha='left', va='center', 
               fontweight='bold', color='#2C3E50')
    
    # Use cases
    ax.text(8, 1.5, 'Applications: Data Journalism, Investment Analysis, Competitor Research', fontsize=12, 
            ha='center', va='center', style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/structured_vs_unstructured_data.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_information_extraction_pipeline():
    """Create cleaner pipeline with financial report example"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'Information Extraction Pipeline: Text to Knowledge', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input example
    input_box = FancyBboxPatch((0.5, 7.5), 6, 1.5, 
                               boxstyle="round,pad=0.2", facecolor='#FADBD8', 
                               edgecolor='#E74C3C', linewidth=2)
    ax.add_patch(input_box)
    ax.text(3.5, 8.5, 'Input: Financial Report', fontsize=14, fontweight='bold', ha='center', va='center')
    
    input_text = """Company A Q2 revenue $50B,
growth 15%. AI hardware "Stardust"
series sales $10B. CEO Li Ming
expressed confidence in future."""
    ax.text(0.7, 8.2, input_text, fontsize=10, ha='left', va='top')
    
    # Step 1: NER
    ner_box = FancyBboxPatch((8.5, 7.5), 6, 1.5, 
                            boxstyle="round,pad=0.2", facecolor='#D6EAF8', 
                            edgecolor='#3498DB', linewidth=2)
    ax.add_patch(ner_box)
    ax.text(11.5, 8.5, 'Named Entity Recognition (NER)', fontsize=14, fontweight='bold', ha='center', va='center')
    
    ner_results = """Entities:
• Company A (ORG)
• Stardust (PRODUCT)
• Li Ming (PERSON)
• $50B, $10B (MONEY)"""
    ax.text(8.7, 8.2, ner_results, fontsize=10, ha='left', va='top')
    
    # Arrow 1
    ax.arrow(6.7, 8.25, 1.6, 0, head_width=0.15, head_length=0.1, 
             fc='#3498DB', ec='#3498DB', linewidth=3)
    ax.text(7.5, 8.6, 'Step 1', fontsize=12, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    # Step 2: Relation Extraction
    rel_box = FancyBboxPatch((0.5, 5), 6, 1.5, 
                            boxstyle="round,pad=0.2", facecolor='#D5F4E6', 
                            edgecolor='#27AE60', linewidth=2)
    ax.add_patch(rel_box)
    ax.text(3.5, 6, 'Relation Extraction (RE)', fontsize=14, fontweight='bold', ha='center', va='center')
    
    rel_results = """Relation Triples:
• (Company A, revenue, $50B)
• (Company A, has product, Stardust)
• (Stardust, sales, $10B)"""
    ax.text(0.7, 5.7, rel_results, fontsize=10, ha='left', va='top')
    
    # Arrow 2
    ax.arrow(11.5, 7.4, 0, -1.6, head_width=0.15, head_length=0.1, 
             fc='#27AE60', ec='#27AE60', linewidth=3)
    ax.text(12.2, 6.5, 'Step 2', fontsize=12, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    # Step 3: Event Extraction
    event_box = FancyBboxPatch((8.5, 5), 6, 1.5, 
                              boxstyle="round,pad=0.2", facecolor='#FEF9E7', 
                              edgecolor='#F39C12', linewidth=2)
    ax.add_patch(event_box)
    ax.text(11.5, 6, 'Event Extraction (EE)', fontsize=14, fontweight='bold', ha='center', va='center')
    
    event_results = """Event Frame:
• Event Type: Earnings Release
• Subject: Company A
• Time: Q2
• Key Data: Revenue growth 15%"""
    ax.text(8.7, 5.7, event_results, fontsize=10, ha='left', va='top')
    
    # Arrow 3
    ax.arrow(6.7, 5.75, 1.6, 0, head_width=0.15, head_length=0.1, 
             fc='#F39C12', ec='#F39C12', linewidth=3)
    ax.text(7.5, 6.1, 'Step 3', fontsize=12, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    # Final Output
    output_box = FancyBboxPatch((4.5, 2.5), 7, 1.5, 
                               boxstyle="round,pad=0.2", facecolor='#E8DAEF', 
                               edgecolor='#8E44AD', linewidth=2)
    ax.add_patch(output_box)
    ax.text(8, 3.5, 'Structured Knowledge Output', fontsize=14, fontweight='bold', ha='center', va='center')
    
    output_text = """JSON Format: {
  "company": "Company A",
  "revenue": "$50B",
  "growth": "15%",
  "product": "Stardust",
  "product_sales": "$10B"
}"""
    ax.text(4.7, 3.2, output_text, fontsize=10, ha='left', va='top', 
           bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    # Arrows to output
    ax.arrow(3.5, 5.4, 1, -1.6, head_width=0.15, head_length=0.1, 
             fc='#8E44AD', ec='#8E44AD', linewidth=2, linestyle='--')
    ax.arrow(11.5, 5.4, -1, -1.6, head_width=0.15, head_length=0.1, 
             fc='#8E44AD', ec='#8E44AD', linewidth=2, linestyle='--')
    
    # Legend
    legend_text = "Applications: Data Journalism, Investment Analysis, Competitor Research, Sentiment Monitoring"
    ax.text(8, 0.5, legend_text, fontsize=12, ha='center', va='center', 
           style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/information_extraction_pipeline.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_ner_example():
    """Create clearer NER with financial report example and color coding"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'Named Entity Recognition (NER): Identifying Key Information', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input text
    ax.text(8, 8.8, 'Input Text:', fontsize=14, fontweight='bold', ha='center', va='center')
    
    # Original sentence with highlighted entities
    sentence = "Company A released Q2 2025 earnings report today, revenue $50 billion, AI hardware 'Stardust' series sales $10 billion."
    ax.text(8, 8.4, sentence, fontsize=12, ha='center', va='center', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', edgecolor='#BDC3C7'))
    
    # Color-coded entities
    entities = [
        ("Company A", "ORG", "Company/Org", "#3498DB", 2, 7.2),
        ("Q2 2025", "TIME", "Time", "#F39C12", 6, 7.2),
        ("$50 billion", "MONEY", "Amount", "#27AE60", 10, 7.2),
        ("Stardust", "PRODUCT", "Product", "#9B59B6", 2, 6.2),
        ("$10 billion", "MONEY", "Amount", "#27AE60", 8, 6.2)
    ]
    
    # Draw entities with color coding
    for i, (entity, label, desc, color, x, y) in enumerate(entities):
        # Entity box
        entity_box = Rectangle((x-0.8, y-0.3), 1.6, 0.6, 
                              facecolor=color, alpha=0.3, 
                              edgecolor=color, linewidth=2)
        ax.add_patch(entity_box)
        ax.text(x, y, entity, fontsize=11, ha='center', va='center', fontweight='bold')
        
        # Label and description
        ax.text(x, y-0.5, f'{label}', fontsize=9, ha='center', va='center', 
               fontweight='bold', color=color)
        ax.text(x, y-0.8, f'{desc}', fontsize=8, ha='center', va='center', color='#7F8C8D')
    
    # Legend section
    legend_box = FancyBboxPatch((1, 4), 14, 2, 
                               boxstyle="round,pad=0.3", facecolor='#EBF5FB', 
                               edgecolor='#3498DB', linewidth=2)
    ax.add_patch(legend_box)
    
    ax.text(8, 5.7, 'Common Entity Types & Color Coding', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Legend items
    legend_items = [
        ("ORG", "Organizations", "#3498DB"),
        ("PERSON", "People's Names", "#E74C3C"),
        ("TIME", "Time & Dates", "#F39C12"),
        ("MONEY", "Amounts & Currency", "#27AE60"),
        ("PRODUCT", "Products & Services", "#9B59B6"),
        ("LOCATION", "Places & Locations", "#1ABC9C")
    ]
    
    for i, (label, desc, color) in enumerate(legend_items):
        x_pos = 2.5 + (i % 3) * 4.5
        y_pos = 5.2 - (i // 3) * 0.4
        
        # Color box
        color_box = Rectangle((x_pos-0.3, y_pos-0.15), 0.6, 0.3, 
                             facecolor=color, alpha=0.3, edgecolor=color, linewidth=1)
        ax.add_patch(color_box)
        
        ax.text(x_pos+0.5, y_pos, f'{label}: {desc}', fontsize=10, ha='left', va='center')
    
    # Application examples
    ax.text(8, 3.2, 'Application Examples', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    applications = [
        '• Data Journalism: Auto-extract company names, people, amounts',
        '• Investment Analysis: Quickly identify key data and metrics in reports',
        '• Sentiment Monitoring: Track mentions of specific companies or products',
        '• Competitor Research: Extract product info and financial data from rivals'
    ]
    
    for i, app in enumerate(applications):
        ax.text(2, 2.8 - i*0.3, app, fontsize=11, ha='left', va='center', color='#34495E')
    
    # Note
    ax.text(8, 0.8, 'Tip: Different colored entity boxes help quickly identify information types', fontsize=10, 
            ha='center', va='center', style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/ner_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_relation_extraction_example():
    """Improve relation extraction visualization with triple relationships"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'Relation Extraction: Discovering Connections Between Entities', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input text
    ax.text(8, 8.8, 'Input Text:', fontsize=14, fontweight='bold', ha='center', va='center')
    
    sentence = "Company A released Q2 2025 earnings report, revenue $50 billion, AI hardware 'Stardust' series sales $10 billion."
    ax.text(8, 8.4, f'"{sentence}"', fontsize=12, ha='center', va='center', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', edgecolor='#BDC3C7'))
    
    # Extracted triples section
    ax.text(8, 7.8, 'Extracted Relation Triples (Subject, Predicate, Object):', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Triple 1
    triple1_box = FancyBboxPatch((1, 6.5), 14, 0.8, 
                                boxstyle="round,pad=0.2", facecolor='#E8F8F5', 
                                edgecolor='#27AE60', linewidth=2)
    ax.add_patch(triple1_box)
    
    # Draw entities and relation
    subject_box = Rectangle((2, 6.7), 2, 0.4, facecolor='#3498DB', alpha=0.3, 
                           edgecolor='#3498DB', linewidth=2)
    ax.add_patch(subject_box)
    ax.text(3, 6.9, 'Company A', fontsize=11, ha='center', va='center', fontweight='bold')
    
    relation_box = Rectangle((6, 6.7), 2, 0.4, facecolor='#F39C12', alpha=0.3, 
                            edgecolor='#F39C12', linewidth=2)
    ax.add_patch(relation_box)
    ax.text(7, 6.9, 'Revenue', fontsize=11, ha='center', va='center', fontweight='bold')
    
    object_box = Rectangle((10, 6.7), 2, 0.4, facecolor='#27AE60', alpha=0.3, 
                          edgecolor='#27AE60', linewidth=2)
    ax.add_patch(object_box)
    ax.text(11, 6.9, '$50 Billion', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Arrows
    ax.arrow(4.2, 6.9, 1.6, 0, head_width=0.1, head_length=0.1, fc='#F39C12', ec='#F39C12', linewidth=3)
    ax.arrow(8.2, 6.9, 1.6, 0, head_width=0.1, head_length=0.1, fc='#F39C12', ec='#F39C12', linewidth=3)
    
    # Triple 2
    triple2_box = FancyBboxPatch((1, 5.3), 14, 0.8, 
                                boxstyle="round,pad=0.2", facecolor='#FDEDEC', 
                                edgecolor='#E74C3C', linewidth=2)
    ax.add_patch(triple2_box)
    
    subject2_box = Rectangle((2, 5.5), 2, 0.4, facecolor='#9B59B6', alpha=0.3, 
                            edgecolor='#9B59B6', linewidth=2)
    ax.add_patch(subject2_box)
    ax.text(3, 5.7, 'Stardust Series', fontsize=11, ha='center', va='center', fontweight='bold')
    
    relation2_box = Rectangle((6, 5.5), 2, 0.4, facecolor='#F39C12', alpha=0.3, 
                             edgecolor='#F39C12', linewidth=2)
    ax.add_patch(relation2_box)
    ax.text(7, 5.7, 'Sales', fontsize=11, ha='center', va='center', fontweight='bold')
    
    object2_box = Rectangle((10, 5.5), 2, 0.4, facecolor='#27AE60', alpha=0.3, 
                           edgecolor='#27AE60', linewidth=2)
    ax.add_patch(object2_box)
    ax.text(11, 5.7, '$10 Billion', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Arrows
    ax.arrow(4.2, 5.7, 1.6, 0, head_width=0.1, head_length=0.1, fc='#F39C12', ec='#F39C12', linewidth=3)
    ax.arrow(8.2, 5.7, 1.6, 0, head_width=0.1, head_length=0.1, fc='#F39C12', ec='#F39C12', linewidth=3)
    
    # Common relation types
    ax.text(8, 4.3, 'Common Relation Types', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    relation_types = [
        ('Company-Product', 'Company produces/sells product'),
        ('Company-Financial', 'Company revenue/profit data'),
        ('Product-Data', 'Product sales/performance data'),
        ('Person-Company', 'Person works at company'),
        ('Event-Time', 'Event occurrence time')
    ]
    
    for i, (rel_type, description) in enumerate(relation_types):
        x_pos = 2.5 + (i % 2) * 6
        y_pos = 3.8 - (i // 2) * 0.6
        
        type_box = Rectangle((x_pos-1.2, y_pos-0.2), 2.4, 0.4, 
                           facecolor='#EBF5FB', edgecolor='#3498DB', linewidth=1)
        ax.add_patch(type_box)
        ax.text(x_pos, y_pos, f'{rel_type}', fontsize=10, ha='center', va='center', fontweight='bold')
        ax.text(x_pos, y_pos-0.3, f'{description}', fontsize=8, ha='center', va='center', color='#7F8C8D')
    
    # Applications
    ax.text(8, 1.5, 'Applications', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    applications = [
        '• Knowledge Graph Construction: Connect companies, products, people',
        '• Business Intelligence: Discover competitive & cooperative relationships',
        '• Investment Decision Support: Analyze company financial & business connections',
        '• News Event Tracking: Understand parties involved and their relationships'
    ]
    
    for i, app in enumerate(applications):
        ax.text(2, 1.2 - i*0.25, app, fontsize=10, ha='left', va='center', color='#34495E')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/relation_extraction_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_event_extraction_example():
    """Make event framework clearer with financial report scenario"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'Event Extraction: Identifying & Structuring Event Information', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input text
    ax.text(8, 8.8, 'Input Text:', fontsize=14, fontweight='bold', ha='center', va='center')
    
    text = "Company A today released Q2 2025 earnings, revenue $50B beat expectations, but net profit fell 5%, stock dropped 3% after-hours."
    ax.text(8, 8.4, f'"{text}"', fontsize=12, ha='center', va='center', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', edgecolor='#BDC3C7'))
    
    # Event trigger detection
    ax.text(8, 7.8, 'Event Trigger Detection', fontsize=14, fontweight='bold', ha='center', va='center', color='#E74C3C')
    
    # Highlight trigger
    trigger_text = "Company A today released Q2 2025 earnings, revenue $50B..."
    ax.text(8, 7.4, trigger_text, fontsize=11, ha='center', va='center')
    
    # Highlight "released"
    trigger_box = Rectangle((6.8, 7.2), 0.8, 0.4, facecolor='#FADBD8', 
                           edgecolor='#E74C3C', linewidth=3)
    ax.add_patch(trigger_box)
    ax.text(7.2, 7.4, 'released', fontsize=11, ha='center', va='center', fontweight='bold', color='#E74C3C')
    
    # Event arguments
    ax.text(8, 6.8, 'Event Argument Extraction', fontsize=14, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    # Event frame visualization
    frame_box = FancyBboxPatch((2, 5.5), 12, 1, 
                              boxstyle="round,pad=0.3", facecolor='#EBF5FB', 
                              edgecolor='#3498DB', linewidth=2)
    ax.add_patch(frame_box)
    
    ax.text(8, 6.1, 'Earnings Release Event Frame', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Arguments
    arguments = [
        ('Company Subject', 'Company A', '#3498DB'),
        ('Event Type', 'Earnings Release', '#27AE60'),
        ('Time', 'Q2 2025', '#F39C12'),
        ('Revenue Data', '$50 Billion', '#9B59B6'),
        ('Market Response', 'Stock -3%', '#E74C3C')
    ]
    
    for i, (role, value, color) in enumerate(arguments):
        x_pos = 3 + (i % 3) * 3.5
        y_pos = 5.7 - (i // 3) * 0.4
        
        # Role label
        ax.text(x_pos, y_pos, f'{role}:', fontsize=10, ha='right', va='center', fontweight='bold')
        
        # Value box
        value_box = Rectangle((x_pos+0.2, y_pos-0.15), 1.5, 0.3, 
                             facecolor=color, alpha=0.2, edgecolor=color, linewidth=1)
        ax.add_patch(value_box)
        ax.text(x_pos+0.95, y_pos, value, fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Event structure template
    ax.text(8, 4.3, 'Event Structure Template', fontsize=14, fontweight='bold', ha='center', va='center', color='#8E44AD')
    
    template_box = FancyBboxPatch((3, 3.2), 10, 0.8, 
                                 boxstyle="round,pad=0.2", facecolor='#F4ECF7', 
                                 edgecolor='#8E44AD', linewidth=2)
    ax.add_patch(template_box)
    
    template_text = "[Event Type] + [Subject] + [Time] + [Key Data] + [Results/Impact]"
    ax.text(8, 3.6, template_text, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Common event types
    ax.text(8, 2.6, 'Common Event Types', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    event_types = [
        ('Earnings Release', 'Company releases financial data'),
        ('Product Launch', 'Company introduces new product'),
        ('M&A Event', 'Company acquisition or merger'),
        ('Personnel Change', 'Executive position changes'),
        ('Stock Volatility', 'Abnormal stock price movements')
    ]
    
    for i, (event_type, description) in enumerate(event_types):
        x_pos = 2.5 + (i % 2) * 6
        y_pos = 2.2 - (i // 2) * 0.4
        
        type_box = Rectangle((x_pos-1, y_pos-0.2), 2, 0.4, 
                           facecolor='#F8F9FA', edgecolor='#BDC3C7', linewidth=1)
        ax.add_patch(type_box)
        ax.text(x_pos, y_pos, event_type, fontsize=10, ha='center', va='center', fontweight='bold')
        ax.text(x_pos, y_pos-0.3, description, fontsize=8, ha='center', va='center', color='#7F8C8D')
    
    # Applications
    ax.text(8, 0.8, 'Applications: News Event Monitoring, Risk Alerting, Automatic Summary Generation', fontsize=11, 
            ha='center', va='center', style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/event_extraction_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_output_formats_comparison():
    """Create better comparison chart for Markdown/JSON/CSV formats"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'Output Format Comparison: Choose the Right Display Method', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Subtitle
    ax.text(8, 9.1, 'Using Company A Financial Data as Example', fontsize=12, ha='center', va='center', 
           style='italic', color='#7F8C8D')
    
    # JSON format
    json_box = FancyBboxPatch((0.5, 6.5), 4.5, 2.5, 
                             boxstyle="round,pad=0.2", facecolor='#E8F8F5', 
                             edgecolor='#27AE60', linewidth=2)
    ax.add_patch(json_box)
    ax.text(2.75, 8.5, 'JSON Format', fontsize=14, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    json_example = """{
  "company": "Company A",
  "quarter": "Q2",
  "revenue": "50B",
  "growth": "15%",
  "product": "Stardust Series",
  "product_sales": "10B"
}"""
    ax.text(0.7, 8.2, json_example, fontsize=9, ha='left', va='top', fontfamily='monospace')
    
    # Markdown format
    md_box = FancyBboxPatch((5.75, 6.5), 4.5, 2.5, 
                           boxstyle="round,pad=0.2", facecolor='#EBF5FB', 
                           edgecolor='#3498DB', linewidth=2)
    ax.add_patch(md_box)
    ax.text(8, 8.5, 'Markdown Table', fontsize=14, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    md_example = """| Metric | Value |
|--------|-------|
| Company | Company A |
| Quarter | Q2 |
| Revenue | $50 Billion |
| Growth Rate | 15% |
| Star Product | Stardust Series |
| Product Sales | $10 Billion |"""
    ax.text(5.95, 8.2, md_example, fontsize=9, ha='left', va='top', fontfamily='monospace')
    
    # CSV format
    csv_box = FancyBboxPatch((11, 6.5), 4.5, 2.5, 
                            boxstyle="round,pad=0.2", facecolor='#FEF9E7', 
                            edgecolor='#F39C12', linewidth=2)
    ax.add_patch(csv_box)
    ax.text(13.25, 8.5, 'CSV Format', fontsize=14, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    csv_example = """Metric,Value
Company,Company A
Quarter,Q2
Revenue,$50 Billion
Growth Rate,15%
Star Product,Stardust Series
Product Sales,$10 Billion"""
    ax.text(11.2, 8.2, csv_example, fontsize=9, ha='left', va='top', fontfamily='monospace')
    
    # Comparison table
    comparison_box = FancyBboxPatch((2, 3.5), 12, 2.5, 
                                   boxstyle="round,pad=0.3", facecolor='#F8F9FA', 
                                   edgecolor='#BDC3C7', linewidth=1)
    ax.add_patch(comparison_box)
    
    ax.text(8, 5.7, 'Format Feature Comparison', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    # Headers
    headers = ['Feature', 'JSON', 'Markdown', 'CSV']
    for i, header in enumerate(headers):
        x_pos = 3 + i * 3
        header_box = Rectangle((x_pos-0.8, 5.2), 1.6, 0.3, 
                              facecolor='#34495E', alpha=0.1)
        ax.add_patch(header_box)
        ax.text(x_pos, 5.35, header, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Comparison data
    comparison_data = [
        ['Readability', 'Medium', 'High', 'High'],
        ['Machine Parsing', 'Easy', 'Complex', 'Easy'],
        ['Data Structure', 'Nested', 'Table', 'Flat'],
        ['File Size', 'Medium', 'Small', 'Smallest'],
        ['Use Case', 'API Exchange', 'Document Display', 'Data Analysis']
    ]
    
    for i, row in enumerate(comparison_data):
        for j, cell in enumerate(row):
            x_pos = 3 + j * 3
            y_pos = 4.8 - i * 0.3
            
            if j == 0:  # Feature column
                fontweight = 'bold'
                color = '#2C3E50'
            else:
                fontweight = 'normal'
                color = '#34495E'
            
            ax.text(x_pos, y_pos, cell, fontsize=10, ha='center', va='center', 
                   fontweight=fontweight, color=color)
    
    # Recommendations
    ax.text(8, 2.8, 'Usage Recommendations', fontsize=14, fontweight='bold', ha='center', va='center', color='#8E44AD')
    
    recommendations = [
        'JSON: Best for API interfaces and program-to-program data exchange',
        'Markdown: Best for documents, reports, and presentations',
        'CSV: Best for Excel analysis, data statistics, and machine learning'
    ]
    
    for i, rec in enumerate(recommendations):
        ax.text(2, 2.4 - i*0.3, rec, fontsize=11, ha='left', va='center', color='#34495E')
    
    # Note
    ax.text(8, 0.8, 'Tip: Choose the most suitable format based on use case and audience', fontsize=10, 
            ha='center', va='center', style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/output_formats_comparison.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_prompt_formula():
    """Improve the prompt structure visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, 'Prompt Formula: The Secret to Structured Information Extraction', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Main formula
    formula_box = FancyBboxPatch((1, 7.5), 14, 1.5, 
                                boxstyle="round,pad=0.3", facecolor='#FEF9E7', 
                                edgecolor='#F39C12', linewidth=3)
    ax.add_patch(formula_box)
    
    ax.text(8, 8.4, 'Prompt = Role Definition + Task Description + Format Requirements + Examples', fontsize=16, 
            ha='center', va='center', fontweight='bold', color='#F39C12')
    ax.text(8, 7.9, '(CRISPE Framework Applied to Information Extraction)', fontsize=12, ha='center', va='center', 
           style='italic', color='#F39C12')
    
    # Detailed breakdown
    components = [
        {
            'title': 'Role Definition (C - Capacity)',
            'color': '#3498DB',
            'examples': ['You are a financial analyst', 'You are a data journalist', 'You are an investment advisor'],
            'position': (2, 6.2)
        },
        {
            'title': 'Task Description (R - Role & I - Insight)',
            'color': '#27AE60',
            'examples': ['Extract key data from the following report', 'Identify important entities in text', 'Summarize main business highlights'],
            'position': (8, 6.2)
        },
        {
            'title': 'Format Requirements (S - Style & P - Personality)',
            'color': '#E74C3C',
            'examples': ['Output in JSON format', 'Use Markdown table', 'List in order of importance'],
            'position': (14, 6.2)
        },
        {
            'title': 'Example Reference (E - Experiment)',
            'color': '#9B59B6',
            'examples': ['Reference format: Company-Revenue-Growth', 'Example: {"company": "Company A"}', 'Output using this template'],
            'position': (2, 4.5)
        }
    ]
    
    for comp in components:
        x, y = comp['position']
        
        # Component box
        comp_box = FancyBboxPatch((x-1.5, y-0.8), 3, 1.6, 
                                 boxstyle="round,pad=0.2", facecolor=comp['color'], alpha=0.1, 
                                 edgecolor=comp['color'], linewidth=2)
        ax.add_patch(comp_box)
        
        ax.text(x, y+0.4, comp['title'], fontsize=11, fontweight='bold', ha='center', va='center', 
               color=comp['color'])
        
        for i, example in enumerate(comp['examples']):
            ax.text(x, y-0.2-i*0.2, f'• {example}', fontsize=9, ha='center', va='center', 
                   color='#34495E')
    
    # Practical example
    example_box = FancyBboxPatch((1, 2.5), 14, 1.8, 
                                boxstyle="round,pad=0.3", facecolor='#E8F8F5', 
                                edgecolor='#27AE60', linewidth=2)
    ax.add_patch(example_box)
    
    ax.text(8, 3.9, 'Practical Example: Extract Structured Data from Financial Reports', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#27AE60')
    
    prompt_example = """Role: You are a financial data analyst
Task: Extract key financial data from the following report text
Format: Output in JSON format, include company, quarter, revenue, growth rate
Example: {"company": "Company A", "revenue": "50B"}"""
    
    ax.text(1.2, 3.6, prompt_example, fontsize=10, ha='left', va='top', fontfamily='monospace')
    
    # Tips section
    tips_box = FancyBboxPatch((1, 0.8), 14, 1.2, 
                             boxstyle="round,pad=0.2", facecolor='#FADBD8', 
                             edgecolor='#E74C3C', linewidth=2)
    ax.add_patch(tips_box)
    
    ax.text(8, 1.7, 'Usage Tips', fontsize=12, fontweight='bold', ha='center', va='center', color='#E74C3C')
    
    tips = [
        '• More specific roles yield more professional outputs',
        '• Format requirements should be clear and specific',
        '• Providing examples reduces ambiguity',
        '• Complex tasks can be broken into multiple steps'
    ]
    
    for i, tip in enumerate(tips):
        x_pos = 3 + (i % 2) * 6
        y_pos = 1.4 - (i // 2) * 0.2
        ax.text(x_pos, y_pos, tip, fontsize=9, ha='left', va='center', color='#34495E')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/prompt_formula.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

# Create all improved diagrams
def main():
    print("Creating improved information extraction diagrams...")
    
    create_improved_structured_vs_unstructured()
    print("Created improved structured vs unstructured data diagram")
    
    create_improved_information_extraction_pipeline()
    print("Created improved information extraction pipeline diagram")
    
    create_improved_ner_example()
    print("Created improved NER example diagram")
    
    create_improved_relation_extraction_example()
    print("Created improved relation extraction example diagram")
    
    create_improved_event_extraction_example()
    print("Created improved event extraction example diagram")
    
    create_improved_output_formats_comparison()
    print("Created improved output formats comparison diagram")
    
    create_improved_prompt_formula()
    print("Created improved prompt formula diagram")
    
    print("\nAll improved diagrams created successfully!")
    print("Files saved to: D:/STU/开课/Slides - 副本/images/")

if __name__ == "__main__":
    main()