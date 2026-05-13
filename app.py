from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "POP 2000s": "https://ice1.somafm.com/poptron-128-mp3",
    "INDIE XP": "https://ice1.somafm.com/indiepop-128-mp3",
    "PUNK XP": "https://ice1.somafm.com/punkrockers-128-mp3",
    "DANCE XP": "https://ice1.somafm.com/beatblender-128-mp3",
    "CHILL XP": "https://ice1.somafm.com/groovesalad-128-mp3"
}


@app.route("/")
def home():

    buttons = ""
    for k in RADIO:
        buttons += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>MTV XP RADIO + CHAT</title>

<style>

body {{
    margin: 0;
    font-family: Tahoma;
    background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    height: 100vh;
    overflow: hidden;
}}

.desktop {{
    display: flex;
    height: 100vh;
}}

.sidebar {{
    width: 240px;
    background: rgba(0,0,0,0.65);
    padding: 10px;
}}

.btn {{
    background: #1e6bff;
    color: white;
    padding: 10px;
    margin: 6px 0;
    cursor: pointer;
    border-radius: 6px;
    text-align: center;
}}

.player {{
    flex: 1;
    padding: 20px;
    color: white;
}}

audio {{
    width: 100%;
}}

.chat {{
    margin-top: 10px;
    background: rgba(0,0,0,0.75);
    padding: 10px;
    height: 180px;
    overflow: hidden;
    font-size: 12px;
}}

.msg {{
    margin: 4px 0;
    color: white;
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
    animation: move 18s linear infinite;
}}

@keyframes move {{
    from {{ transform: translateX(0); }}
    to {{ transform: translateX(-100%); }}
}}

</style>
</head>

<body>

<div class="desktop">

<div class="sidebar">
{buttons}
</div>

<div class="player">

<h2 id="now">SELECT STATION</h2>

<audio id="audio" controls></audio>

<div class="chat" id="chat">
<div class="msg">SYSTEM: MSN Messenger connected 💬</div>
<div class="msg">Ashley: 2000s vibes are back 😭</div>
<div class="msg">Mike: burning CD right now 💿</div>
</div>

</div>

</div>

<div class="ticker">
<span>
BREAKING NEWS: MTV returns to peak 2003 • MySpace profiles trending again • Winamp skins downloaded worldwide • Limewire activity spikes • iPod Nano nostalgia wave • MSN Messenger servers simulated online • Pop-punk revival in NYC • Avril Lavigne dominates charts again • CD burning software downloads increase • Napster-era memories resurface •
</span>
</div>

<script>

const streams = {RADIO};

/* 🎧 PLAY */
function play(station) {{
    const audio = document.getElementById("audio");
    document.getElementById("now").innerText = "NOW PLAYING: " + station;

    audio.src = streams[station];
    audio.play().catch(()=>{{}});
}}

/* 💬 MSN-STYLE CHAT VARIETY */
const chatLines = [
    "Ashley: OMG this song was on MySpace 😭",
    "Mike: I miss Winamp skins lol 💿",
    "DJ: MTV countdown vibes are back 🎧",
    "SYSTEM: user connected via dial-up simulation",
    "Emma: burning CDs was a lifestyle",
    "Jake: this feels like Limewire era 💀",
    "NYC: signal stable 🗽",
    "Tom: iPod shuffle energy detected",
    "Lisa: MSN status = BRB listening to pop punk",
    "Alex: 2000s internet was WILD"
];

setInterval(() => {{
    const chat = document.getElementById("chat");

    const div = document.createElement("div");
    div.className = "msg";

    div.innerText = chatLines[Math.floor(Math.random()*chatLines.length)];

    chat.appendChild(div);

    if(chat.children.length > 10) {{
        chat.removeChild(chat.children[0]);
    }}

}}, 1800);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "MTV XP CHAT MODE ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)