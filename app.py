# -*- coding: utf-8 -*-
"""Single-stage animated Streamlit presentation."""

import base64
import json
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


def image_source(filename):
    """Embed repository images so the Streamlit iframe never hits CORS issues."""
    path = Path(__file__).resolve().parent / filename
    if path.exists():
        encoded = base64.b64encode(path.read_bytes()).decode("ascii")
        return f"data:image/png;base64,{encoded}"
    safe_name = filename.replace(" ", "%20")
    return f"https://raw.githubusercontent.com/s942509/Data-base-project/main/{safe_name}"


st.set_page_config(
    page_title="データ基盤構築の考え方と業務自動化",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed",
)


SLIDES = [
    {
        "type": "title",
        "eyebrow": "DATA PLATFORM / AUTOMATION",
        "title": "データ基盤構築の考え方と<br>業務自動化",
        "reporter": "Reporter: 佳蓁（カシン）",
        "date": "2026/08/24",
        "ball1": {"x": 74, "y": 73, "size": 45},
        "ball2": {"x": 48, "y": 82, "size": 27},
    },
    {
        "type": "toc",
        "eyebrow": "TODAY'S FLOW",
        "title": "Contents",
        "items": [
            "経歴と提案の背景",
            "自動化の実例と成果",
            "現在の三つの課題",
            "改善の全体設計",
            "導入方法と期待効果",
            "今後の進め方",
        ],
        "ball1": {"x": -8, "y": 48, "size": 38},
        "ball2": {"x": 18, "y": 74, "size": 23},
    },
    {
        "type": "experience",
        "num": "01",
        "title": "医療ビッグデータ基盤構築の経験",
        "images": [
            {
                "id": "project",
                "url": image_source("project.png"),
                "alt": "健康大數據永續平台計畫成果報告",
            },
            {
                "id": "four",
                "url": image_source("4.png"),
                "alt": "医療画像とデータ処理の実例",
            },
            {
                "id": "center",
                "url": image_source("pc center.png"),
                "alt": "国家高速網路與計算中心",
            },
        ],
        "ball1": {"x": -16, "y": 86, "size": 26},
        "ball2": {"x": 96, "y": 8, "size": 14},
    },
    {
        "type": "pipeline",
        "num": "02",
        "title": "商材別に抽出・集計",
        "source_label": "データソース",
        "sources": ["Cros 受注一", "Cros 受注二"],
        "products": ["コラーゲン", "プラセンタ", "ナイトコラーゲン", "QQ", "もっちり", "⋮", "CRM売上"],
        "note": "Taboola売上<br>CC数を補完",
        "result_label": "各商材の日報へ自動入力",
        "image": image_source("slide4.png"),
        "ball1": {"x": 108, "y": 108, "size": 22},
        "ball2": {"x": -6, "y": -8, "size": 13},
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
        "ball1": {"x": -12, "y": 50, "size": 39},
        "ball2": {"x": 21, "y": 9, "size": 18},
    },
    {
        "type": "section",
        "num": "04",
        "title": "改善の全体設計",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
        "ball1": {"x": 69, "y": 65, "size": 42},
        "ball2": {"x": 55, "y": 50, "size": 20},
    },
    {
        "type": "section",
        "num": "05",
        "title": "導入方法と期待効果",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
        "ball1": {"x": -9, "y": -16, "size": 38},
        "ball2": {"x": 17, "y": 18, "size": 20},
    },
    {
        "type": "section",
        "num": "06",
        "title": "今後の進め方",
        "points": [
            "（ここに内容を記載）",
            "（ここに内容を記載）",
        ],
        "ball1": {"x": 70, "y": 62, "size": 43},
        "ball2": {"x": 50, "y": 76, "size": 21},
    },
]


slides_json = json.dumps(SLIDES, ensure_ascii=False)


