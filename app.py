from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "night indie": "https://ice1.somafm.com/indiepop-128-mp3",
    "dream pop": "https://ice1.somafm.com/dronezone-128-mp3",
    "emo nostalgia": "https://ice1.somafm.com/punkrockers-128-mp3",
    "soft beats": "https://ice1.somafm.com/groovesalad-128-mp3",
    "2000s pop": "https://ice1.somafm.com/poptron-128-mp3"
}

MOODS = [
    "it’s 2am and everything feels different",
    "this song feels like a memory",
    "internet was softer in 2012",
    "you are alone but not really",
    "scrolling thoughts instead of sleeping"
]


@app.route("/")
def home():

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>Night Radio / Internet Nostalgia</title>

<style>

body {{
    margin: 0;
    font-family: Arial;
    background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1506905925346-21bda4d32df4?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    color: #eaeaea;
    overflow: hidden;
}}

.blur {{
    position: fixed;
    width: 100%;
    height: 100%;
    backdrop-filter: blur(2px);
    opacity: 0.6;
}}

.container {{
    display: flex;
    height: 100vh;
    padding: 20px;
    gap: 20px;
}}

/* 🌙 RADIO */
.radio {{
    width: 320px;
    background: rgba(20,20,25,0.7);
    border-radius: 14px;
    padding: 15px;
}}

.btn {{
    background: rgba(255,255,255,0.06);
    padding: 8px;
    margin: 6px 0;
    border-radius: 10px;
    cursor: pointer;
}}

audio {{
    width: 100%;
    margin-top: 10px;
}}

/* 🧠 MODE SWITCH */
.mode {{
    position: fixed;
    top: 10px;
    right: 10px;
    background: rgba(255,255,255,0.08);
    padding: 10px;
    border-radius: 10px;
    cursor: pointer;
}}

/* 🕰 TUMBLR FEED */
.feed {{
    flex: 1;
    overflow-y: auto;
}}

.post {{
    background: rgba(20,20,25,0.75);
    margin-bottom: 12px;
    padding: 12px;
    border-radius: 14px;
}}

.hidden {{
    display: none;
}}

</style>
</head>

<body>

<div class="blur"></div>

<div class="mode" onclick="toggleMode()">
switch mode 🌗
</div>

<div class="container">

<!-- 🌙 RADIO MODE -->
<div class="radio" id="radioPanel">
<h3>🌙 Night Radio</h3>

{stations}

<audio id="audio" autoplay controls></audio>

<p style="opacity:0.6;font-size:12px;">
“music starts instantly”
</p>
</div>

<!-- 🕰 INTERNET MODE -->
<div class="feed hidden" id="feed">

<div class="post">
<h3>internet nostalgia</h3>
<p>we used to feel more online in 2012.</p>
</div>

<div class="post">
<h3>thought</h3>
<p id="mood"></p>
</div>

</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 autoplay vibe */
window.onload = () => {{
    document.getElementById("audio").src = streams["night indie"];
    document.getElementById("audio").play().catch(()=>{{}});
}};

/* 🎧 play station */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
}}

/* 🌗 mode switch */
function toggleMode() {{
    document.getElementById("radioPanel").classList.toggle("hidden");
    document.getElementById("feed").classList.toggle("hidden");
}}

/* 🧠 mood generator */
const moods = {MOODS};

setInterval(()=> {{
    let el = document.getElementById("mood");
    if(el) {{
        el.innerText = moods[Math.floor(Math.random()*moods.length)];
    }}
}}, 2500);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "night radio + nostalgia mode active", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)