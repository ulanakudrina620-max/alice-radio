from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "MTV POP 2003": "https://ice1.somafm.com/poptron-128-mp3",
    "MYSPACE INDIE": "https://ice1.somafm.com/indiepop-128-mp3",
    "POP PUNK ERA": "https://ice1.somafm.com/punkrockers-128-mp3",
    "DANCE 2005": "https://ice1.somafm.com/beatblender-128-mp3",
    "CHILL NIGHT": "https://ice1.somafm.com/groovesalad-128-mp3"
}


@app.route("/")
def home():

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">📻 {k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>XP NEXT LEVEL DESKTOP</title>

<style>

body {{
    margin: 0;
    font-family: Tahoma;
    background:
    linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1518391846015-55a9cc003b25?auto=format&fit=crop&w=2000&q=80');
    overflow: hidden;
}}

.desktop {{
    width: 100%;
    height: 100vh;
    position: relative;
}}

/* 🪟 WINDOW SYSTEM */
.window {{
    position: absolute;
    width: 320px;
    background: rgba(0,0,0,0.85);
    border: 2px solid #3aa0ff;
    border-radius: 8px;
    color: white;
    box-shadow: 0 0 15px rgba(0,150,255,0.4);
}}

.titlebar {{
    background: linear-gradient(to right, #0b2a6f, #1e6bff);
    padding: 5px;
    cursor: move;
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    font-weight: bold;
}}

.controls span {{
    margin-left: 8px;
    cursor: pointer;
}}

.content {{
    padding: 10px;
}}

.btn {{
    background: #1e6bff;
    padding: 6px;
    margin: 4px 0;
    border-radius: 6px;
    text-align: center;
    cursor: pointer;
}}

.btn:hover {{
    background: #3399ff;
}}

/* 📻 RADIO */
#radio {{ top: 70px; left: 60px; }}
/* 💬 CHAT */
#chat {{ top: 110px; left: 420px; }}
/* 📁 DESKTOP ICON */
.icon {{
    width: 80px;
    color: white;
    text-align: center;
    margin: 20px;
    cursor: pointer;
}}

.icon:hover {{
    transform: scale(1.05);
}}

/* 🟦 TASKBAR */
.taskbar {{
    position: fixed;
    bottom: 0;
    width: 100%;
    height: 40px;
    background: linear-gradient(to right, #0b2a6f, #1e6bff);
    display: flex;
    align-items: center;
    color: white;
    padding: 0 10px;
}}

.start {{
    background: #00aa00;
    padding: 5px 12px;
    cursor: pointer;
    margin-right: 10px;
}}

.task {{
    margin-left: 10px;
    background: rgba(255,255,255,0.2);
    padding: 3px 8px;
    border-radius: 4px;
    cursor: pointer;
}}

audio {{
    width: 100%;
}}

.msg {{
    font-size: 11px;
    margin: 3px 0;
    background: rgba(255,255,255,0.05);
    padding: 4px;
    border-radius: 4px;
}}

</style>
</head>

<body>

<div class="desktop">

<!-- 📻 RADIO -->
<div class="window" id="radio">
<div class="titlebar">
<span>📻 RADIO</span>
<div class="controls">
<span onclick="minimize('radio')">_</span>
<span onclick="closeWin('radio')">X</span>
</div>
</div>
<div class="content">
{stations}
<audio id="audio" controls></audio>
</div>
</div>

<!-- 💬 CHAT -->
<div class="window" id="chat">
<div class="titlebar">
<span>💬 MSN CHAT</span>
<div class="controls">
<span onclick="minimize('chat')">_</span>
<span onclick="closeWin('chat')">X</span>
</div>
</div>
<div class="content" id="chatBox">
<div class="msg">SYSTEM: XP DESKTOP ONLINE</div>
<div class="msg">Ashley: MSN vibes 💬</div>
</div>
</div>

<!-- 📁 ICON -->
<div class="icon" onclick="openWin('chat')">
📁<br>My Chat
</div>

</div>

<!-- 🟦 TASKBAR -->
<div class="taskbar">
<div class="start" onclick="alert('START MENU')">START</div>
<div class="task" onclick="openWin('radio')">Radio</div>
<div class="task" onclick="openWin('chat')">Chat</div>
</div>

<script>

const streams = {RADIO};

/* 🎧 PLAY RADIO */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
}}

/* 🪟 WINDOW SYSTEM */
function openWin(id) {{
    document.getElementById(id).style.display = "block";
}}

function closeWin(id) {{
    document.getElementById(id).style.display = "none";
}}

function minimize(id) {{
    document.getElementById(id).style.display = "none";
}}

/* 🖱️ DRAG */
function drag(win) {{
    let isDown = false, ox, oy;

    win.querySelector(".titlebar").addEventListener("mousedown", (e)=>{{
        isDown = true;
        ox = e.clientX - win.offsetLeft;
        oy = e.clientY - win.offsetTop;
        win.style.zIndex = 999;
    }});

    document.addEventListener("mousemove", (e)=>{{
        if(!isDown) return;
        win.style.left = (e.clientX - ox) + "px";
        win.style.top = (e.clientY - oy) + "px";
    }});

    document.addEventListener("mouseup", ()=> isDown=false);
}}

document.querySelectorAll(".window").forEach(drag);

/* 💬 CHAT LIVE */
const msgs = [
    "Mike: XP is alive again 💿",
    "Ashley: MSN forever 💬",
    "DJ: MTV mode ON",
    "NYC: signal stable 🗽",
    "Emma: Winamp vibes 🎧"
];

setInterval(()=> {{
    const box = document.getElementById("chatBox");
    const div = document.createElement("div");
    div.className = "msg";
    div.innerText = msgs[Math.floor(Math.random()*msgs.length)];
    box.appendChild(div);

    if(box.children.length > 10) box.removeChild(box.children[0]);
}}, 1400);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {"response": {"text": "NEXT LEVEL DESKTOP ACTIVE", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)