#!/usr/bin/env python3
"""
Create information_extraction_concept.png diagram
Shows the complete Information Extraction Architecture flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyBboxPatch, Circle, Arrow
import numpy as np

def create_information_extraction_concept():
    """Create comprehensive Information Extraction Architecture diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(18, 12))
    ax.set_xlim(0, 18)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(9, 11.5, '信息提取架构：从非结构化文本到结构化数据', fontsize=24, fontweight='bold', 
            ha='center', va='center', color='#2C3E50')
    
    # Subtitle
    ax.text(9, 11.1, 'Information Extraction Architecture Pipeline', fontsize=14, ha='center', va='center', 
           style='italic', color='#7F8C8D')
    
    # === INPUT SECTION (LEFT) ===
    input_header = FancyBboxPatch((0.5, 9), 5, 0.8, 
                                 boxstyle="round,pad=0.2", facecolor='#FADBD8', 
                                 edgecolor='#E74C3C', linewidth=3)
    ax.add_patch(input_header)
    ax.text(3, 9.4, '输入：非结构化文本', fontsize=16, fontweight='bold', ha='center', va='center', color='#E74C3C')
    
    # Input examples
    input_examples = [
        {
            'title': '财务报告',
            'content': 'A公司今日发布2025年Q2财报，\n营收500亿美元，同比增长15%，\nAI硬件"星尘"系列销售100亿美元。',
            'y_pos': 8.2,
            'color': '#FADBD8'
        },
        {
            'title': '新闻资讯',
            'content': '科技巨头A公司宣布新产品\n"星尘Pro"，CEO李明表示\n这将改变行业格局。',
            'y_pos': 6.8,
            'color': '#FADBD8'
        },
        {
            'title': '社交媒体',
            'content': '@A公司 的#星尘系列#真的\n太棒了！刚买了他们的新\n产品，性能超出预期！',
            'y_pos': 5.4,
            'color': '#FADBD8'
        }
    ]
    
    for example in input_examples:
        # Example box
        example_box = FancyBboxPatch((0.7, example['y_pos']-0.8), 4.6, 1.2, 
                                   boxstyle="round,pad=0.2", facecolor=example['color'], 
                                   edgecolor='#E74C3C', linewidth=2, alpha=0.6)
        ax.add_patch(example_box)
        
        # Title
        ax.text(2.9, example['y_pos']-0.2, example['title'], fontsize=12, fontweight='bold', 
               ha='center', va='center', color='#E74C3C')
        
        # Content
        ax.text(0.9, example['y_pos']-0.5, example['content'], fontsize=9, ha='left', va='top')
    
    # === PROCESSING SECTION (MIDDLE) ===
    process_header = FancyBboxPatch((6.5, 9), 5, 0.8, 
                                   boxstyle="round,pad=0.2", facecolor='#EBF5FB', 
                                   edgecolor='#3498DB', linewidth=3)
    ax.add_patch(process_header)
    ax.text(9, 9.4, '处理层：NLP流水线', fontsize=16, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    # NER Box
    ner_box = FancyBboxPatch((6.7, 7.8), 4.6, 1.2, 
                           boxstyle="round,pad=0.2", facecolor='#D6EAF8', 
                           edgecolor='#3498DB', linewidth=3)
    ax.add_patch(ner_box)
    ax.text(9, 8.6, '命名实体识别 (NER)', fontsize=14, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    ner_content = """识别文本中的实体：
• A公司 (组织机构)
• 星尘系列 (产品名称)  
• 李明 (人物姓名)
• 500亿美元 (金额)"""
    ax.text(6.9, 8.2, ner_content, fontsize=9, ha='left', va='top')
    
    # Arrow down to RE
    ax.arrow(9, 7.7, 0, -0.4, head_width=0.15, head_length=0.1, 
             fc='#27AE60', ec='#27AE60', linewidth=3)
    ax.text(9.5, 7.5, '实体→关系', fontsize=10, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    # RE Box
    re_box = FancyBboxPatch((6.7, 6.2), 4.6, 1.2, 
                          boxstyle="round,pad=0.2", facecolor='#D5F4E6', 
                          edgecolor='#27AE60', linewidth=3)
    ax.add_patch(re_box)
    ax.text(9, 7, '关系提取 (RE)', fontsize=14, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    re_content = """发现实体间关系：
• (A公司, 营收, 500亿美元)
• (A公司, 拥有产品, 星尘系列)
• (星尘系列, 销售额, 100亿美元)"""
    ax.text(6.9, 6.6, re_content, fontsize=9, ha='left', va='top')
    
    # Arrow down to EE
    ax.arrow(9, 6.1, 0, -0.4, head_width=0.15, head_length=0.1, 
             fc='#F39C12', ec='#F39C12', linewidth=3)
    ax.text(9.5, 5.9, '关系→事件', fontsize=10, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    # EE Box
    ee_box = FancyBboxPatch((6.7, 4.6), 4.6, 1.2, 
                          boxstyle="round,pad=0.2", facecolor='#FEF9E7', 
                          edgecolor='#F39C12', linewidth=3)
    ax.add_patch(ee_box)
    ax.text(9, 5.4, '事件提取 (EE)', fontsize=14, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    ee_content = """识别完整事件框架：
• 事件：财报发布
• 主体：A公司
• 时间：2025年Q2
• 关键数据：营收增长15%"""
    ax.text(6.9, 5, ee_content, fontsize=9, ha='left', va='top')
    
    # === OUTPUT SECTION (RIGHT) ===
    output_header = FancyBboxPatch((12.5, 9), 5, 0.8, 
                                  boxstyle="round,pad=0.2", facecolor='#D5F4E6', 
                                  edgecolor='#27AE60', linewidth=3)
    ax.add_patch(output_header)
    ax.text(15, 9.4, '输出：结构化数据', fontsize=16, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    # Output examples
    output_examples = [
        {
            'title': '实体数据库',
            'content': """[
  {"entity": "A公司", "type": "ORG"},
  {"entity": "星尘系列", "type": "PRODUCT"},
  {"entity": "李明", "type": "PERSON"}
]""",
            'y_pos': 8.2,
            'color': '#D5F4E6'
        },
        {
            'title': '关系网络',
            'content': """[
  {"subject": "A公司", "predicate": "营收", "object": "500亿美元"},
  {"subject": "A公司", "predicate": "拥有产品", "object": "星尘系列"}
]""",
            'y_pos': 6.8,
            'color': '#D5F4E6'
        },
        {
            'title': '事件框架',
            'content': """{
  "event_type": "财报发布",
  "company": "A公司",
  "quarter": "Q2 2025",
  "revenue": "500亿美元",
  "growth": "15%",
  "key_product": "星尘系列"
}""",
            'y_pos': 5.4,
            'color': '#D5F4E6'
        }
    ]
    
    for example in output_examples:
        # Example box
        example_box = FancyBboxPatch((12.7, example['y_pos']-0.8), 4.6, 1.2, 
                                   boxstyle="round,pad=0.2", facecolor=example['color'], 
                                   edgecolor='#27AE60', linewidth=2, alpha=0.6)
        ax.add_patch(example_box)
        
        # Title
        ax.text(14.9, example['y_pos']-0.2, example['title'], fontsize=12, fontweight='bold', 
               ha='center', va='center', color='#27AE60')
        
        # Content
        ax.text(12.9, example['y_pos']-0.5, example['content'], fontsize=8, ha='left', va='top',
               fontfamily='monospace')
    
    # === ARROWS CONNECTING SECTIONS ===
    # Input to Processing
    ax.arrow(5.7, 8.5, 0.6, 0, head_width=0.2, head_length=0.1, 
             fc='#3498DB', ec='#3498DB', linewidth=4)
    ax.text(6, 8.8, '文本输入', fontsize=12, fontweight='bold', ha='center', va='center', color='#3498DB')
    
    # Processing to Output
    ax.arrow(11.7, 8.5, 0.6, 0, head_width=0.2, head_length=0.1, 
             fc='#27AE60', ec='#27AE60', linewidth=4)
    ax.text(12, 8.8, '结构化输出', fontsize=12, fontweight='bold', ha='center', va='center', color='#27AE60')
    
    # === LEGEND AND APPLICATIONS ===
    # Applications box
    apps_box = FancyBboxPatch((2, 2.5), 14, 1.5, 
                             boxstyle="round,pad=0.3", facecolor='#FEF9E7', 
                             edgecolor='#F39C12', linewidth=2, linestyle='--')
    ax.add_patch(apps_box)
    
    ax.text(9, 3.5, '应用场景', fontsize=16, fontweight='bold', ha='center', va='center', color='#F39C12')
    
    applications = [
        '数据新闻自动摘要',
        '投资分析报告生成',
        '竞品情报收集',
        '舆情监测分析',
        '知识图谱构建',
        '智能问答系统'
    ]
    
    for i, app in enumerate(applications):
        x_pos = 3 + (i % 3) * 4
        y_pos = 3.1 - (i // 3) * 0.3
        ax.text(x_pos, y_pos, f'• {app}', fontsize=11, ha='left', va='center', color='#34495E')
    
    # Technical notes
    ax.text(9, 1.2, '技术特点：基于深度学习的端到端信息提取 | 支持多语言 | 实时处理 | 高准确率', 
           fontsize=11, ha='center', va='center', style='italic', color='#7F8C8D')
    
    # Color legend
    legend_box = FancyBboxPatch((0.5, 0.3), 17, 0.6, 
                               boxstyle="round,pad=0.2", facecolor='#F8F9FA', 
                               edgecolor='#BDC3C7', linewidth=1)
    ax.add_patch(legend_box)
    
    ax.text(1, 0.6, '颜色说明：', fontsize=10, fontweight='bold', ha='left', va='center')
    ax.text(2.5, 0.6, '● 输入层 (红色)', fontsize=9, ha='left', va='center', color='#E74C3C')
    ax.text(5, 0.6, '● 处理层 (蓝色→绿色→橙色)', fontsize=9, ha='left', va='center', color='#3498DB')
    ax.text(9, 0.6, '● 输出层 (绿色)', fontsize=9, ha='left', va='center', color='#27AE60')
    ax.text(12, 0.6, '● 应用层 (橙色虚线)', fontsize=9, ha='left', va='center', color='#F39C12')
    
    plt.tight_layout()
    plt.savefig('D:/STU/开课/Slides - 副本/images/information_extraction_concept.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created information_extraction_concept.png")

if __name__ == "__main__":
    create_information_extraction_concept()