HTML = r"""
<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<style>
  :root {
    --ink: #4b3586;
    --purple: #7135de;
    --soft-purple: #a982ee;
    --line: rgba(108, 70, 181, .16);
  }

  * { box-sizing: border-box; }
  html, body { margin: 0; background: transparent; overflow: hidden; }
  button { font: inherit; }

  .shell {
    width: 100%;
    padding: 6px 8px 0;
    font-family: "Noto Sans JP", "Yu Gothic", "Microsoft JhengHei", Arial, sans-serif;
  }

  .stage {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    isolation: isolate;
    border-radius: clamp(16px, 2vw, 30px);
    background:
      radial-gradient(circle at 85% 10%, rgba(225,211,252,.38), transparent 29%),
      linear-gradient(145deg, #fcfaff 0%, #f7f2fd 54%, #f0e7fb 100%);
    box-shadow: 0 24px 70px rgba(30, 13, 61, .28);
    cursor: pointer;
    user-select: none;
    outline: none;
  }

  .stage::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    pointer-events: none;
    background: linear-gradient(115deg, rgba(255,255,255,.28), transparent 48%);
  }

  .orb {
    position: absolute;
    z-index: 1;
    width: calc(var(--size) * 1%);
    aspect-ratio: 1;
    left: calc(var(--x) * 1%);
    top: calc(var(--y) * 1%);
    border-radius: 50%;
    transform: translate(-50%, -50%);
    transition:
      left 900ms cubic-bezier(.65,0,.25,1),
      top 900ms cubic-bezier(.65,0,.25,1),
      width 900ms cubic-bezier(.65,0,.25,1),
      opacity 360ms ease;
    will-change: left, top, width;
  }

  .orb-a {
    opacity: .92;
    background: radial-gradient(circle at 29% 24%,
      #fff 0%, #e6d8ff 11%, #c3a1f7 32%, #9560ed 64%, #6427c9 100%);
    box-shadow:
      inset -3.2vw -3.4vw 5.5vw rgba(52,14,127,.27),
      inset 2vw 1.7vw 4vw rgba(255,255,255,.28),
      0 2.1vw 4.7vw rgba(92,39,188,.22);
  }

  .orb-b {
    z-index: 2;
    opacity: .68;
    background: radial-gradient(circle at 30% 24%,
      #fff 0%, #eee6ff 14%, #d1bafa 39%, #ad82ed 70%, #8350d5 100%);
    box-shadow:
      inset -2vw -2.2vw 4vw rgba(55,17,130,.20),
      inset 1.5vw 1.2vw 3vw rgba(255,255,255,.34),
      0 1.5vw 3.4vw rgba(92,39,188,.18);
  }

  .orb::after {
    content: "";
    position: absolute;
    left: 17%; top: 12%; width: 28%; height: 18%;
    border-radius: 50%;
    transform: rotate(-25deg);
    filter: blur(2px);
    background: radial-gradient(ellipse, rgba(255,255,255,.75), transparent 70%);
  }

  .content {
    position: absolute;
    inset: 0;
    z-index: 5;
    pointer-events: none;
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
    transition: opacity 280ms ease, transform 380ms ease, filter 380ms ease;
  }

  .content.out {
    opacity: 0;
    transform: translateY(-12px);
    filter: blur(5px);
  }

  .content.in {
    animation: contentIn 650ms cubic-bezier(.22,.9,.32,1) both;
  }

  @keyframes contentIn {
    from { opacity: 0; transform: translateY(20px); filter: blur(5px); }
    to   { opacity: 1; transform: translateY(0); filter: blur(0); }
  }

  .eyebrow {
    color: #9370df;
    font-size: clamp(9px, 1vw, 14px);
    font-weight: 800;
    letter-spacing: .22em;
    margin-bottom: 1.2vw;
  }

  .title-layout {
    position: absolute;
    left: 7%; top: 32%;
    width: 61%;
  }

  .main-title {
    margin: 0;
    color: #6625d1;
    font-size: clamp(24px, 4vw, 55px);
    font-weight: 900;
    line-height: 1.22;
    letter-spacing: .01em;
  }

  .meta {
    display: flex;
    gap: 2.2vw;
    margin-top: 3vw;
    color: #765bb8;
    font-size: clamp(10px, 1.2vw, 16px);
  }

  .toc-layout {
    position: absolute;
    inset: 0;
    display: grid;
    grid-template-columns: 40% 60%;
    align-items: center;
  }

  .toc-heading { padding-left: 10%; }
  .toc-heading h1 {
    margin: 0;
    color: #6929d4;
    font-size: clamp(27px, 4vw, 52px);
  }

  .toc-list { width: 84%; }
  .toc-row {
    display: grid;
    grid-template-columns: 48px 1fr;
    align-items: baseline;
    gap: 10px;
    padding: clamp(7px, 1vw, 14px) 0;
    border-bottom: 1px solid var(--line);
  }
  .toc-num { color: #9669eb; font-weight: 800; font-size: clamp(10px, 1.1vw, 15px); }
  .toc-text { color: var(--ink); font-weight: 750; font-size: clamp(13px, 1.65vw, 22px); }

  .section-layout {
    position: absolute;
    inset: 0;
    display: grid;
    grid-template-columns: 39% 61%;
    align-items: center;
  }
  .section-mark { padding-left: 12%; color: white; text-shadow: 0 2px 14px rgba(60,20,130,.28); }
  .section-num { font-size: clamp(28px, 4.4vw, 61px); font-weight: 900; letter-spacing: .08em; }
  .section-label { font-size: clamp(9px, 1vw, 14px); font-weight: 700; letter-spacing: .2em; }
  .section-copy { width: 86%; padding-right: 4%; }
  .section-copy h1 {
    margin: 0 0 1.2vw;
    color: #56349e;
    font-size: clamp(23px, 3.2vw, 44px);
    line-height: 1.25;
  }
  .rule { width: 74px; height: 4px; border-radius: 8px; background: linear-gradient(90deg,#8b5cf6,#ccb3f6); margin-bottom: 1.8vw; }
  .points { margin: 0; padding: 0; list-style: none; }
  .points li {
    position: relative;
    margin: 0 0 clamp(7px, 1vw, 14px);
    padding-left: 20px;
    color: #5c4a89;
    font-size: clamp(11px, 1.35vw, 18px);
    line-height: 1.55;
  }
  .points li::before {
    content: "";
    position: absolute;
    left: 0; top: .65em;
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #9765eb;
    box-shadow: 0 0 0 5px rgba(151,101,235,.11);
  }

  /* Fourth page: data pipeline */
  .pipeline-layout {
    position: absolute;
    inset: 0;
    color: #493343;
  }
  .pipeline-title {
    position: absolute;
    left: 5.3%;
    top: 5.8%;
    margin: 0;
    color: #402b3b;
    font-size: clamp(22px, 2.85vw, 39px);
    font-weight: 900;
    letter-spacing: .015em;
  }
  .pipeline-flow {
    position: absolute;
    inset: 0;
  }
  .pipeline-source {
    position: absolute;
    left: 4.9%;
    top: 18.8%;
    width: 12%;
    height: 29%;
  }
  .pipeline-label {
    display: inline-flex;
    align-items: center;
    width: 89%;
    min-height: 35px;
    padding: 7px 13px;
    color: white;
    background: linear-gradient(135deg, #a66f9b, #8f5a85);
    font-size: clamp(11px, 1.25vw, 17px);
    font-weight: 850;
    letter-spacing: .04em;
    white-space: nowrap;
  }
  .source-stack {
    position: relative;
    display: grid;
    gap: 22%;
    margin-top: 45%;
  }
  .source-stack::after {
    content: "";
    position: absolute;
    z-index: -1;
    left: 49%;
    top: 38%;
    width: 2px;
    height: 35%;
    background: #a36890;
  }
  .source-box {
    padding: 9px 12px;
    border: 1.5px solid #9b6ff0;
    background: linear-gradient(135deg, rgba(241,232,255,.88), rgba(213,191,249,.82));
    color: #49343d;
    font-size: clamp(10px, 1.05vw, 15px);
    white-space: nowrap;
  }
  .flow-arrow {
    position: absolute;
    width: 5%;
    height: 20px;
    background: linear-gradient(90deg, #7c3aed, #a56ce5);
    filter: drop-shadow(0 2px 2px rgba(85,28,57,.15));
  }
  .flow-arrow::after {
    content: "";
    position: absolute;
    top: 50%;
    right: -18px;
    transform: translateY(-50%);
    border-top: 20px solid transparent;
    border-bottom: 20px solid transparent;
    border-left: 20px solid #a56ce5;
  }
  .arrow-one { left: 22.4%; top: 34.5%; }
  .arrow-two { left: 66.5%; top: 36%; background: linear-gradient(90deg, #8b5cf6, #ae7ce9); }
  .arrow-two::after { border-left-color: #ae7ce9; }
  .pipeline-products {
    position: absolute;
    left: 35%;
    top: 18.4%;
    width: 17.3%;
    height: 41.2%;
    padding: 3% 8% 5%;
    border: 2px solid #8b5cf6;
    background: rgba(255,255,255,.24);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }
  .product-item {
    color: #49343e;
    font-size: clamp(10px, 1.12vw, 16px);
    line-height: 1.15;
    white-space: nowrap;
    word-break: keep-all;
  }
  .pipeline-note {
    position: absolute;
    left: 54.6%;
    top: 35.2%;
    width: 10%;
    color: #573b4b;
    font-size: clamp(10px, 1.05vw, 15px);
    line-height: 1.45;
  }
  .pipeline-note::before,
  .pipeline-note::after {
    content: "";
    position: absolute;
    right: 105%;
    width: 65%;
    height: 2px;
    transform-origin: right center;
    background: #9f648a;
  }
  .pipeline-note::before { top: 38%; transform: rotate(-23deg); }
  .pipeline-note::after { top: 60%; transform: rotate(-8deg); }
  .pipeline-result {
    position: absolute;
    left: 75.8%;
    top: 17.1%;
    width: 19.1%;
    height: 35%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 0;
  }
  .result-label {
    width: 100%;
    padding: 8px 10px;
    color: white;
    background: linear-gradient(135deg, #9f658d, #885176);
    text-align: center;
    font-size: clamp(10px, 1.15vw, 16px);
    font-weight: 850;
    white-space: nowrap;
  }
  .result-image {
    display: block;
    width: 100%;
    height: 75%;
    margin-top: 7%;
    object-fit: contain;
    filter: drop-shadow(10px 14px 11px rgba(46,29,48,.25));
  }
  .pipeline-curves {
    position: absolute;
    inset: 0;
    z-index: 2;
    width: 100%;
    height: 100%;
    overflow: visible;
    pointer-events: none;
  }
  .pipeline-curve {
    fill: none;
    stroke: #8f62c8;
    stroke-width: 2.1;
    vector-effect: non-scaling-stroke;
    stroke-linecap: round;
    stroke-linejoin: round;
  }
  .etl-label {
    position: absolute;
    left: 10.5%;
    top: 70.5%;
    color: #563b4d;
    font-size: clamp(11px, 1.25vw, 17px);
    letter-spacing: .04em;
  }
  .pipeline-name {
    position: absolute;
    left: 50%;
    top: 89.2%;
    transform: translateX(-50%);
    color: #3e2939;
    font-size: clamp(14px, 1.8vw, 25px);
    font-weight: 900;
    letter-spacing: .025em;
  }

  /* Third page: layered experience images */
  .experience-layout {
    position: absolute;
    inset: 0;
  }
  .experience-title {
    position: absolute;
    z-index: 9;
    left: 5.8%;
    top: 7.5%;
    margin: 0;
    color: #412b3b;
    font-size: clamp(22px, 3.15vw, 43px);
    font-weight: 900;
    letter-spacing: .01em;
  }
  .experience-title::after {
    content: "";
    display: block;
    width: 72px;
    height: 4px;
    margin-top: 13px;
    border-radius: 8px;
    background: linear-gradient(90deg, #8b5cf6, #d0b9f7);
  }
  .experience-card {
    position: absolute;
    z-index: 6;
    margin: 0;
    overflow: visible;
    border: 0;
    border-radius: 0;
    background: transparent;
    box-shadow: none;
    opacity: 0;
    transform: translateY(18px) scale(.965);
    filter: blur(3px);
    transition:
      opacity 430ms ease,
      transform 560ms cubic-bezier(.22,.9,.32,1),
      filter 430ms ease;
  }
  .experience-card.shown {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0);
  }
  .experience-card img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: contain;
    background: transparent;
  }
  .experience-project {
    z-index: 5;
    top: 3.5%;
    right: 3.4%;
    width: 32%;
    height: 42%;
  }
  .experience-four {
    z-index: 6;
    left: 2.8%;
    bottom: 7%;
    width: 30%;
    height: 42%;
  }
  .experience-center {
    z-index: 8;
    left: 23%;
    top: 28%;
    width: 53%;
    height: 55%;
  }
  .experience-step {
    position: absolute;
    z-index: 11;
    left: 5.8%;
    top: 20%;
    color: #8c6ac9;
    font-size: clamp(9px, .9vw, 13px);
    font-weight: 800;
    letter-spacing: .14em;
  }

  /* Fourth reveal: liquid-glass summary */
  .experience-summary {
    z-index: 10;
    right: 3.2%;
    bottom: 7.5%;
    width: 35%;
    height: 27%;
    border: 0;
    border-radius: clamp(16px, 2vw, 28px);
    background: transparent;
    box-shadow: 0 18px 44px rgba(71, 38, 126, .20);
    isolation: isolate;
    overflow: hidden;
  }
  .experience-summary::before {
    content: "";
    position: absolute;
    inset: 0;
    z-index: 0;
    border-radius: inherit;
    border: 1px solid rgba(255, 255, 255, .72);
    background: linear-gradient(135deg,
      rgba(255,255,255,.62),
      rgba(236,224,255,.28) 52%,
      rgba(255,255,255,.48));
    box-shadow:
      inset 0 0 15px rgba(255,255,255,.78),
      inset 0 -18px 32px rgba(140,92,225,.08);
    pointer-events: none;
  }
  .experience-summary::after {
    content: "";
    position: absolute;
    inset: -7%;
    z-index: -1;
    border-radius: inherit;
    background: rgba(255,255,255,.14);
    backdrop-filter: blur(12px) saturate(135%);
    -webkit-backdrop-filter: blur(12px) saturate(135%);
    filter: url(#glass-distortion);
    pointer-events: none;
  }
  .summary-content {
    position: relative;
    z-index: 3;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: clamp(15px, 2vw, 27px);
    color: #4f377e;
  }
  .summary-kicker {
    display: flex;
    align-items: center;
    gap: 9px;
    margin-bottom: clamp(8px, 1vw, 14px);
    color: #8b5cf6;
    font-size: clamp(9px, .85vw, 12px);
    font-weight: 900;
    letter-spacing: .16em;
  }
  .summary-kicker::before {
    content: "";
    width: 25px;
    height: 3px;
    border-radius: 4px;
    background: linear-gradient(90deg, #7c3aed, #c4a4f5);
  }
  .summary-text {
    margin: 0;
    color: #49356f;
    font-size: clamp(12px, 1.45vw, 20px);
    font-weight: 780;
    line-height: 1.65;
    letter-spacing: .015em;
    text-shadow: 0 1px 0 rgba(255,255,255,.65);
  }

  .hud {
    position: absolute;
    z-index: 10;
    left: 4%; right: 4%; bottom: 3.2%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    pointer-events: none;
  }
  .progress { display: flex; gap: 7px; }
  .dot { width: 6px; height: 6px; border-radius: 50%; background: rgba(106,67,178,.20); transition: width .3s, background .3s; }
  .dot.active { width: 24px; border-radius: 8px; background: #8b5cf6; }
  .counter { color: #8f72d0; font-size: clamp(9px, .9vw, 13px); font-weight: 800; letter-spacing: .14em; }

  .next-hint {
    position: absolute;
    z-index: 12;
    right: 3.4%; top: 4.8%;
    display: flex;
    align-items: center;
    gap: 9px;
    border: 1px solid rgba(119,76,198,.18);
    border-radius: 999px;
    padding: 8px 13px;
    color: #7651be;
    background: rgba(255,255,255,.40);
    backdrop-filter: blur(8px);
    font-size: clamp(9px, .9vw, 13px);
    font-weight: 800;
    letter-spacing: .1em;
    pointer-events: none;
  }

  .ripple {
    position: absolute;
    z-index: 20;
    width: 14px; height: 14px;
    border: 2px solid rgba(116,64,211,.45);
    border-radius: 50%;
    transform: translate(-50%,-50%) scale(.2);
    animation: ripple 620ms ease-out forwards;
    pointer-events: none;
  }
  @keyframes ripple { to { opacity: 0; transform: translate(-50%,-50%) scale(8); } }

  @media (max-width: 620px) {
    .toc-row { grid-template-columns: 30px 1fr; }
    .points li { padding-left: 13px; }
    .points li::before { width: 5px; height: 5px; box-shadow: none; }
    .next-hint { padding: 5px 8px; }
  }

  @media (prefers-reduced-motion: reduce) {
    .orb, .content { transition-duration: 1ms !important; animation-duration: 1ms !important; }
  }
</style>
</head>
<body>
  <div class="shell">
    <main
      class="stage"
      id="stage"
      tabindex="0"
      role="button"
      aria-label="Animated presentation; click or press Enter for next scene"
    >
      <div class="orb orb-a" id="orbA"></div>
      <div class="orb orb-b" id="orbB"></div>
      <section class="content" id="content"></section>
      <div class="next-hint" id="nextHint">CLICK <span>→</span></div>
      <div class="hud">
        <div class="progress" id="progress"></div>
        <div class="counter" id="counter"></div>
      </div>
    </main>
  </div>

<script>
  const slides = __SLIDES__;
  const stage = document.getElementById('stage');
  const content = document.getElementById('content');
  const orbA = document.getElementById('orbA');
  const orbB = document.getElementById('orbB');
  const progress = document.getElementById('progress');
  const counter = document.getElementById('counter');
  const nextHint = document.getElementById('nextHint');

  let index = 0;
  let busy = false;
  let revealStep = 0;

  function escapeText(value) {
    return String(value)
      .replaceAll('&', '&amp;')
      .replaceAll('<', '&lt;')
      .replaceAll('>', '&gt;')
      .replaceAll('"', '&quot;')
      .replaceAll("'", '&#039;');
  }

  function setOrb(orb, data) {
    orb.style.setProperty('--x', data.x);
    orb.style.setProperty('--y', data.y);
    orb.style.setProperty('--size', data.size);
  }

  function titleMarkup(s) {
    return `
      <div class="title-layout">
        <div class="eyebrow">${escapeText(s.eyebrow)}</div>
        <h1 class="main-title">${s.title}</h1>
        <div class="meta">
          <span>${escapeText(s.reporter)}</span>
          <span>${escapeText(s.date)}</span>
        </div>
      </div>`;
  }

  function tocMarkup(s) {
    const rows = s.items.map((item, i) => `
      <div class="toc-row">
        <span class="toc-num">${String(i + 1).padStart(2, '0')}</span>
        <span class="toc-text">${escapeText(item)}</span>
      </div>`).join('');
    return `
      <div class="toc-layout">
        <div class="toc-heading">
          <div class="eyebrow">${escapeText(s.eyebrow)}</div>
          <h1>${escapeText(s.title)}</h1>
        </div>
        <div class="toc-list">${rows}</div>
      </div>`;
  }

  function sectionMarkup(s) {
    const points = s.points.map(point => `<li>${escapeText(point)}</li>`).join('');
    return `
      <div class="section-layout">
        <div class="section-mark">
          <div class="section-num">${escapeText(s.num)}</div>
          <div class="section-label">SECTION</div>
        </div>
        <div class="section-copy">
          <h1>${escapeText(s.title)}</h1>
          <div class="rule"></div>
          <ul class="points">${points}</ul>
        </div>
      </div>`;
  }

  function pipelineMarkup(s) {
    const sources = s.sources.map(source =>
      `<div class="source-box">${escapeText(source)}</div>`
    ).join('');
    const products = s.products.map(product =>
      `<div class="product-item">${escapeText(product)}</div>`
    ).join('');
    return `
      <div class="pipeline-layout">
        <h1 class="pipeline-title">${escapeText(s.title)}</h1>
        <svg class="pipeline-curves" viewBox="0 0 1000 562" preserveAspectRatio="none" aria-hidden="true">
          <path class="pipeline-curve"
            d="M88 352 L88 374 Q88 386 101 386 L435 386 Q448 386 448 374 L448 352"></path>
          <path class="pipeline-curve"
            d="M28 438 C28 468 48 477 83 477 L458 477
               C482 477 492 490 500 516
               C508 490 518 477 542 477 L917 477
               C952 477 972 468 972 438"></path>
        </svg>
        <div class="pipeline-flow">
          <div class="pipeline-source">
            <div class="pipeline-label">${escapeText(s.source_label)}</div>
            <div class="source-stack">${sources}</div>
          </div>
          <div class="flow-arrow arrow-one"></div>
          <div class="pipeline-products">${products}</div>
          <div class="pipeline-note">${s.note}</div>
          <div class="flow-arrow arrow-two"></div>
          <div class="pipeline-result">
            <div class="result-label">${escapeText(s.result_label)}</div>
            <img class="result-image" src="${s.image}" alt="商材別の日報への自動入力結果">
          </div>
        </div>
        <div class="etl-label">ETL（Extract / Transform / Load）</div>
        <div class="pipeline-name">Data Pipeline</div>
      </div>`;
  }

  function experienceMarkup(s) {
    const project = s.images.find(image => image.id === 'project');
    const four = s.images.find(image => image.id === 'four');
    const center = s.images.find(image => image.id === 'center');
    return `
      <div class="experience-layout">
        <svg width="0" height="0" aria-hidden="true" style="position:absolute">
          <defs>
            <filter id="glass-distortion" x="-20%" y="-20%" width="140%" height="140%">
              <feTurbulence type="fractalNoise" baseFrequency="0.025 0.025"
                numOctaves="2" seed="92" result="noise"></feTurbulence>
              <feGaussianBlur in="noise" stdDeviation="2" result="blurred"></feGaussianBlur>
              <feDisplacementMap in="SourceGraphic" in2="blurred" scale="42"
                xChannelSelector="R" yChannelSelector="G"></feDisplacementMap>
            </filter>
          </defs>
        </svg>
        <h1 class="experience-title">${escapeText(s.title)}</h1>
        <div class="experience-step" id="experienceStep">CLICK TO REVEAL · 0 / 4</div>
        <figure class="experience-card experience-project" data-reveal="1">
          <img src="${project.url}" alt="${escapeText(project.alt)}">
        </figure>
        <figure class="experience-card experience-four" data-reveal="2">
          <img src="${four.url}" alt="${escapeText(four.alt)}">
        </figure>
        <figure class="experience-card experience-center" data-reveal="3">
          <img src="${center.url}" alt="${escapeText(center.alt)}">
        </figure>
        <aside class="experience-card experience-summary" data-reveal="4">
          <div class="summary-content">
            <div class="summary-kicker">KEY TAKEAWAY</div>
            <p class="summary-text">画像もデータも、AI学習に活用できる<br>「品質・規格・量」を確保することがポイントです。</p>
          </div>
        </aside>
      </div>`;
  }

  function markup(s) {
    if (s.type === 'title') return titleMarkup(s);
    if (s.type === 'toc') return tocMarkup(s);
    if (s.type === 'experience') return experienceMarkup(s);
    if (s.type === 'pipeline') return pipelineMarkup(s);
    return sectionMarkup(s);
  }

  function updateExperience() {
    if (slides[index].type !== 'experience') return;
    content.querySelectorAll('[data-reveal]').forEach(card => {
      const step = Number(card.dataset.reveal);
      card.classList.toggle('shown', step <= revealStep);
    });
    const label = document.getElementById('experienceStep');
    if (label) {
      label.textContent = revealStep < 4
        ? `CLICK TO REVEAL · ${revealStep} / 4`
        : 'KEY TAKEAWAY · 4 / 4';
    }
    drawHud();
  }

  function drawHud() {
    progress.innerHTML = slides.map((_, i) =>
      `<span class="dot ${i === index ? 'active' : ''}"></span>`
    ).join('');
    counter.textContent = `${String(index + 1).padStart(2, '0')} / ${String(slides.length).padStart(2, '0')}`;
    if (slides[index].type === 'experience' && revealStep < 4) {
      nextHint.innerHTML = `REVEAL ${revealStep + 1} / 4 <span>＋</span>`;
    } else {
      nextHint.innerHTML = index === slides.length - 1 ? 'RESTART <span>↻</span>' : 'CLICK <span>→</span>';
    }
  }

  function showInitial() {
    const s = slides[index];
    setOrb(orbA, s.ball1);
    setOrb(orbB, s.ball2);
    content.innerHTML = markup(s);
    content.classList.add('in');
    drawHud();
  }

  function moveTo(nextIndex) {
    if (busy || nextIndex === index) return;
    busy = true;

    content.classList.remove('in');
    content.classList.add('out');

    const next = slides[nextIndex];
    setTimeout(() => {
      setOrb(orbA, next.ball1);
      setOrb(orbB, next.ball2);
    }, 120);

    setTimeout(() => {
      index = nextIndex;
      revealStep = 0;
      content.innerHTML = markup(slides[index]);
      content.classList.remove('out');
      void content.offsetWidth;
      content.classList.add('in');
      drawHud();
      busy = false;
    }, 1020);
  }

  function next() {
    if (busy) return;
    if (slides[index].type === 'experience' && revealStep < 4) {
      revealStep += 1;
      updateExperience();
      return;
    }
    moveTo(index === slides.length - 1 ? 0 : index + 1);
  }

  function previous() {
    if (busy) return;
    if (slides[index].type === 'experience' && revealStep > 0) {
      revealStep -= 1;
      updateExperience();
      return;
    }
    moveTo(index === 0 ? slides.length - 1 : index - 1);
  }

  stage.addEventListener('pointerdown', () => {
    stage.focus({preventScroll: true});
  });

  stage.addEventListener('click', event => {
    stage.focus({preventScroll: true});
    const rect = stage.getBoundingClientRect();
    const ripple = document.createElement('span');
    ripple.className = 'ripple';
    ripple.style.left = `${event.clientX - rect.left}px`;
    ripple.style.top = `${event.clientY - rect.top}px`;
    stage.appendChild(ripple);
    setTimeout(() => ripple.remove(), 700);
    next();
  });

  function handleKey(event) {
    if (['ArrowRight', ' ', 'Enter', 'PageDown'].includes(event.key)) {
      event.preventDefault();
      event.stopPropagation();
      next();
    }
    if (['ArrowLeft', 'PageUp'].includes(event.key)) {
      event.preventDefault();
      event.stopPropagation();
      previous();
    }
  }

  window.addEventListener('keydown', handleKey, true);
  document.addEventListener('keydown', handleKey, true);

  window.addEventListener('load', () => {
    stage.focus({preventScroll: true});
  });

  showInitial();
</script>
</body>
</html>
""".replace("__SLIDES__", slides_json)


st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(145deg, #0c0e16, #141323);
      }
      [data-testid="stHeader"], [data-testid="stToolbar"], footer { display: none; }
      .block-container {
        width: min(1220px, 96vw);
        max-width: 1220px;
        padding: 1.3rem 0 0;
      }
      iframe { display: block; border: 0; }
    </style>
    """,
    unsafe_allow_html=True,
)


components.html(
    HTML,
    height=720,
    scrolling=False,
)
