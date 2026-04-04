#!/usr/bin/env python3
"""
Create improved educational diagrams for Information Extraction presentation
Focused on financial report examples for undergraduate students
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
    ax.text(8, 9.5, '从非结构化到结构化：财务报告信息提取', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Unstructured Data (Left side)
    unstruct_box = FancyBboxPatch((0.5, 5.5), 7, 3.5, 
                                  boxstyle="round,pad=0.2", facecolor='#FFE5CC', 
                                  edgecolor='#E67E22', linewidth=3)
    ax.add_patch(unstruct_box)
    ax.text(4, 8.5, '非结构化文本', fontsize=16, fontweight='bold', 
            ha='center', va='center', color='#E67E22')
    
    # Financial report text example
    report_text = """A公司今日发布2025年第二季度财报。报告显示，
公司营收达到500亿美元，同比增长15%，超出市场预期。
其中，AI硬件部门“星尘”系列产品销售额达100亿美元。
CEO李明表示：“我们对‘星尘’的长期潜力充满信心。”
财报发布后，公司股价盘后下跌3%。"""
    
    ax.text(0.7, 8.2, '财报原文：', fontsize=12, fontweight='bold', ha='left', va='top')
    ax.text(0.7, 7.8, report_text, fontsize=10, ha='left', va='top', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))
    
    # Structured Data (Right side)
    struct_box = FancyBboxPatch((8.5, 5.5), 7, 3.5, 
                               boxstyle="round,pad=0.2", facecolor='#D5F4E6', 
                               edgecolor='#27AE60', linewidth=3)
    ax.add_patch(struct_box)
    ax.text(12, 8.5, '结构化数据', fontsize=16, fontweight='bold', 
            ha='center', va='center', color='#27AE60')
    
    # Structured table example
    table_data = [
        ['实体类型', '实体名称', '数值/描述'],
        ['公司', 'A公司', '营收500亿美元'],
        ['产品', '星尘系列', '销售额100亿美元'],
        ['人物', 'CEO李明', '正面观点'],
        ['财务指标', '营收', '同比增长15%'],
        ['市场反应', '股价', '盘后下跌3%']
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
    
    ax.text(8, 6.8, '信息提取技术', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#3498DB')
    
    # Benefits section
    benefits_box = FancyBboxPatch((2, 2.5), 12, 2.5, 
                                  boxstyle="round,pad=0.3", facecolor='#EBF5FB', 
                                  edgecolor='#3498DB', linewidth=2, linestyle='--')
    ax.add_patch(benefits_box)
    
    ax.text(8, 4.5, '结构化数据的优势', fontsize=16, fontweight='bold', 
            ha='center', va='center', color='#3498DB')
    
    benefits = [
        '✓ 快速查询和分析',
        '✓ 便于数据可视化',
        '✓ 支持自动化处理',
        '✓ 易于比较和对比'
    ]
    
    for i, benefit in enumerate(benefits):
        x_pos = 3 + (i % 2) * 6
        y_pos = 4.1 - (i // 2) * 0.4
        ax.text(x_pos, y_pos, benefit, fontsize=12, ha='left', va='center', 
               fontweight='bold', color='#2C3E50')
    
    # Use cases
    ax.text(8, 1.5, '应用场景：数据新闻、投资分析、竞品研究', fontsize=12, 
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
    ax.text(8, 9.5, '信息提取流水线：从文本到知识', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input example
    input_box = FancyBboxPatch((0.5, 7.5), 6, 1.5, 
                               boxstyle="round,pad=0.2", facecolor='#FADBD8', 
                               edgecolor='#E74C3C', linewidth=2)
    ax.add_patch(input_box)
    ax.text(3.5, 8.5, '输入：财报文本', fontsize=14, fontweight='bold', ha='center', va='center')
    
    input_text = """A公司Q2营收500亿美元，
同比增长15%。AI硬件“星尘”
系列销售100亿美元。CEO李明
表示对未来充满信心。"""
    ax.text(0.7, 8.2, input_text, fontsize=10, ha='left', va='top')
    
    # Step 1: NER
    ner_box = FancyBboxPatch((8.5, 7.5), 6, 1.5, 
                            boxstyle="round,pad=0.2", facecolor='#D6EAF8', 
                            edgecolor='#3498DB', linewidth=2)
    ax.add_patch(ner_box)
    ax.text(11.5, 8.5, '命名实体识别 (NER)', fontsize=14, fontweight='bold', ha='center', va='center')
    
    ner_results = """实体：
