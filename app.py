# -*- coding: utf-8 -*-
"""
流動球體風格 Streamlit 簡報
"""

import streamlit as st
import streamlit.components.v1 as components


# ============================================================
# Streamlit 基本設定
# ============================================================

st.set_page_config(
    page_title="データ基盤構築の考え方と業務自動化",
    page_icon="🟣",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# 投影片內容
# ============================================================

SLIDES = [
    {
        "type": "title",
        "title_lines": [
            "データ基盤構築の考え方と",
            "業務自動化",
        ],
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


# ============================================================
# 共用 CSS
# ============================================================

BASE_CSS = f"""
* {{
    box-sizing: border-box;
}}

html,
body {{
    margin: 0;
    padding: 0;
    background: transparent;
    overflow: hidden;
}}

.viewport {{
    position: relative;
    width: 100%;
    height: {CANVAS_H}px;
    overflow: hidden;
}}

.stage {{
    position: absolute;
    top: 0;
    left: 50%;
    width: {CANVAS_W}px;
    height: {CANVAS_H}px;

    transform-origin: top center;
    transform: translateX(-50%);

    overflow: hidden;
    border-radius: 28px;

    background:
        radial-gradient(
            circle at 88% 12%,
            rgba(221, 205, 255, 0.32) 0%,
            transparent 30%
        ),
        linear-gradient(
            145deg,
            #fcfaff 0%,
            #f7f2fd 52%,
            #f1e8fc 100%
        );

    box-shadow:
        0 18px 55px rgba(54, 28, 100, 0.16);

    font-family:
        "Noto Sans JP",
        "Hiragino Kaku Gothic ProN",
        "Yu Gothic",
        "Microsoft JhengHei",
        "Helvetica Neue",
        Arial,
        sans-serif;
}}


/* ------------------------------------------------------------
   球體共用樣式
------------------------------------------------------------ */

.circle,
.ball-a,
.ball-b {{
    position: absolute;
    display: block;
    border-radius: 50%;
    overflow: hidden;

    will-change: transform, opacity;
    animation-fill-mode: forwards;
    animation-timing-function: cubic-bezier(.22, .9, .32, 1);
}}


/* 主球 */

.ball-a {{
    z-index: 1;

    background:
        radial-gradient(
            circle at 29% 24%,
            rgba(255, 255, 255, 0.92) 0%,
            rgba(224, 209, 255, 0.88) 13%,
            rgba(183, 148, 247, 0.95) 36%,
            rgba(139, 92, 246, 0.98) 67%,
            rgba(94, 45, 190, 1) 100%
        );

    box-shadow:
        inset -40px -46px 70px rgba(54, 17, 130, 0.34),
        inset 26px 24px 48px rgba(255, 255, 255, 0.30),
        0 32px 65px rgba(109, 40, 217, 0.25);

    animation-name: ballInA;
    animation-duration: 1.20s;
}}


/* 副球 */

.ball-b {{
    z-index: 2;

    background:
        radial-gradient(
            circle at 30% 25%,
            rgba(255, 255, 255, 0.96) 0%,
            rgba(235, 225, 255, 0.92) 16%,
            rgba(200, 174, 250, 0.90) 42%,
            rgba(166, 122, 239, 0.92) 72%,
            rgba(121, 75, 211, 0.96) 100%
        );

    box-shadow:
        inset -28px -34px 54px rgba(71, 31, 150, 0.24),
        inset 20px 18px 38px rgba(255, 255, 255, 0.36),
        0 24px 48px rgba(109, 40, 217, 0.20);

    animation-name: ballInB;
    animation-duration: 1.32s;
    animation-delay: 0.08s;
}}


/* 球體表面的光點 */

.ball-a::after,
.ball-b::after {{
    content: "";
    position: absolute;

    top: 12%;
    left: 17%;

    width: 27%;
    height: 18%;

    border-radius: 50%;

    background:
        radial-gradient(
            ellipse,
            rgba(255, 255, 255, 0.66) 0%,
            rgba(255, 255, 255, 0.18) 45%,
            transparent 72%
        );

    transform: rotate(-25deg);
    filter: blur(2px);
}}


/* ------------------------------------------------------------
   球體移動
------------------------------------------------------------ */

@keyframes ballInA {{
    0% {{
        transform:
            translate(var(--dxA), var(--dyA))
            scale(0.30)
            rotate(-14deg);

        opacity: 0;
    }}

    58% {{
        opacity: 0.95;
    }}

    74% {{
        transform:
            translate(-18px, 10px)
            scale(1.07)
            rotate(3deg);

        opacity: 0.95;
    }}

    88% {{
        transform:
            translate(7px, -4px)
            scale(0.98)
            rotate(-1deg);
    }}

    100% {{
        transform:
            translate(0, 0)
            scale(1)
            rotate(0);

        opacity: 0.95;
    }}
}}


@keyframes ballInB {{
    0% {{
        transform:
            translate(var(--dxB), var(--dyB))
            scale(0.24)
            rotate(18deg);

        opacity: 0;
    }}

    58% {{
        opacity: 0.72;
    }}

    72% {{
        transform:
            translate(15px, -9px)
            scale(1.09)
            rotate(-4deg);

        opacity: 0.72;
    }}

    88% {{
        transform:
            translate(-5px, 4px)
            scale(0.97)
            rotate(1deg);
    }}

    100% {{
        transform:
            translate(0, 0)
            scale(1)
            rotate(0);

        opacity: 0.72;
    }}
}}


/* ------------------------------------------------------------
   文字動畫：等球體移動後再出現
------------------------------------------------------------ */

.textup {{
    opacity: 0;
    transform: translateY(24px);

    animation-name: textIn;
    animation-duration: 0.68s;
    animation-timing-function: cubic-bezier(.22, .9, .32, 1);
    animation-fill-mode: forwards;
}}

@keyframes textIn {{
    0% {{
        opacity: 0;
        transform: translateY(24px);
        filter: blur(4px);
    }}

    100% {{
        opacity: 1;
        transform: translateY(0);
        filter: blur(0);
    }}
}}


.pagefoot {{
    position: absolute;
    right: 34px;
    bottom: 22px;

    z-index: 5;

    color: #9c87d9;
    font-size: 12px;
    letter-spacing: 0.08em;

    opacity: 0;

    animation: textIn 0.55s ease 1.85s forwards;
}}


/* ------------------------------------------------------------
   窄螢幕自動縮放
------------------------------------------------------------ */

@media (max-width: 1160px) {{
    .stage {{
        left: 0;
        transform: scale(calc(100vw / {CANVAS_W}));
        transform-origin: top left;
    }}

    .viewport {{
        height: calc({CANVAS_H}px * (100vw / {CANVAS_W}));
    }}
}}


/* 使用者關閉動畫時 */

@media (prefers-reduced-motion: reduce) {{
    .circle,
    .ball-a,
    .ball-b,
    .textup,
    .pagefoot {{
        animation: none !important;
        opacity: 1 !important;
        transform: none !important;
        filter: none !important;
    }}
}}
"""


# ============================================================
# HTML 輔助函式
# ============================================================

def points_html(points, delay_base=1.72, step=0.13):
    result = []

    for index, point in enumerate(points):
        delay = delay_base + index * step

        result.append(
            f"""
            <li
                class="textup"
                style="animation-delay:{delay:.2f}s"
            >
                {point}
            </li>
            """
        )

    return "\n".join(result)


# ============================================================
# 首頁
# ============================================================

def render_title(slide):
    lines_html = "".join(
        f"<div>{line}</div>"
        for line in slide["title_lines"]
    )

    return f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <style>
            {BASE_CSS}

            .title-small-orb {{
                position: absolute;
                top: -80px;
                left: -75px;

                width: 235px;
                height: 235px;

                z-index: 0;
                border-radius: 50%;

                background:
                    radial-gradient(
                        circle at 62% 64%,
                        #d4bdfa 0%,
                        #eee5fc 63%,
                        rgba(255,255,255,0) 72%
                    );

                opacity: 0.78;
            }}

            .title-line {{
                position: absolute;
                top: 90px;
                right: 74px;

                width: 2px;
                height: 410px;

                z-index: 4;

                background:
                    linear-gradient(
                        to bottom,
                        #8b5cf6,
                        rgba(200, 179, 245, 0.30)
                    );
            }}

            .title-line-dot {{
                position: absolute;
                top: 81px;
                right: 66px;

                width: 18px;
                height: 18px;

                z-index: 5;
                border-radius: 50%;

                background: #8b5cf6;

                box-shadow:
                    0 0 0 7px rgba(139, 92, 246, 0.13);
            }}

            .title-copy {{
                position: absolute;
                top: 218px;
                left: 76px;

                z-index: 5;

                color: #6425d0;
                font-size: 45px;
                font-weight: 850;
                line-height: 1.26;
                letter-spacing: 0.01em;
            }}

            .title-meta {{
                position: absolute;
                top: 407px;
                left: 78px;

                z-index: 5;

                color: #7257b6;
                font-size: 15px;
                line-height: 1.7;
            }}

            .title-meta-row {{
                display: flex;
                align-items: center;
                gap: 14px;
            }}

            .meta-ball {{
                width: 38px;
                height: 38px;
                flex: 0 0 auto;

                border-radius: 50%;

                background:
                    radial-gradient(
                        circle at 30% 25%,
                        #ffffff 0%,
                        #d9c8fb 35%,
                        #a57ce9 100%
                    );

                box-shadow:
                    inset -7px -8px 14px rgba(77, 31, 155, 0.18),
                    0 8px 18px rgba(109, 40, 217, 0.17);
            }}

            .title-date {{
                margin-top: 7px;
                margin-left: 52px;
            }}
        </style>
    </head>

    <body>
        <div class="viewport">
            <div class="stage">

                <div class="title-small-orb"></div>

                <div
                    class="circle ball-a"
                    style="
                        width:460px;
                        height:460px;
                        right:-112px;
                        bottom:-158px;
                        --dxA:360px;
                        --dyA:130px;
                    "
                ></div>

                <div
                    class="circle ball-b"
                    style="
                        width:285px;
                        height:285px;
                        right:235px;
                        bottom:-24px;
                        --dxB:-320px;
                        --dyB:190px;
                    "
                ></div>

                <div class="title-line"></div>
                <div class="title-line-dot"></div>

                <div
                    class="title-copy textup"
                    style="animation-delay:1.42s"
                >
                    {lines_html}
                </div>

                <div
                    class="title-meta textup"
                    style="animation-delay:1.72s"
                >
                    <div class="title-meta-row">
                        <span class="meta-ball"></span>
                        <span>{slide["reporter"]}</span>
                    </div>

                    <div class="title-date">
                        {slide["date"]}
                    </div>
                </div>

            </div>
        </div>
    </body>
    </html>
    """


# ============================================================
# 目錄頁
# ============================================================

def render_toc(slide):
    rows = []

    for index, item in enumerate(slide["items"], start=1):
        delay = 1.54 + (index - 1) * 0.12

        rows.append(
            f"""
            <div
                class="toc-row textup"
                style="animation-delay:{delay:.2f}s"
            >
                <span class="toc-num">{index:02d}</span>
                <span class="toc-text">{item}</span>
            </div>
            """
        )

    rows_html = "\n".join(rows)

    return f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">

        <style>
            {BASE_CSS}

            .toc-corner-ball {{
                position: absolute;
                top: 28px;
                right: 72px;

                width: 70px;
                height: 70px;

                z-index: 4;
                border-radius: 50%;

                background:
                    radial-gradient(
                        circle at 30% 25%,
                        #ffffff 0%,
                        #ded0fb 35%,
                        #aa82ed 100%
                    );

                box-shadow:
                    inset -10px -12px 20px rgba(75, 28, 160, 0.18),
                    0 12px 24px rgba(109, 40, 217, 0.17);
            }}

            .toc-heading {{
                position: absolute;
                top: 284px;
                left: 106px;

                z-index: 6;

                color: #6425d0;
                font-size: 38px;
                font-weight: 850;
                letter-spacing: -0.02em;
            }}

            .toc-subheading {{
                position: absolute;
                top: 340px;
                left: 109px;

                z-index: 6;

                color: rgba(84, 57, 145, 0.70);
                font-size: 14px;
                letter-spacing: 0.14em;
            }}

            .toc-panel {{
                position: absolute;
                top: 157px;
                left: 535px;

                width: 505px;
                z-index: 6;
            }}

            .toc-row {{
                display: flex;
                align-items: baseline;
                gap: 20px;

                min-height: 64px;
                padding: 17px 0 13px;

                border-bottom:
                    1px solid rgba(140, 100, 220, 0.16);
            }}

            .toc-num {{
                width: 34px;

                color: #9465ed;
                font-size: 15px;
                font-weight: 800;
            }}

            .toc-text {{
                color: #4b3885;
                font-size: 20px;
                font-weight: 680;
                letter-spacing: 0.01em;
            }}
        </style>
    </head>

    <body>
        <div class="viewport">
            <div class="stage">

                <div class="toc-corner-ball"></div>

                <div
                    class="circle ball-a"
                    style="
                        width:420px;
                        height:420px;
                        left:-178px;
                        top:118px;
                        --dxA:-390px;
                        --dyA:-110px;
                    "
                ></div>

                <div
                    class="circle ball-b"
                    style="
                        width:265px;
                        height:265px;
                        left:96px;
                        top:350px;
                        --dxB:-260px;
                        --dyB:220px;
                    "
                ></div>

                <div
                    class="toc-heading textup"
                    style="animation-delay:1.38s"
                >
                    {slide["heading"]}
                </div>

                <div
                    class="toc-subheading textup"
                    style="animation-delay:1.52s"
                >
                    {slide.get("subtitle", "")}
                </div>

                <div class="toc-panel">
                    {rows_html}
                </div>

            </div>
        </div>
    </body>
    </html>
    """


# ============================================================
# 章節內容頁
# ============================================================

def render_section(slide):
    list_html = points_html(
        slide["points"],
        delay_base=1.72,
        step=0.13,
    )

    return f"""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">

        <style>
            {BASE_CSS}

            .section-corner-ball {{
                position: absolute;
                top: 25px;
                right: 66px;

                width: 62px;
                height: 62px;

                z-index: 5;
                border-radius: 50%;

                background:
                    radial-gradient(
                        circle at 30% 25%,
                        #ffffff 0%,
                        #dfd2fb 36%,
                        #a982eb 100%
                    );

                box-shadow:
                    inset -9px -11px 18px rgba(75, 28, 160, 0.18),
                    0 11px 22px rgba(109, 40, 217, 0.17);
            }}

            .section-bottom-ball {{
                position: absolute;
                right: 152px;
                bottom: 34px;

                width: 34px;
                height: 34px;

                z-index: 5;
                border-radius: 50%;

                background:
                    radial-gradient(
                        circle at 30% 25%,
                        #ffffff 0%,
                        #d7c6f8 38%,
                        #986be2 100%
                    );

                box-shadow:
                    0 8px 18px rgba(109, 40, 217, 0.17);
            }}

            .section-number {{
                position: absolute;
                top: 250px;
                left: 113px;

                z-index: 7;

                color: #ffffff;
                font-size: 29px;
                font-weight: 850;
                letter-spacing: 0.09em;

                text-shadow:
                    0 2px 12px rgba(60, 20, 130, 0.24);
            }}

            .section-label {{
                position: absolute;
                top: 294px;
                left: 115px;

                z-index: 7;

                color: rgba(255, 255, 255, 0.84);
                font-size: 13px;
                font-weight: 600;
                letter-spacing: 0.17em;
            }}

            .section-title {{
                position: absolute;
                top: 230px;
                left: 548px;

                width: 520px;
                z-index: 7;

                color: #56369e;
                font-size: 35px;
                font-weight: 850;
                line-height: 1.35;
                letter-spacing: 0.01em;
            }}

            .title-underline {{
                position: absolute;
                top: 302px;
                left: 550px;

                width: 72px;
                height: 4px;

                z-index: 7;
                border-radius: 10px;

                background:
                    linear-gradient(
                        90deg,
                        #8b5cf6,
                        #c8aef4
                    );

                opacity: 0;

                animation:
                    lineGrow 0.65s
                    cubic-bezier(.22, .9, .32, 1)
                    1.62s forwards;
            }}

            @keyframes lineGrow {{
                from {{
                    width: 0;
                    opacity: 0;
                }}

                to {{
                    width: 72px;
                    opacity: 1;
                }}
            }}

            .section-points {{
                position: absolute;
                top: 335px;
                left: 550px;

                width: 530px;
                z-index: 7;

                margin: 0;
                padding: 0;

                list-style: none;
            }}

            .section-points li {{
                position: relative;

                margin-bottom: 13px;
                padding-left: 20px;

                color: #5b4a88;
                font-size: 16px;
                line-height: 1.65;
            }}

            .section-points li::before {{
                content: "";

                position: absolute;
                top: 10px;
                left: 0;

                width: 7px;
                height: 7px;

                border-radius: 50%;

                background: #9765eb;

                box-shadow:
                    0 0 0 5px rgba(151, 101, 235, 0.11);
            }}
        </style>
    </head>

    <body>
        <div class="viewport">
            <div class="stage">

                <div class="section-corner-ball"></div>
                <div class="section-bottom-ball"></div>

                <div
                    class="circle ball-a"
                    style="
                        width:440px;
                        height:440px;
                        left:-200px;
                        top:102px;
                        --dxA:-400px;
                        --dyA:-100px;
                    "
                ></div>

                <div
                    class="circle ball-b"
                    style="
                        width:270px;
                        height:270px;
                        left:82px;
                        top:345px;
                        --dxB:-270px;
                        --dyB:220px;
                    "
                ></div>

                <div
                    class="section-number textup"
                    style="animation-delay:1.35s"
                >
                    {slide["num"]}
                </div>

                <div
                    class="section-label textup"
                    style="animation-delay:1.48s"
                >
                    SECTION
                </div>

                <div
                    class="section-title textup"
                    style="animation-delay:1.48s"
                >
                    {slide["title"]}
                </div>

                <div class="title-underline"></div>

                <ul class="section-points">
                    {list_html}
                </ul>

            </div>
        </div>
    </body>
    </html>
    """


# ============================================================
# 選擇 renderer
# ============================================================

RENDERERS = {
    "title": render_title,
    "toc": render_toc,
    "section": render_section,
}


def render_slide_html(slide):
    renderer = RENDERERS.get(slide["type"])

    if renderer is None:
        return "<h1>Unsupported slide type</h1>"

    return renderer(slide)


# ============================================================
# Streamlit 外層樣式
# ============================================================

st.markdown(
    """
    <style>
        html,
        body,
        [data-testid="stAppViewContainer"] {
            background:
                linear-gradient(
                    145deg,
                    #0d1017 0%,
                    #131420 100%
                );
        }

        [data-testid="stHeader"] {
            background: transparent;
        }

        [data-testid="stToolbar"] {
            display: none;
        }

        .block-container {
            max-width: 1220px;
            padding-top: 1.2rem;
            padding-bottom: 1.2rem;
        }

        div[data-testid="stHorizontalBlock"] {
            align-items: center;
        }

        div[data-testid="stButton"] button {
            min-height: 42px;

            color: #eee7ff;
            font-weight: 650;

            border:
                1px solid rgba(180, 145, 245, 0.28);
            border-radius: 14px;

            background:
                rgba(117, 75, 190, 0.16);

            transition:
                transform 160ms ease,
                border-color 160ms ease,
                background 160ms ease;
        }

        div[data-testid="stButton"] button:hover {
            border-color:
                rgba(190, 155, 255, 0.65);

            background:
                rgba(137, 92, 220, 0.28);

            transform: translateY(-1px);
        }

        div[data-testid="stButton"] button:disabled {
            opacity: 0.28;
        }

        iframe {
            border-radius: 28px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# 投影片狀態
# ============================================================

if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0


slide_count = len(SLIDES)
current_index = st.session_state.slide_idx


# ============================================================
# 上方控制列
# ============================================================

previous_column, counter_column, next_column = st.columns(
    [1.25, 5.5, 1.25]
)


with previous_column:
    previous_clicked = st.button(
        "◀ 前へ",
        use_container_width=True,
        disabled=current_index == 0,
    )

    if previous_clicked:
        st.session_state.slide_idx = max(
            0,
            current_index - 1,
        )
        st.rerun()


with counter_column:
    st.markdown(
        f"""
        <div style="
            text-align:center;
            color:#b69af0;
            font-size:14px;
            font-weight:700;
            letter-spacing:.16em;
        ">
            {current_index + 1:02d} / {slide_count:02d}
        </div>
        """,
        unsafe_allow_html=True,
    )


with next_column:
    next_clicked = st.button(
        "次へ ▶",
        use_container_width=True,
        disabled=current_index == slide_count - 1,
    )

    if next_clicked:
        st.session_state.slide_idx = min(
            slide_count - 1,
            current_index + 1,
        )
        st.rerun()


# ============================================================
# 顯示投影片
# ============================================================

current_slide = SLIDES[current_index]

components.html(
    render_slide_html(current_slide),
    height=CANVAS_H + 12,
    scrolling=False,
)


# ============================================================
# 下方頁碼按鈕
# ============================================================

dot_columns = st.columns(slide_count)

for index, column in enumerate(dot_columns):
    with column:
        if index == current_index:
            label = f"● {index + 1:02d}"
        else:
            label = f"○ {index + 1:02d}"

        dot_clicked = st.button(
            label,
            key=f"slide_dot_{index}",
            use_container_width=True,
        )

        if dot_clicked:
            st.session_state.slide_idx = index
            st.rerun()
