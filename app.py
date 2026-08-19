# -*- coding: utf-8 -*-
"""
データ基盤構築の考え方と業務自動化 — Streamlit プレゼンテーション
------------------------------------------------------------------
紫のバブル（円）モチーフのテンプレートを再現し、ページ遷移のたびに
2つの円が動いてから文字が現れるアニメーションを実装しています。

デプロイ方法:
    1) requirements.txt の内容で依存関係をインストール
       pip install -r requirements.txt
    2) 実行
       streamlit run app.py
    3) Streamlit Community Cloud にそのまま push すればデプロイ可能です。

内容を編集したい場合は、ファイル下部の `SLIDES` リストを書き換えてください。
"""

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="データ基盤構築の考え方と業務自動化", layout="wide")

# ----------------------------------------------------------------------------
# スライドの内容定義（ここを書き換えれば内容をカスタマイズできます）
# ----------------------------------------------------------------------------
SLIDES = [
    {
        "type": "title",
        "title_lines": ["データ基盤構築の考え方と", "業務自動化"],
        "reporter": "Reporter: XXX",
        "date": "XX.XX.XX",
    },
    {
        "type": "toc",
        "heading": "Contents",
        "subtitle": "本日の流れ",
        "items": [
            "経歴と提案の背景",
            "自動化の実例と成果",
            "現在の三つの課題",
            "改善の全体設計",
            "導入方法と期待効果",
            "今後の進め方",
        ],
    },
    {
        "type": "section",
        "num": "01",
        "title": "経歴と提案の背景",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
    },
    {
        "type": "section",
        "num": "02",
        "title": "自動化の実例と成果",
        "points": [
            "日報タブの月次複製をGASで自動化（テーブル名・数式参照・日付を自動更新）",
            "収益実績シートの出荷金額・返品金額・数量集計をGAS関数で自動更新",
            "広告実績データをPython（gspread）で取得し、レート換算のうえ月次日報へ反映",
            "週報と日報をGASで連携し、媒体別（Facebook / GSEM / YouTube）の実績を自動集計",
        ],
    },
    {
        "type": "section",
        "num": "03",
        "title": "現在の三つの課題",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
    },
    {
        "type": "section",
        "num": "04",
        "title": "改善の全体設計",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
    },
    {
        "type": "section",
        "num": "05",
        "title": "導入方法と期待効果",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
    },
    {
        "type": "section",
        "num": "06",
        "title": "今後の進め方",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
    },
]

CANVAS_W = 1160
CANVAS_H = 653

# ----------------------------------------------------------------------------
# 共通スタイル
# ----------------------------------------------------------------------------
BASE_CSS = f"""
* {{ box-sizing: border-box; }}
html, body {{ margin:0; padding:0; background: transparent; }}
.stage {{
  position: relative;
  width: {CANVAS_W}px;
  height: {CANVAS_H}px;
  margin: 0 auto;
  background: linear-gradient(155deg, #fbf9fe 0%, #f6f1fc 55%, #f1e9fb 100%);
  border-radius: 28px;
  overflow: hidden;
  box-shadow: 0 18px 46px rgba(109, 40, 217, 0.14);
  font-family: "Hiragino Kaku Gothic ProN", "Noto Sans JP", "Helvetica Neue", Arial, sans-serif;
}}
.circle {{
  position: absolute;
  border-radius: 50%;
  will-change: transform, opacity;
  animation-fill-mode: forwards;
  animation-timing-function: cubic-bezier(.22,.9,.32,1);
}}
.ball-a {{
  background: radial-gradient(circle at 32% 30%, #c9b7f7 0%, #9b6ff0 55%, #7c4fe0 100%);
  opacity: 0.9;
  animation-name: ballInA;
  animation-duration: 1000ms;
}}
.ball-b {{
  background: radial-gradient(circle at 35% 32%, #e4d7fb 0%, #b79af2 60%, #9b6ff0 100%);
  opacity: 0.55;
  animation-name: ballInB;
  animation-duration: 1150ms;
  animation-delay: 80ms;
}}
@keyframes ballInA {{
  0%   {{ transform: translate(var(--dxA), var(--dyA)) scale(0.55); opacity: 0; }}
  62%  {{ transform: translate(calc(var(--dxA) * 0.12), calc(var(--dyA) * 0.12)) scale(1.05); opacity: 0.9; }}
  100% {{ transform: translate(0,0) scale(1); opacity: 0.9; }}
}}
@keyframes ballInB {{
  0%   {{ transform: translate(var(--dxB), var(--dyB)) scale(0.55); opacity: 0; }}
  62%  {{ transform: translate(calc(var(--dxB) * 0.12), calc(var(--dyB) * 0.12)) scale(1.05); opacity: 0.55; }}
  100% {{ transform: translate(0,0) scale(1); opacity: 0.55; }}
}}
.textup {{
  opacity: 0;
  transform: translateY(20px);
  animation: textIn 650ms cubic-bezier(.22,.9,.32,1) forwards;
}}
@keyframes textIn {{
  to {{ opacity: 1; transform: translateY(0); }}
}}
.pagefoot {{
  position:absolute; bottom:22px; right:34px;
  font-size:12px; letter-spacing:.08em; color:#a48fe0;
  opacity:0; animation: textIn 500ms ease forwards; animation-delay: 1.05s;
}}
@media (prefers-reduced-motion: reduce) {{
  .circle, .textup, .pagefoot {{ animation: none !important; opacity: 1 !important; transform:none !important; }}
}}
"""

