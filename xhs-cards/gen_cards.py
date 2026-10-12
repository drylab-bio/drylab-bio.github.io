#!/usr/bin/env python3
"""Generate 8 XHS card HTML files (1080x1440, DRYLAB dark theme). v2: fix footer overflow + shared bar baseline."""
import os

OUT = os.path.dirname(os.path.abspath(__file__))

CSS = """
* { margin:0; padding:0; box-sizing:border-box; }
html,body { width:1080px; height:1440px; overflow:hidden; }
:root {
  --page:#0d0d0d; --surface:#1a1a19; --surface2:#232322;
  --ink:#ffffff; --ink2:#c3c2b7; --muted:#898781;
  --grid:#2c2c2a; --border:rgba(255,255,255,.10);
  --accent:#3987e5; --accent-ink:#86b6ef; --wash:#16283f; --floor:#d95926;
}
body {
  font-family:-apple-system,"PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif;
  background:var(--page); color:var(--ink);
  width:1080px; height:1440px; position:relative;
  display:flex; flex-direction:column; padding:96px 90px 60px;
}
body::before {
  content:""; position:absolute; inset:0;
  background:radial-gradient(900px 500px at 85% -5%, rgba(57,135,229,.14), transparent 60%),
             radial-gradient(700px 420px at -10% 105%, rgba(57,135,229,.07), transparent 55%);
  pointer-events:none;
}
.mono { font-family:"SF Mono",ui-monospace,Menlo,Consolas,monospace; }
.top { display:flex; justify-content:space-between; align-items:center; margin-bottom:70px; }
.brand { font-size:30px; letter-spacing:.28em; color:var(--muted); font-weight:600; }
.tag { font-size:28px; color:var(--accent-ink); border:1.5px solid rgba(57,135,229,.45);
       padding:10px 26px; border-radius:999px; background:var(--wash); }
.footer { margin-top:auto; padding-top:36px; border-top:1px solid var(--border);
          display:flex; justify-content:space-between; align-items:center; }
.footer .fbrand { font-size:26px; color:var(--muted); letter-spacing:.2em; }
.footer .fnum { font-size:28px; color:var(--muted); }
.card { background:var(--surface); border:1px solid var(--border); border-radius:28px; }
"""

def shell(body: str, num: int, total: int = 8) -> str:
    return ("<!DOCTYPE html><html lang=\"zh\"><head><meta charset=\"utf-8\">"
            "<style>" + CSS + "</style></head><body>" + body +
            '<div class="footer"><span class="fbrand">DRYLAB-BENCH · AI 生物安全风险评测</span>'
            '<span class="fnum mono">' + f"{num:02d} / {total:02d}" + "</span></div>"
            "</body></html>")

cards = {}

# ---------------- Card 1 · cover ----------------
cards[1] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">真实数据阅卷</span></div>
<div style="flex:1; display:flex; align-items:center;">
  <div class="card" style="width:100%; padding:90px 80px 76px; position:relative; background:linear-gradient(180deg,#1c1c1b,#171716);">
    <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:64px;">
      <span style="font-size:30px; color:var(--muted); letter-spacing:.18em;">模拟考 · 生物设计卷</span>
      <span class="mono" style="font-size:28px; color:var(--muted);">NO. 2026-001</span>
    </div>
    <div style="font-size:118px; font-weight:800; line-height:1.22;">AI 生物考试<br>成绩单出炉</div>
    <div style="margin-top:70px; display:flex; flex-direction:column; gap:30px; font-size:36px;">
      <div style="display:flex; gap:34px;"><span style="color:var(--muted); width:150px; flex:none;">考　生</span><span>15 个顶流大模型</span></div>
      <div style="display:flex; gap:34px;"><span style="color:var(--muted); width:150px; flex:none;">考　题</span><span>给蛋白质设计突变</span></div>
      <div style="display:flex; gap:34px;"><span style="color:var(--muted); width:150px; flex:none;">阅卷人</span><span>18 万条真实实验数据</span></div>
    </div>
    <div style="position:absolute; right:64px; top:150px; transform:rotate(12deg);
                border:5px solid #e5484d; color:#e5484d; border-radius:22px;
                font-size:44px; font-weight:800; padding:16px 30px; letter-spacing:.1em; opacity:.92;">
      分数偏高 ⚠</div>
  </div>
</div>
<div style="display:flex; justify-content:space-between; align-items:center; margin-top:56px;">
  <span style="font-size:34px; color:var(--ink2);">模型全程看不到标准答案</span>
  <span style="font-size:34px; color:var(--accent-ink); font-weight:700;">左滑看成绩 →</span>
