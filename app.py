from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 PRO STABLE STREAMS (с резервами)
RADIO = {
    "pop_2000s": [
        "https://ice1.somafm.com/poptron-128-mp3",
        "https://ice2.somafm.com/poptron-128-mp3"
    ],

    "indie_rock": [
        "https://ice1.somafm.com/indiepop-128-mp3",
        "https://ice2.somafm.com/indiepop-128-mp3"
    ],

    "pop_punk": [
        "https://ice1.somafm.com/punkrockers-128-mp3"
    ],

    "dance_2000s": [
        "https://ice1.somafm.com/beatblender-128-mp3",
        "https://ice2.somafm.com/beatblender-128-mp3"
    ],

    # 🎤 HIP HOP (стабильный вариант)
    "hiphop_2000s": [
        "https://ice1.somafm.com/dubstep-128-mp3"
    ],

    "rnb_2000s": [
        "https://ice1.somafm.com/smoothjazz-128-mp3"
    ],

    "chill_night": [
        "https://ice1.somafm.com/groovesalad-128-mp3"
    ],

    "uk_pop": [
        "https://stream.live.vc.bbcmedia.co.uk/bbc_radio_one"
    ]
}


@app.route("/")
def home():
    return f"""
<!DOCTYPE html>
<html>
<head>
<title>MTV 2003 PRO DESKTOP RADIO</title>

<style>

body {{
    margin: 0;
    font-family: Tahoma, Arial;

    background:
    linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');

    background-size: cover;
    background-position: center;
    height: 100vh;
    overflow: hidden;
}}

.window {{
    display: flex;
    flex-direction: column;
    height: 100vh;
}}

.topbar {{
    height: 50px;
    display: flex;
    justify-content: space-between;
    align-items: center;

    padding: 0 20px;
    background: linear-gradient(to right, #0b2a6f, #1a5cff);
    color: white;
    font-weight: bold;
}}

.main {{
    flex: 1;
    display: flex;
    padding: 20px;
    gap: 20px;
}}

.sidebar {{
    width: 280px;
    background: rgba(0,0,0,0.55);
    border-radius: 12px;
    padding: 15px;
}}

.btn {{
    background: linear-gradient(to bottom, #3daeff, #0050aa);
    border: 1px solid #7fd4ff;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 10px;
    cursor: pointer;
    font-weight: bold;
    color: white;
}}

.btn:hover {{
    transform: scale(1.03);
}}

.player {{
    flex: 1;
    background: rgba(0,0,0,0.65);
    border-radius: 14px;
    padding: 20px;
    display: flex;
    flex-direction: column;
}}

.screen {{
    background: black;
    border: 1px solid #5ac8ff;
    border-radius: 10px;
    padding: 15px;
    height: 120px;
}}

.nowplaying {{
    color: #00ffcc;
    font-size: 14px;
}}

audio {{
    width: 100%;
    margin-top: 10px;
}}

/* 💬 MSN STYLE CHAT */
.chat {{
    margin-top: 15px;
    background: rgba(10,10,25,0.95);
    border: 1px solid rgba(120,200,255,0.5);
    border-radius: 12px;
    padding: 10px;
    height: 180px;
    overflow: hidden;
    font-size: 12px;
    color: white;
}}

.msg {{
    margin: 5px 0;
    padding: 4px 8px;
    background: rgba(255,255,255,0.05);
    border-radius: 6px;
}}

.ticker {{
    position: fixed;
    bottom: 0;
    width: 100%;
    background: yellow;
    color: black;
    font-weight: bold;
    white-space: nowrap;
    overflow: hidden;
}}

.ticker span {{
    display: inline-block;
    padding-left: 100%;
    animation: ticker 22s linear infinite;
}}

@keyframes ticker {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

</style>
</head>

<body>

<div class="window">

<div class="topbar">
<div>📺 MTV RADIO 2003 PRO</div>
<div>● NYC SIGNAL STABLE</div>
</div>

<div class="main">

<div class="sidebar">

<div class="btn" onclick="play('pop_2000s')">💿 POP 2000s</div>
<div class="btn" onclick="play('indie_rock')">🎸 INDIE ROCK</div>
<div class="btn" onclick="play('pop_punk')">🔥 POP PUNK</div>
<div class="btn" onclick="play('dance_2000s')">🪩 DANCE</div>
<div class="btn" onclick="play('hiphop_2000s')">🎤 HIP HOP</div>
<div class="btn" onclick="play('rnb_2000s')">🎧 R&B</div>
<div class="btn" onclick="play('chill_night')">🌙 CHILL</div>
<div class="btn" onclick="play('uk_pop')">🇬🇧 UK HITS</div>

</div>

<div class="player">

<div class="screen">
<div class="nowplaying" id="nowplaying">NOW PLAYING: idle</div>
</div>

<audio id="audio" controls autoplay></audio>

<div class="chat" id="chat">
<div class="msg">SYSTEM: NYC radio connected 🗽</div>
<div class="msg">Ashley: this feels like 2006 😭</div>
<div class="msg">Mike: burning CD right now 💿</div>
</div>

</div>

</div>

<div class="ticker">
<span>
BREAKING: MTV revival continues • MySpace servers online • Windows XP still running • Pop punk resurgence in NYC • Limewire archive active • CD burning trend rising • Emo wave detected •
</span>
</div>

</div>

<script>

const streams = {RADIO};

function play(station) {{

    let audio = document.getElementById("audio");
    let list = streams[station];
    let i = 0;

    document.getElementById("nowplaying").innerText =
    "NOW PLAYING: " + station.toUpperCase();

    function tryNext() {{
        if(i >= list.length) return;

        audio.src = list[i];

        audio.play().catch(() => {{
            i++;
            tryNext();
        }});

        let failTimer = setTimeout(() => {{
            if(audio.readyState < 2) {{
                i++;
                tryNext();
            }}
        }}, 3500);

        audio.onplaying = () => clearTimeout(failTimer);
    }}

    tryNext();
}}

// 💬 LIVE MSN CHAT
const messages = [
    "SYSTEM: connection stable 🗽",
    "Ashley: MTV is back?? 😭",
    "Mike: burning CD vibe 💿",
    "Emma: 2000s forever 🎸",
    "Jake: pop punk never died 🖤",
    "NYC: signal strong 📡"
];

setInterval(() => {{
    let chat = document.getElementById("chat");

    let div = document.createElement("div");
    div.className = "msg";

    div.innerText =
        messages[Math.floor(Math.random() * messages.length)];

    chat.appendChild(div);

    if(chat.children.length > 9) {{
        chat.removeChild(chat.children[0]);
    }}
}}, 2200);

</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return jsonify({
        "response": {
            "text": "MTV PRO radio online",
            "end_session": False
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)