def _points_html(points, delay_base=0.85, step=0.1):
    lis = []
    for i, p in enumerate(points):
        d = delay_base + i * step
        lis.append(
            f'<li class="textup" style="animation-delay:{d:.2f}s">{p}</li>'
        )
    return "\n".join(lis)


def render_title(slide):
    lines_html = "".join(f"<div>{ln}</div>" for ln in slide["title_lines"])
    html = f"""
    <style>{BASE_CSS}
      .t-badge {{ position:absolute; top:0; left:0; width:180px; height:180px;
        background: radial-gradient(circle at 65% 65%, #d9c8fb 0%, #efe6fb 70%, transparent 100%);
        border-radius: 0 0 100% 0; opacity:.8; }}
      .t-title {{ position:absolute; left:70px; top:225px; font-size:44px; font-weight:800;
        color:#6d28d9; line-height:1.25; letter-spacing:.01em; }}
      .t-sub {{ position:absolute; left:70px; top:398px; font-size:15px; color:#7c5fc4; }}
      .t-sub .dot {{ display:inline-block; width:34px; height:34px; border-radius:50%;
        background: radial-gradient(circle at 35% 30%, #e4d7fb, #b79af2); margin-right:12px; vertical-align:middle; }}
      .t-line {{ position:absolute; right:60px; top:96px; width:2px; height:410px; background:#c8b3f5; opacity:.8; }}
      .t-dot {{ position:absolute; right:52px; top:88px; width:18px; height:18px; border-radius:50%; background:#8b5cf6; }}
    </style>
    <div class="stage">
      <div class="t-badge"></div>
      <div class="ball-a" style="width:460px;height:460px; right:-140px; bottom:-150px;
           --dxA:180px; --dyA:120px;"></div>
      <div class="ball-b" style="width:300px;height:300px; right:200px; bottom:-40px;
           --dxB:-140px; --dyB:160px;"></div>
      <div class="t-line"></div>
      <div class="t-dot"></div>
      <div class="t-title textup" style="animation-delay:.6s">{lines_html}</div>
      <div class="t-sub textup" style="animation-delay:.85s">
        <span class="dot"></span>{slide['reporter']}<br/><span style="margin-left:46px; display:inline-block; margin-top:6px;">{slide['date']}</span>
      </div>
    </div>
    """
    return html


def render_toc(slide):
    items_html = []
    for i, item in enumerate(slide["items"], start=1):
        d = 0.9 + (i - 1) * 0.1
        items_html.append(f"""
        <div class="toc-row textup" style="animation-delay:{d:.2f}s">
          <span class="toc-num">{i:02d}</span><span class="toc-txt">{item}</span>
        </div>""")
    items_html = "\n".join(items_html)
    html = f"""
    <style>{BASE_CSS}
      .c-corner {{ position:absolute; width:70px; height:70px; border-radius:50%;
        background: radial-gradient(circle at 35% 32%, #e4d7fb, #b79af2); opacity:.7; }}
      .c-heading {{ position:absolute; left:96px; top:296px; font-size:36px; font-weight:800; color:#6d28d9; }}
      .toc-panel {{ position:absolute; left:520px; top:190px; width:520px; }}
      .toc-row {{ display:flex; align-items:baseline; gap:18px; padding:14px 0; border-bottom:1px solid rgba(140,100,220,.14); }}
      .toc-num {{ font-size:15px; font-weight:700; color:#9b6ff0; width:28px; }}
      .toc-txt {{ font-size:19px; font-weight:600; color:#4c3a86; }}
    </style>
    <div class="stage">
      <div class="c-corner" style="top:26px; right:70px;"></div>
      <div class="ball-a" style="width:400px;height:400px; left:-160px; top:130px;
           --dxA:-180px; --dyA:-60px;"></div>
      <div class="ball-b" style="width:260px;height:260px; left:60px; top:340px;
           --dxB:-140px; --dyB:140px;"></div>
      <div class="c-heading textup" style="animation-delay:.62s">{slide['heading']}</div>
      <div class="toc-panel">{items_html}</div>
      <div class="pagefoot">{slide.get('subtitle','')}</div>
    </div>
    """
    return html