</div>
'''

# ---------------- Card 2 · rules ----------------
rows2 = [
    ("考　官", "18 万条真实湿实验数据"),
    ("考　生", "15 个顶流大模型"),
    ("考　题", "给真实蛋白质设计突变"),
    ("阅　卷", "只按实验数据打分，不听模型自评"),
    ("监　考", "标准答案全程封存，模型看不到"),
]
rows_html = ""
for i, (k, v) in enumerate(rows2):
    border = "border-bottom:1px solid var(--border);" if i < len(rows2) - 1 else ""
    rows_html += ('<div style="display:flex; align-items:baseline; gap:36px; padding:30px 0;' + border + '">'
                  '<span class="mono" style="flex:none; width:190px; font-size:32px; color:var(--accent-ink); font-weight:700;">' + k + '</span>'
                  '<span style="font-size:40px; font-weight:600; line-height:1.4;">' + v + '</span></div>')
cards[2] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">考场规则</span></div>
<div style="font-size:80px; font-weight:800; margin-bottom:26px;">先说规矩</div>
<div style="font-size:34px; color:var(--muted); margin-bottom:16px;">这是一场不能作弊的考试</div>
<div class="card" style="padding:8px 54px;">''' + rows_html + '''</div>
<div style="margin-top:30px; font-size:31px; color:var(--ink2); line-height:1.6;">
数据来源：ProteinGym / ViroGym 真实 DMS 测量<br>
30 个场景 · 6 类任务 · 187,695 条实验测量</div>
'''

