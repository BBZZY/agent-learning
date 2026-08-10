"""阶段0冒烟测试：SQLite 最小读写（阶段1预热，社区随访场景）

功能：建表 → 插入 → 查询 → 关闭。验证 Python + SQLite 环境就绪。
"""
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "demo.db"

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS followups")
cur.execute(
    """
    CREATE TABLE followups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient TEXT NOT NULL,
        diagnosis TEXT,
        followup_date TEXT,
        note TEXT
    )
    """
)

cur.executemany(
    "INSERT INTO followups (patient, diagnosis, followup_date, note) VALUES (?,?,?,?)",
    [
        ("王阿姨", "高血压", "2026-08-11", "血压140/90，按时服药"),
        ("李叔", "2型糖尿病", "2026-08-11", "空腹血糖6.8，饮食控制良好"),
    ],
)
conn.commit()

rows = cur.execute("SELECT * FROM followups").fetchall()
for row in rows:
    print(row)
print(f"共 {len(rows)} 条随访记录，数据库文件: {DB_PATH.name}")
conn.close()