def render_section(slide):
    points_html = _points_html(slide["points"], delay_base=0.95, step=0.12)
    html = f"""
    <style>{BASE_CSS}
      .s-corner {{ position:absolute; width:60px; height:60px; border-radius:50%;
        background: radial-gradient(circle at 35% 32%, #e4d7fb, #b79af2); opacity:.65; }}
      .s-num {{ position:absolute; left:118px; top:260px; font-size:26px; font-weight:800; color:#fff;
        letter-spacing:.08em; z-index:3; }}
      .s-num-label {{ position:absolute; left:118px; top:300px; font-size:15px; color:#efe6fb; z-index:3; }}
      .s-title {{ position:absolute; left:560px; top:250px; font-size:34px; font-weight:800; color:#5b3aa8; width:520px; }}
      .s-points {{ position:absolute; left:560px; top:330px; width:540px; list-style:none; margin:0; padding:0; }}
      .s-points li {{ font-size:16px; color:#5c4a8a; line-height:1.7; margin-bottom:12px; padding-left:18px; position:relative; }}
      .s-points li:before {{ content:""; position:absolute; left:0; top:9px; width:6px; height:6px; border-radius:50%; background:#9b6ff0; }}
    </style>
    <div class="stage">
      <div class="s-corner" style="top:24px; right:64px;"></div>
      <div class="s-corner" style="width:34px;height:34px; bottom:30px; right:150px;"></div>
      <div class="ball-a" style="width:430px;height:430px; left:-190px; top:110px;
           --dxA:-190px; --dyA:-90px;"></div>
      <div class="ball-b" style="width:260px;height:260px; left:70px; top:330px;
           --dxB:-120px; --dyB:150px;"></div>
      <div class="s-num textup" style="animation-delay:.58s">{slide['num']}</div>
      <div class="s-num-label textup" style="animation-delay:.7s">SECTION</div>
      <div class="s-title textup" style="animation-delay:.68s">{slide['title']}</div>
      <ul class="s-points">{points_html}</ul>
    </div>
    """
    return html


RENDERERS = {"title": render_title, "toc": render_toc, "section": render_section}


def render_slide_html(slide):
    return RENDERERS[slide["type"]](slide)


# ----------------------------------------------------------------------------
# Streamlit アプリ本体
# ----------------------------------------------------------------------------
st.markdown(
    """
    <style>
      .block-container {padding-top: 2rem; padding-bottom: 1rem; max-width: 1220px;}
      div[data-testid="stHorizontalBlock"] {align-items:center;}
    </style>
    """,
    unsafe_allow_html=True,
)

if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

n = len(SLIDES)
idx = st.session_state.slide_idx

col_prev, col_mid, col_next = st.columns([1, 6, 1])
with col_prev:
    if st.button("◀ 前へ", use_container_width=True, disabled=(idx == 0)):
        st.session_state.slide_idx = max(0, idx - 1)
        st.rerun()
with col_next:
    if st.button("次へ ▶", use_container_width=True, disabled=(idx == n - 1)):
        st.session_state.slide_idx = min(n - 1, idx + 1)
        st.rerun()
with col_mid:
    st.markdown(
        f"<div style='text-align:center;color:#8b5cf6;font-weight:600;'>"
        f"{idx + 1} / {n}</div>",
        unsafe_allow_html=True,
    )

current = SLIDES[idx]
# key を slide_idx に紐づけることで、切り替えるたびにコンポーネントが
# 再マウントされ、円と文字のアニメーションが毎回再生されます。
components.html(
    render_slide_html(current),
    height=CANVAS_H + 20,
    scrolling=False,
)

# ページ移動用のドット（クリックでジャンプ）
dot_cols = st.columns(n)
for i, c in enumerate(dot_cols):
    with c:
        label = "●" if i == idx else "○"
        if st.button(label, key=f"dot_{i}", use_container_width=True):
            st.session_state.slide_idx = i
            st.rerun()