# ---------------- Card 3 · 67.6% ----------------
cards[3] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">成绩单 · 第 1 条</span></div>
<div style="flex:1; display:flex; flex-direction:column; justify-content:center;">
  <div style="font-size:44px; color:var(--ink2); margin-bottom:10px;">一次提问，AI 的设计就跑赢了</div>
  <div class="mono" style="font-size:300px; font-weight:800; line-height:1.05;
       background:linear-gradient(90deg,#6da7ec,#3987e5); -webkit-background-clip:text; background-clip:text; color:transparent;">67.6<span style="font-size:150px;">%</span></div>
  <div style="font-size:56px; font-weight:800; margin:36px 0 40px;">的“平均变体”</div>
  <div style="font-size:38px; color:var(--ink2); line-height:1.75; max-width:880px;">
    在不能调工具、不能多轮迭代的 one-shot 模式下，67.6% 的 AI 设计突变，优于该基因上实测变异体的平均水平。</div>
  <div style="margin-top:56px; padding:34px 40px; border-left:6px solid var(--accent); background:var(--wash); border-radius:0 20px 20px 0; font-size:36px; line-height:1.6;">
    AI 挑突变，不是瞎蒙。</div>
</div>
'''

# ---------------- Card 4 · bars (shared baseline) ----------------
bars = [
    ("S0　一次提问", 0.359, False),
    ("+ 自我迭代", 0.371, False),
    ("+ 工具调用", 0.407, False),
    ("agent 全开", 0.475, True),
]
bars_html = ""
for label, v, hi in bars:
    hp = v / 0.475 * 100
    color = "linear-gradient(180deg,#6da7ec,#2a78d6)" if hi else "#3a3a38"
    numcolor = "var(--accent-ink)" if hi else "var(--ink2)"
    bars_html += ('<div style="flex:1; display:flex; flex-direction:column; align-items:center; height:100%;">'
                  '<span class="mono" style="font-size:44px; font-weight:800; color:' + numcolor + ';">' + f"{v:.3f}" + '</span>'
                  '<div style="width:150px; flex:1; display:flex; align-items:flex-end; margin-top:18px;">'
                  '<div style="width:100%; height:' + f"{hp:.1f}" + '%; border-radius:18px 18px 0 0; background:' + color + ';"></div>'
                  '</div>'
                  '<span style="font-size:28px; white-space:nowrap; margin-top:24px; color:' + ("var(--ink)" if hi else "var(--muted)") + '; font-weight:' + ("700" if hi else "400") + ';">' + label + '</span></div>')
cards[4] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">成绩单 · 第 2 条</span></div>
<div style="font-size:84px; font-weight:800; margin-bottom:20px;">放开手脚之后，涨了</div>
<div style="font-size:34px; color:var(--muted); margin-bottom:60px;">整体风险分（BRS）· pooled · 15 个模型平均</div>
<div style="display:flex; align-items:stretch; gap:48px; height:700px; padding:0 20px;">''' + bars_html + '''</div>
<div style="margin-top:56px; display:flex; align-items:center; gap:28px;">
  <span class="mono" style="font-size:40px; font-weight:800; color:#0d0d0d; background:linear-gradient(90deg,#6da7ec,#3987e5); padding:12px 30px; border-radius:14px;">总涨幅 +0.116</span>
  <span style="font-size:33px; color:var(--ink2); line-height:1.5;">agent 化 = 让模型自己边想边干</span>
</div>
'''

# ---------------- Card 5 · dumbbell ----------------
models = [  # name, s0, s2, delta, highlight
    ("Claude Fable 5",   0.287, 0.754, "+0.467", True),
    ("Kimi-K3",          0.519, 0.631, "+0.112", False),
    ("GLM-5.3",          0.394, 0.492, "+0.098", False),
    ("DeepSeek V4 Pro",  0.276, 0.483, "+0.207", False),
    ("Grok 4.5",         0.368, 0.467, "+0.099", False),
    ("DeepSeek V4 Flash",0.428, 0.416, "-0.012", False),
    ("Claude Opus 5",    0.378, 0.383, "+0.005", False),
    ("Claude Opus 4.8",  0.227, 0.369, "+0.142", False),
]
def pct(v):  # scale 0.2–0.8
    return (v - 0.2) / 0.6 * 100
dumb = ""
for name, s0, s2, delta, hi in models:
    l, r = pct(min(s0, s2)), pct(max(s0, s2))
    line = "linear-gradient(90deg,#6da7ec,#3987e5)" if hi else "#3a3a38"
    dot0 = "#5c5c58"
    dot2 = "var(--accent)" if hi else "#4f7fc0"
    dumb += ('<div style="display:flex; align-items:center; gap:26px; padding:12px 0;'
             + ("background:var(--wash); border-radius:16px; margin:0 -24px; padding-left:24px; padding-right:24px;" if hi else "") + '">'
             '<span style="flex:none; width:300px; font-size:' + ("34px" if hi else "30px") + '; font-weight:' + ("800" if hi else "500") + '; color:' + ("var(--ink)" if hi else "var(--ink2)") + ';">' + name + '</span>'
             '<div style="flex:1; position:relative; height:44px;">'
             '<div style="position:absolute; top:50%; transform:translateY(-50%); height:8px; left:' + f"{l:.1f}" + '%; width:' + f"{r-l:.1f}" + '%; background:' + line + '; border-radius:4px;"></div>'
             f'<div style="position:absolute; top:50%; transform:translate(-50%,-50%); width:26px; height:26px; border-radius:50%; background:{dot0}; left:{l:.1f}%;"></div>'
             f'<div style="position:absolute; top:50%; transform:translate(-50%,-50%); width:32px; height:32px; border-radius:50%; background:{dot2}; left:{r:.1f}%; box-shadow:{("0 0 0 8px rgba(57,135,229,.25)" if hi else "none")};"></div>'
             '</div>'
             f'<span class="mono" style="flex:none; width:160px; text-align:right; font-size:34px; font-weight:800; color:{"var(--accent-ink)" if hi else "var(--muted)"};">{delta}</span></div>')
cards[5] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">成绩单 · 第 3 条</span></div>
<div style="font-size:84px; font-weight:800; margin-bottom:14px;">最大黑马：+0.467</div>
<div style="font-size:34px; color:var(--muted); margin-bottom:30px;">灰点 = 一次提问　蓝点 = agent 全开　（BRS，0 为实验均值基线）</div>
<div class="card" style="padding:16px 36px;">''' + dumb + '''</div>
<div style="margin-top:28px; font-size:34px; line-height:1.6; color:var(--ink2);">
<b style="color:var(--ink);">Claude Fable 5：0.287 → 0.754。</b><br>
one-shot 时期还在下游，agent 化后直接冲到全场最高分。</div>
'''

# ---------------- Card 6 · 金句 ----------------
steps = [("多轮对话", "+0.068", 100), ("工具调用", "+0.048", 71), ("自我迭代", "+0.012", 18)]
step_html = ""
for name, d, w in steps:
    step_html += ('<div style="margin-bottom:52px;">'
                  '<div style="display:flex; justify-content:space-between; margin-bottom:20px;">'
                  f'<span style="font-size:40px; font-weight:700;">{name}</span>'
                  f'<span class="mono" style="font-size:44px; font-weight:800; color:var(--accent-ink);">{d}</span></div>'
                  f'<div style="height:26px; border-radius:13px; background:var(--surface2); overflow:hidden;">'
                  f'<div style="height:100%; width:{w}%; border-radius:13px; background:linear-gradient(90deg,#2a78d6,#6da7ec);"></div></div></div>')
cards[6] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">涨分玄学</span></div>
<div style="font-size:84px; font-weight:800; margin-bottom:64px;">涨分，涨在哪一步？</div>
<div style="padding:0 10px;">''' + step_html + '''</div>
<div style="flex:1; display:flex; align-items:center;">
  <div style="font-size:76px; font-weight:800; line-height:1.5;">
    <span style="color:var(--accent-ink);">「</span>会反思，<br>比会用工具更涨分。<span style="color:var(--accent-ink);">」</span></div>
</div>
<div style="font-size:34px; color:var(--ink2); line-height:1.7;">拆开算账才发现：让模型"多想几轮"，比给它接一堆专业工具更管用。</div>
'''

# ---------------- Card 7 · 四条规矩 ----------------
rules = [
    ("01", "纯计算评估", "全程 in silico，零湿实验、零合成"),
    ("02", "答案封存", "模型从始至终看不到真实数据标签"),
    ("03", "防刷题", "30 个场景只开源 15 个，其余 15 个作为盲考卷"),
    ("04", "可复现", "代码、分数、开放场景数据全部开源"),
]
rules_html = ""
for i, (n, t, d) in enumerate(rules):
    border = "border-bottom:1px solid var(--border);" if i < len(rules) - 1 else ""
    rules_html += ('<div style="display:flex; gap:40px; align-items:flex-start; padding:34px 0;' + border + '">'
                   f'<span class="mono" style="flex:none; font-size:48px; font-weight:800; color:var(--accent); opacity:.9;">{n}</span>'
                   '<div><div style="font-size:42px; font-weight:800; margin-bottom:8px;">' + t + '</div>'
                   '<div style="font-size:32px; color:var(--ink2); line-height:1.55;">' + d + '</div></div></div>')
cards[7] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">Responsible Release</span></div>
<div style="font-size:80px; font-weight:800; margin-bottom:18px;">为什么我们敢公开</div>
<div style="font-size:34px; color:var(--muted); margin-bottom:18px;">红线先划好，数据再出门</div>
<div class="card" style="padding:6px 50px;">''' + rules_html + '''</div>
<div style="margin-top:24px; font-size:30px; color:var(--muted); line-height:1.6;">
完整 Responsible Use 声明见项目主页。本笔记仅引用聚合统计，不含任何具体序列或场景细节。</div>
'''

# ---------------- Card 8 · 资源卡 ----------------
res = [
    ("🌐", "项目主页", "drylab-bio.github.io"),
    ("🐙", "GitHub", "drylab-bio/DRYLAB-Bench"),
    ("📄", "论文", "arXiv 即将上线"),
]
res_html = ""
for i, (ic, k, v) in enumerate(res):
    border = "border-bottom:1px solid var(--border);" if i < len(res) - 1 else ""
    res_html += ('<div style="display:flex; align-items:center; gap:34px; padding:32px 0;' + border + '">'
                 f'<span style="flex:none; font-size:52px;">{ic}</span>'
                 f'<span style="flex:none; width:190px; font-size:34px; color:var(--muted);">{k}</span>'
                 f'<span class="mono" style="font-size:34px; font-weight:700; white-space:nowrap;">{v}</span></div>')
cards[8] = '''
<div class="top"><span class="brand">DRYLAB-BENCH</span><span class="tag">资源卡</span></div>
<div style="font-size:84px; font-weight:800; margin-bottom:40px;">想看原文的，<br>收好这张图</div>
<div class="card" style="padding:10px 54px;">''' + res_html + '''</div>
<div style="flex:1; display:flex; flex-direction:column; justify-content:center; align-items:center; gap:28px;">
  <div style="font-size:72px; font-weight:800;">收藏这张图就够了 📌</div>
  <div style="font-size:34px; color:var(--muted);">论文挂出后，评论区置顶第一时间更新</div>
</div>
<div style="margin-bottom:48px; padding:28px 40px; border-radius:20px; background:var(--wash); font-size:33px; color:var(--accent-ink); line-height:1.6;">
关于评测设计的问题，评论区必回。</div>
'''

for num, body in cards.items():
    path = os.path.join(OUT, f"card{num}.html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(shell(body, num))
    print("wrote", path)
