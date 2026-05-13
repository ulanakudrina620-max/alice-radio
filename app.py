from flask import Flask, jsonify
import os

app = Flask(__name__)

# 🎧 STABLE 2000s / 2010 ERA RADIO STREAMS
RADIO = {

    # 💿 2000s POP HITS (Britney, Rihanna, Katy Perry era)
    "pop_2000s": [
        "https://ice1.somafm.com/poptron-128-mp3"
    ],

    # 🎸 ALT / INDIE 2000s (Arctic Monkeys / The Strokes vibe)
    "indie_rock": [
        "https://ice1.somafm.com/indiepop-128-mp3"
    ],

    # 🎸 POP PUNK / EMO (Green Day / Fall Out Boy / Paramore vibe)
    "pop_punk": [
        "https://ice1.somafm.com/punkrockers-128-mp3"
    ],

    # 🪩 2000s CLUB / DANCE / EURODANCE
    "dance_2000s": [
        "https://ice1.somafm.com/beatblender-128-mp3"
    ],

    # 🎤 HIP HOP 2000s (50 Cent / Eminem / Jay-Z vibe)
    "hiphop_2000s": [
        "https://ice1.somafm.com/dubstep-128-mp3"
    ],

    # 🌙 CHILL / NIGHT DRIVE (2000s late-night vibe)
    "chill_night": [
        "https://ice1.somafm.com/groovesalad-128-mp3"
    ],

    # 🎧 R&B / SOUL 2000s (Alicia Keys / Usher vibe)
    "rnb_2000s": [
        "https://ice1.somafm.com/smoothjazz-128-mp3"
    ],

    # 🇬🇧 UK / MTV EUROPE 2000s VIBE
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
<title>MTV 2003 DESKTOP RADIO</title>

<style>

body {{
    margin: 0;
    font-family: Tahoma, Arial;

    background:
    linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.92)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');

    background-size: cover;
    background-position: center;

    height: 100vh;
    overflow: hidden;
}}

.window {{
    width: 100vw;
    height: 100vh;

    display: flex;
    flex-direction: column;
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

.logo {{
    font-size: 18px;
}}

.online {{
    color: #00ff88;
    font-size: 12px;
}}

.main {{
    flex: 1;
    display: flex;
    padding: 20px;
    gap: 20px;
}}

.sidebar {{
    width: 280px;
    background: rgba(0,0,0,0.45);
    border-radius: 12px;
    padding: 15px;
}}

.title {{
    font-size: 12px;
    opacity: 0.6;
    margin-bottom: 10px;
}}

.btn {{
    background: linear-gradient(to bottom, #3daeff, #0050aa);
    border: 1px solid #7fd4ff;

    padding: 10px;
    margin-bottom: 10px;

    border-radius: 10px;

    cursor: pointer;

    text-align: center;
    font-weight: bold;
    font-size: 13px;
}}

.btn:hover {{
    transform: scale(1.03);
}}

.player {{
    flex: 1;
    background: rgba(0,0,0,0.55);
    border-radius: 14px;
    padding: 20px;
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

.chat {{
    margin-top: 15px;
    background: rgba(0,0,0,0.35);
    border-radius: 10px;
    padding: 10px;
    height: 120px;
    font-size: 12px;
}}

.msg {{
    margin-bottom: 4px;
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
    animation: ticker 28s linear infinite;
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
<div class="logo">📺 MTV RADIO 2003 — 2000s ERA</div>
<div class="online">● ONLINE</div>
</div>

<div class="main">

<div class="sidebar">

<div class="title">2000–2010 STATIONS</div>

<div class="btn" onclick="play('pop_2000s')">💿 POP 2000s</div>
<div class="btn" onclick="play('indie_rock')">🎸 INDIE ROCK</div>
<div class="btn" onclick="play('pop_punk')">🔥 POP PUNK / EMO</div>
<div class="btn" onclick="play('dance_2000s')">🪩 DANCE HITS</div>
<div class="btn" onclick="play('hiphop_2000s')">🎤 HIP HOP</div>
<div class="btn" onclick="play('rnb_2000s')">🎧 R&B / SOUL</div>
<div class="btn" onclick="play('chill_night')">🌙 NIGHT CHILL</div>
<div class="btn" onclick="play('uk_pop')">🇬🇧 UK HITS</div>

</div>

<div class="player">

<div class="screen">
<div class="nowplaying" id="nowplaying">NOW PLAYING: idle</div>
</div>

<audio id="audio" controls autoplay></audio>

<div class="chat">
<div class="msg">SYSTEM: connected to NYC signal 🗽</div>
<div class="msg">Ashley: 2007 vibes hit different 😭</div>
<div class="msg">Mike: burning CD right now 💿</div>
</div>

</div>

</div>

<div class="ticker">
<span>
BREAKING: MTV still relevant in alternate timeline • MySpace revival detected • iPod Classic sales rising • Pop punk returning to NYC • Limewire archive reactivated • 2000s music wave spreading globally • Windows XP still stable somehow • CD-R production increased • Emo revival in Brooklyn •
</span>
</div>

</div>

<script>

const streams = {RADIO};

function play(station) {{

    document.getElementById("nowplaying").innerText =
    "NOW PLAYING: " + station.toUpperCase();

    let audio = document.getElementById("audio");
    let list = streams[station];
    let i = 0;

    function next() {{

        if(i >= list.length) return;

        audio.src = list[i];

        audio.play().catch(() => {{
            i++;
            next();
        }});

        let t = setTimeout(() => {{
            if(audio.readyState < 2) {{
                i++;
                next();
            }}
        }}, 4000);

        audio.onplaying = () => clearTimeout(t);
    }}

    next();
}}

</script>

</body>
</html>
"""


@app.route("/alice", methods=["POST"])
def alice():
    return jsonify({
        "response": {
            "text": "MTV 2000s Radio active",
            "end_session": False
        }
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)