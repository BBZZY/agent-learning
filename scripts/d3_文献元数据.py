# d3_文献元数据.py
# D3 精读示例：用 Python 处理"医学文献元数据"
# 运行：.venv/bin/python scripts/d3_文献元数据.py

# ========== 块1：单篇文献 = 一个 dict（键值对） ==========
paper1 = {
    "pmid": "37600001",
    "title": "Large language models for automated code generation: a systematic review",
    "journal": "TOSEM",
    "year": 2023,
    "authors": ["Zhang W", "Li M", "Wang H"],
}

# ========== 块2：文献列表 = 一个 list（一列 dict） ==========
papers = [
    paper1,
    {"pmid": "37600002", "title": "Retrieval-augmented generation for knowledge-intensive NLP tasks",
     "journal": "NeurIPS", "year": 2021, "authors": ["Chen Y", "Liu S"]},
    {"pmid": "37600003", "title": "A survey on multi-agent reinforcement learning",
     "journal": "AI Review", "year": 2019, "authors": ["Zhao Q", "Sun K", "Xu L"]},
    {"pmid": "37600004", "title": "Deep learning approaches in educational data mining",
     "journal": "Computers & Education", "year": 2022, "authors": ["Wu J"]},
    {"pmid": "37600005", "title": "Model context protocol: standardizing agent-tool integration",
     "journal": "arXiv", "year": 2024, "authors": ["Huang R", "Zhou T", "Ma F", "Guo D"]},
]

# ========== 块3：for 循环 + len() ==========
print("== 文献总数 ==")
print(len(papers))          # len() 数一列数据有几个

# ========== 块4：for + if 筛选 ==========
print("== 2020 年及以后的文献 ==")
for paper in papers:        # 每篇依次取名 paper
    if paper["year"] >= 2020:   # 条件判断（缩进表示属于 if）
        print(paper["year"], paper["title"])

# ========== 块5：函数 + f-string ==========
def format_citation(paper):     # 定义函数（缩进=函数体）
    authors = ", ".join(paper["authors"])   # join：把作者列表拼成字符串
    return f"{authors}. {paper['title']}. {paper['journal']} {paper['year']}."

print("== 引用格式输出 ==")
for paper in papers:
    print(format_citation(paper))

# ========== 块6：dict 计数（统计各期刊文献数） ==========
journal_count = {}
for paper in papers:
    journal = paper["journal"]
    if journal in journal_count:          # 已出现过 → 计数 +1
        journal_count[journal] = journal_count[journal] + 1
    else:                                 # 第一次出现 → 从 1 开始
        journal_count[journal] = 1

print("== 各期刊文献数 ==")
for journal, count in journal_count.items():   # items() 取出每个键值对
    print(journal, count)