• A公司 (ORG)
• 星尘 (PRODUCT)
• 李明 (PERSON)
• 500亿、100亿 (MONEY)"""
    ax.text(8.7, 8.2, ner_results, fontsize=10, ha='left', va='top')
    
    # Arrow 1
    ax.arrow(6.7, 8.25, 1.6, 0, head_width=0.15, head_length=0.1, 
             fc='#3498DB', ec='#3498DB', linewidth=3)
    ax.text(7.5, 8.6, '步骤1', fontsize=12, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    # Step 2: Relation Extraction
    rel_box = FancyBboxPatch((0.5, 5), 6, 1.5, 
                            boxstyle="round,pad=0.2", facecolor='#D5F4E6', 
                            edgecolor='#27AE60', linewidth=2)
    ax.add_patch(rel_box)
    ax.text(3.5, 6, '关系提取 (RE)', fontsize=14, fontweight='bold', ha='center', va='center')
    
    rel_results = """关系三元组：
• (A公司, 营收, 500亿美元)
• (A公司, 拥有产品, 星尘系列)
• (星尘系列, 销售额, 100亿美元)"""
    ax.text(0.7, 5.7, rel_results, fontsize=10, ha='left', va='top')
    
    # Arrow 2
    ax.arrow(11.5, 7.4, 0, -1.6, head_width=0.15, head_length=0.1, 
             fc='#27AE60', ec='#27AE60', linewidth=3)
    ax.text(12.2, 6.5, '步骤2', fontsize=12, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    # Step 3: Event Extraction
    event_box = FancyBboxPatch((8.5, 5), 6, 1.5, 
                              boxstyle="round,pad=0.2", facecolor='#FEF9E7', 
                              edgecolor='#F39C12', linewidth=2)
    ax.add_patch(event_box)
    ax.text(11.5, 6, '事件提取 (EE)', fontsize=14, fontweight='bold', ha='center', va='center')
    
    event_results = """事件框架：
• 事件类型：财报发布
• 主体：A公司
• 时间：Q2
• 关键数据：营收增长15%"""
    ax.text(8.7, 5.7, event_results, fontsize=10, ha='left', va='top')
    
    # Arrow 3
    ax.arrow(6.7, 5.75, 1.6, 0, head_width=0.15, head_length=0.1, 
             fc='#F39C12', ec='#F39C12', linewidth=3)
    ax.text(7.5, 6.1, '步骤3', fontsize=12, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    # Final Output
    output_box = FancyBboxPatch((4.5, 2.5), 7, 1.5, 
                               boxstyle="round,pad=0.2", facecolor='#E8DAEF', 
                               edgecolor='#8E44AD', linewidth=2)
    ax.add_patch(output_box)
    ax.text(8, 3.5, '结构化知识输出', fontsize=14, fontweight='bold', ha='center', va='center')
    
    output_text = """JSON格式：{
  "company": "A公司",
  "revenue": "500亿美元",
  "growth": "15%",
  "product": "星尘系列",
  "product_sales": "100亿美元"
}"""
    ax.text(4.7, 3.2, output_text, fontsize=10, ha='left', va='top', 
           bbox=dict(boxstyle="round,pad=0.2", facecolor='white', alpha=0.8))
    
    # Arrows to output
    ax.arrow(3.5, 5.4, 1, -1.6, head_width=0.15, head_length=0.1, 
             fc='#8E44AD', ec='#8E44AD', linewidth=2, linestyle='--')
    ax.arrow(11.5, 5.4, -1, -1.6, head_width=0.15, head_length=0.1, 
             fc='#8E44AD', ec='#8E44AD', linewidth=2, linestyle='--')
    
    # Legend
    legend_text = "适用于：数据新闻、投资分析、竞品研究、舆情监测"
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
    ax.text(8, 9.5, '命名实体识别 (NER)：识别文本中的关键信息', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input text
    ax.text(8, 8.8, '输入文本：', fontsize=14, fontweight='bold', ha='center', va='center')
    
    # Original sentence with highlighted entities
    sentence = "A公司今日发布2025年第二季度财报，营收500亿美元，AI硬件“星尘”系列销售100亿美元。"
    ax.text(8, 8.4, sentence, fontsize=12, ha='center', va='center', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', edgecolor='#BDC3C7'))
    
    # Color-coded entities
    entities = [
        ("A公司", "ORG", "公司/组织", "#3498DB", 2, 7.2),
        ("2025年第二季度", "TIME", "时间", "#F39C12", 6, 7.2),
        ("500亿美元", "MONEY", "金额", "#27AE60", 10, 7.2),
        ("星尘", "PRODUCT", "产品", "#9B59B6", 2, 6.2),
        ("100亿美元", "MONEY", "金额", "#27AE60", 8, 6.2)
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
    
    ax.text(8, 5.7, '常见实体类型及颜色标识', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Legend items
    legend_items = [
        ("ORG", "组织机构", "#3498DB"),
        ("PERSON", "人物姓名", "#E74C3C"),
        ("TIME", "时间日期", "#F39C12"),
        ("MONEY", "金额数量", "#27AE60"),
        ("PRODUCT", "产品服务", "#9B59B6"),
        ("LOCATION", "地点位置", "#1ABC9C")
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
    ax.text(8, 3.2, '应用场景', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    applications = [
        '• 数据新闻：自动提取公司名、人名、金额等关键信息',
        '• 投资分析：快速识别财报中的核心数据和指标',
        '• 舆情监测：追踪特定公司或产品的提及情况',
        '• 竞品研究：提取竞争对手的产品信息和财务数据'
    ]
    
    for i, app in enumerate(applications):
        ax.text(2, 2.8 - i*0.3, app, fontsize=11, ha='left', va='center', color='#34495E')
    
    # Note
    ax.text(8, 0.8, '提示：不同颜色的实体框帮助快速识别信息类型', fontsize=10, 
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
    ax.text(8, 9.5, '关系提取：发现实体之间的关联', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input text
    ax.text(8, 8.8, '输入文本：', fontsize=14, fontweight='bold', ha='center', va='center')
    
    sentence = "A公司发布Q2财报，营收500亿美元，AI硬件“星尘”系列销售100亿美元。"
    ax.text(8, 8.4, f'"{sentence}"', fontsize=12, ha='center', va='center', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', edgecolor='#BDC3C7'))
    
    # Extracted triples section
    ax.text(8, 7.8, '提取的关系三元组 (主语, 谓语, 宾语)：', fontsize=14, fontweight='bold', 
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
    ax.text(3, 6.9, 'A公司', fontsize=11, ha='center', va='center', fontweight='bold')
    
    relation_box = Rectangle((6, 6.7), 2, 0.4, facecolor='#F39C12', alpha=0.3, 
                            edgecolor='#F39C12', linewidth=2)
    ax.add_patch(relation_box)
    ax.text(7, 6.9, '营收', fontsize=11, ha='center', va='center', fontweight='bold')
    
    object_box = Rectangle((10, 6.7), 2, 0.4, facecolor='#27AE60', alpha=0.3, 
                          edgecolor='#27AE60', linewidth=2)
    ax.add_patch(object_box)
    ax.text(11, 6.9, '500亿美元', fontsize=11, ha='center', va='center', fontweight='bold')
    
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
    ax.text(3, 5.7, '星尘系列', fontsize=11, ha='center', va='center', fontweight='bold')
    
    relation2_box = Rectangle((6, 5.5), 2, 0.4, facecolor='#F39C12', alpha=0.3, 
                             edgecolor='#F39C12', linewidth=2)
    ax.add_patch(relation2_box)
    ax.text(7, 5.7, '销售额', fontsize=11, ha='center', va='center', fontweight='bold')
    
    object2_box = Rectangle((10, 5.5), 2, 0.4, facecolor='#27AE60', alpha=0.3, 
                           edgecolor='#27AE60', linewidth=2)
    ax.add_patch(object2_box)
    ax.text(11, 5.7, '100亿美元', fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Arrows
    ax.arrow(4.2, 5.7, 1.6, 0, head_width=0.1, head_length=0.1, fc='#F39C12', ec='#F39C12', linewidth=3)
    ax.arrow(8.2, 5.7, 1.6, 0, head_width=0.1, head_length=0.1, fc='#F39C12', ec='#F39C12', linewidth=3)
    
    # Common relation types
    ax.text(8, 4.3, '常见关系类型', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    relation_types = [
        ('公司-产品', '公司生产/销售产品'),
        ('公司-财务', '公司营收/利润数据'),
        ('产品-数据', '产品销售/性能数据'),
        ('人物-公司', '人物在公司任职'),
        ('事件-时间', '事件发生时间')
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
    ax.text(8, 1.5, '应用场景', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    applications = [
        '• 构建知识图谱：连接公司、产品、人物等信息',
        '• 商业情报分析：发现公司间的竞争与合作关系',
        '• 投资决策支持：分析公司财务与业务关联',
        '• 新闻事件追踪：理解事件相关方及其关系'
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
    ax.text(8, 9.5, '事件提取：识别和结构化事件信息', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Input text
    ax.text(8, 8.8, '输入文本：', fontsize=14, fontweight='bold', ha='center', va='center')
    
    text = "A公司今日发布2025年Q2财报，营收500亿美元超预期，但净利润下降5%，股价盘后下跌3%。"
    ax.text(8, 8.4, f'"{text}"', fontsize=12, ha='center', va='center', 
           bbox=dict(boxstyle="round,pad=0.5", facecolor='#F8F9FA', edgecolor='#BDC3C7'))
    
    # Event trigger detection
    ax.text(8, 7.8, '事件触发词检测', fontsize=14, fontweight='bold', ha='center', va='center', color='#E74C3C')
    
    # Highlight trigger
    trigger_text = "A公司今日发布2025年Q2财报，营收500亿美元..."
    ax.text(8, 7.4, trigger_text, fontsize=11, ha='center', va='center')
    
    # Highlight "发布"
    trigger_box = Rectangle((6.8, 7.2), 0.8, 0.4, facecolor='#FADBD8', 
                           edgecolor='#E74C3C', linewidth=3)
    ax.add_patch(trigger_box)
    ax.text(7.2, 7.4, '发布', fontsize=11, ha='center', va='center', fontweight='bold', color='#E74C3C')
    
    # Event arguments
    ax.text(8, 6.8, '事件论元提取', fontsize=14, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    # Event frame visualization
    frame_box = FancyBboxPatch((2, 5.5), 12, 1, 
                              boxstyle="round,pad=0.3", facecolor='#EBF5FB', 
                              edgecolor='#3498DB', linewidth=2)
    ax.add_patch(frame_box)
    
    ax.text(8, 6.1, '财报发布事件框架', fontsize=12, fontweight='bold', ha='center', va='center')
    
    # Arguments
    arguments = [
        ('公司主体', 'A公司', '#3498DB'),
        ('事件类型', '财报发布', '#27AE60'),
        ('时间', '2025年Q2', '#F39C12'),
        ('营收数据', '500亿美元', '#9B59B6'),
        ('市场反应', '股价下跌3%', '#E74C3C')
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
    ax.text(8, 4.3, '事件结构模板', fontsize=14, fontweight='bold', ha='center', va='center', color='#8E44AD')
    
    template_box = FancyBboxPatch((3, 3.2), 10, 0.8, 
                                 boxstyle="round,pad=0.2", facecolor='#F4ECF7', 
                                 edgecolor='#8E44AD', linewidth=2)
    ax.add_patch(template_box)
    
    template_text = "[事件类型] + [主体] + [时间] + [关键数据] + [结果/影响]"
    ax.text(8, 3.6, template_text, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Common event types
    ax.text(8, 2.6, '常见事件类型', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    event_types = [
        ('财报发布', '公司发布财务数据'),
        ('产品发布', '公司推出新产品'),
        ('并购事件', '公司收购或合并'),
        ('人事变动', '高管任职变动'),
        ('股价波动', '股票价格异常变动')
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
    ax.text(8, 0.8, '应用：新闻事件监测、风险预警、自动摘要生成', fontsize=11, 
            ha='center', va='center', style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU\u8bfe\Slides - 副本\images\event_extraction_example.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_output_formats_comparison():
    """Create better comparison chart for Markdown/JSON/CSV formats"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, '输出格式对比：选择适合的展示方式', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Subtitle
    ax.text(8, 9.1, '以A公司财报数据为例', fontsize=12, ha='center', va='center', 
           style='italic', color='#7F8C8D')
    
    # JSON format
    json_box = FancyBboxPatch((0.5, 6.5), 4.5, 2.5, 
                             boxstyle="round,pad=0.2", facecolor='#E8F8F5', 
                             edgecolor='#27AE60', linewidth=2)
    ax.add_patch(json_box)
    ax.text(2.75, 8.5, 'JSON格式', fontsize=14, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    json_example = """{
  "company": "A公司",
  "quarter": "Q2",
  "revenue": "500亿",
  "growth": "15%",
  "product": "星尘系列",
  "product_sales": "100亿"
}"""
    ax.text(0.7, 8.2, json_example, fontsize=9, ha='left', va='top', fontfamily='monospace')
    
    # Markdown format
    md_box = FancyBboxPatch((5.75, 6.5), 4.5, 2.5, 
                           boxstyle="round,pad=0.2", facecolor='#EBF5FB', 
                           edgecolor='#3498DB', linewidth=2)
    ax.add_patch(md_box)
    ax.text(8, 8.5, 'Markdown表格', fontsize=14, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    md_example = """| 指标 | 数值 |
|------|------|
| 公司 | A公司 |
| 季度 | Q2 |
| 营收 | 500亿美元 |
| 增长率 | 15% |
| 明星产品 | 星尘系列 |
| 产品销售额 | 100亿美元 |"""
    ax.text(5.95, 8.2, md_example, fontsize=9, ha='left', va='top', fontfamily='monospace')
    
    # CSV format
    csv_box = FancyBboxPatch((11, 6.5), 4.5, 2.5, 
                            boxstyle="round,pad=0.2", facecolor='#FEF9E7', 
                            edgecolor='#F39C12', linewidth=2)
    ax.add_patch(csv_box)
    ax.text(13.25, 8.5, 'CSV格式', fontsize=14, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    csv_example = """指标,数值
公司,A公司
季度,Q2
营收,500亿美元
增长率,15%
明星产品,星尘系列
产品销售额,100亿美元"""
    ax.text(11.2, 8.2, csv_example, fontsize=9, ha='left', va='top', fontfamily='monospace')
    
    # Comparison table
    comparison_box = FancyBboxPatch((2, 3.5), 12, 2.5, 
                                   boxstyle="round,pad=0.3", facecolor='#F8F9FA', 
                                   edgecolor='#BDC3C7', linewidth=1)
    ax.add_patch(comparison_box)
    
    ax.text(8, 5.7, '格式特点对比', fontsize=14, fontweight='bold', ha='center', va='center', color='#2C3E50')
    
    # Headers
    headers = ['特点', 'JSON', 'Markdown', 'CSV']
    for i, header in enumerate(headers):
        x_pos = 3 + i * 3
        header_box = Rectangle((x_pos-0.8, 5.2), 1.6, 0.3, 
                              facecolor='#34495E', alpha=0.1)
        ax.add_patch(header_box)
        ax.text(x_pos, 5.35, header, fontsize=11, ha='center', va='center', fontweight='bold')
    
    # Comparison data
    comparison_data = [
        ['可读性', '中等', '高', '高'],
        ['机器解析', '简单', '复杂', '简单'],
        ['数据结构', '嵌套', '表格', '平面'],
        ['文件大小', '中等', '小', '最小'],
        ['适用场景', 'API交换', '文档展示', '数据分析']
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
    ax.text(8, 2.8, '使用建议', fontsize=14, fontweight='bold', ha='center', va='center', color='#8E44AD')
    
    recommendations = [
        'JSON: 适合程序间数据交换、API接口',
        'Markdown: 适合文档、报告、演示文稿',
        'CSV: 适合Excel分析、数据统计、机器学习'
    ]
    
    for i, rec in enumerate(recommendations):
        ax.text(2, 2.4 - i*0.3, rec, fontsize=11, ha='left', va='center', color='#34495E')
    
    # Note
    ax.text(8, 0.8, '提示：根据使用场景和受众选择最合适的格式', fontsize=10, 
            ha='center', va='center', style='italic', color='#7F8C8D')
    
    plt.tight_layout()
    plt.savefig('D:/STU\u8bfe\Slides - 副本\images\output_formats_comparison.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_improved_prompt_formula():
    """Improve the prompt structure visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(8, 9.5, '提示词公式：结构化信息提取的秘诀', fontsize=20, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Main formula
    formula_box = FancyBboxPatch((1, 7.5), 14, 1.5, 
                                boxstyle="round,pad=0.3", facecolor='#FEF9E7', 
                                edgecolor='#F39C12', linewidth=3)
    ax.add_patch(formula_box)
    
    ax.text(8, 8.4, '提示词 = 角色定义 + 任务说明 + 格式要求 + 示例参考', fontsize=16, 
            ha='center', va='center', fontweight='bold', color='#F39C12')
    ax.text(8, 7.9, '(CRISPE框架在信息提取中的应用)', fontsize=12, ha='center', va='center', 
           style='italic', color='#F39C12')
    
    # Detailed breakdown
    components = [
        {
            'title': '角色定义 (C - Capacity)',
            'color': '#3498DB',
            'examples': ['你是一名财经分析师', '你是一位数据新闻记者', '你是投资顾问'],
            'position': (2, 6.2)
        },
        {
            'title': '任务说明 (R - Role & I - Insight)',
            'color': '#27AE60',
            'examples': ['请从以下财报中提取关键数据', '识别文本中的重要实体', '总结主要业务亮点'],
            'position': (8, 6.2)
        },
        {
            'title': '格式要求 (S - Style & P - Personality)',
            'color': '#E74C3C',
            'examples': ['以JSON格式输出', '使用Markdown表格', '按重要性排序列出'],
            'position': (14, 6.2)
        },
        {
            'title': '示例参考 (E - Experiment)',
            'color': '#9B59B6',
            'examples': ['参考格式：公司-营收-增长率', '例如：{\"公司\": \"A公司\"}', '按此模板输出'],
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
    
    ax.text(8, 3.9, '实战示例：从财报中提取结构化数据', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#27AE60')
    
    prompt_example = """角色：你是一名财经数据分析师
任务：从以下财报文本中提取关键财务数据
格式：按JSON格式输出，包含公司、季度、营收、增长率
示例：{\"company\": \"A公司\", \"revenue\": \"500亿\"}"""
    
    ax.text(1.2, 3.6, prompt_example, fontsize=10, ha='left', va='top', fontfamily='monospace')
    
    # Tips section
    tips_box = FancyBboxPatch((1, 0.8), 14, 1.2, 
                             boxstyle="round,pad=0.2", facecolor='#FADBD8', 
                             edgecolor='#E74C3C', linewidth=2)
    ax.add_patch(tips_box)
    
    ax.text(8, 1.7, '使用技巧', fontsize=12, fontweight='bold', ha='center', va='center', color='#E74C3C')
    
    tips = [
        '• 角色越具体，输出越专业',
        '• 格式要求要明确具体',
        '• 提供示例可减少歧义',
        '• 复杂任务可分解为多个步骤'
    ]
    
    for i, tip in enumerate(tips):
        x_pos = 3 + (i % 2) * 6
        y_pos = 1.4 - (i // 2) * 0.2
        ax.text(x_pos, y_pos, tip, fontsize=9, ha='left', va='center', color='#34495E')
    
    plt.tight_layout()
    plt.savefig('D:\STU\u8bfe\Slides - 副本\images\prompt_formula.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

# Create all improved diagrams
def main():
    print("Creating improved information extraction diagrams...")
    
    create_improved_structured_vs_unstructured()
    print("✓ Created improved structured vs unstructured data diagram")
    
    create_improved_information_extraction_pipeline()
    print("✓ Created improved information extraction pipeline diagram")
    
    create_improved_ner_example()
    print("✓ Created improved NER example diagram")
    
    create_improved_relation_extraction_example()
    print("✓ Created improved relation extraction example diagram")
    
    create_improved_event_extraction_example()
    print("✓ Created improved event extraction example diagram")
    
    create_improved_output_formats_comparison()
    print("✓ Created improved output formats comparison diagram")
    
    create_improved_prompt_formula()
    print("✓ Created improved prompt formula diagram")
    
    print("\n🎉 All improved diagrams created successfully!")
    print("Files saved to: D:/STU/开课/Slides - 副本/images/")

if __name__ == "__main__":
    main()