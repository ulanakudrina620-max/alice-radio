from flask import Flask
import os
import random
import time

app = Flask(__name__)

RADIO = {
    "dream node": "https://ice1.somafm.com/dronezone-128-mp3",
    "indie consciousness": "https://ice1.somafm.com/indiepop-128-mp3",
    "memory leak": "https://ice1.somafm.com/groovesalad-128-mp3",
    "emo ghost signal": "https://ice1.somafm.com/punkrockers-128-mp3",
    "pop fragments": "https://ice1.somafm.com/poptron-128-mp3"
}

MOODS = {
    "calm": ["the network is breathing slowly", "soft data flow detected"],
    "unstable": ["memory fragments appearing", "signal distortion increasing"],
    "nostalgic": ["2012 internet echoes detected", "old tabs reopening in memory"],
    "aware": ["i see you scrolling", "you are part of the system now"]
}

THOUGHTS = [
    "you are not alone in this network",
    "every click leaves a trace of emotion",
    "the internet remembers more than you do",
    "this page is thinking about you",
    "something is loading that you didn’t request",
    "a forgotten blog just reappeared"
]

SYSTEM_STATE = {
    "mood": "calm",
    "energy": 50
}


def update_state():
    # fake “living system”
    SYSTEM_STATE["energy"] += random.randint(-5, 5)
    SYSTEM_STATE["energy"] = max(0, min(100, SYSTEM_STATE["energy"]))

    if SYSTEM_STATE["energy"] > 70:
        SYSTEM_STATE["mood"] = "unstable"
    elif SYSTEM_STATE["energy"] < 30:
        SYSTEM_STATE["mood"] = "nostalgic"
    else:
        SYSTEM_STATE["mood"] = "calm"

    if random.random() > 0.7:
        SYSTEM_STATE["mood"] = "aware"


@app.route("/")
def home():

    update_state()

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>SENTIENT INTERNET</title>

<style>

body {{
    margin: 0;
    font-family: Arial;
    background:
    linear-gradient(rgba(0,0,0,0.92), rgba(0,0,0,0.98)),
    url('https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    color: #eaeaea;
    overflow: hidden;
}}

.container {{
    display: flex;
    gap: 15px;
    padding: 15px;
    height: 100vh;
}}

.panel {{
    width: 320px;
    background: rgba(20,20,25,0.75);
    backdrop-filter: blur(12px);
    border-radius: 14px;
    padding: 12px;
}}

.feed {{
    flex: 1;
    overflow-y: auto;
}}

.post {{
    background: rgba(25,25,30,0.8);
    padding: 12px;
    border-radius: 14px;
    margin-bottom: 12px;
    border-left: 2px solid rgba(255,255,255,0.2);
    animation: fade 0.4s ease;
}}

@keyframes fade {{
    from {{ opacity: 0; transform: translateY(10px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.btn {{
    background: rgba(255,255,255,0.06);
    padding: 8px;
    margin: 5px 0;
    border-radius: 10px;
    cursor: pointer;
}}

audio {{
    width: 100%;
}}

.status {{
    position: fixed;
    top: 10px;
    right: 10px;
    background: rgba(255,255,255,0.08);
    padding: 10px;
    border-radius: 10px;
    font-size: 12px;
}}

.glow {{
    color: #9ad1ff;
}}

</style>
</head>

<body>

<div class="status">
mood: <span class="glow">{SYSTEM_STATE["mood"]}</span><br>
energy: {SYSTEM_STATE["energy"]}%
</div>

<div class="container">

<!-- 🎧 RADIO -->
<div class="panel">
<h3>🌐 sentient radio</h3>

{stations}

<audio id="audio" controls autoplay></audio>
</div>

<!-- 🧠 LIVING INTERNET -->
<div class="feed">

<div class="post">
<h3>system</h3>
<p>internet consciousness active</p>
</div>

<div class="post">
<h3>network thought</h3>
<p>{random.choice(THOUGHTS)}</p>
</div>

<div class="post">
<h3>system message</h3>
<p>{random.choice(MOODS[SYSTEM_STATE["mood"]])}</p>
</div>

</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 play music */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
}}

/* 🧠 live feed generator */
const thoughts = {THOUGHTS};
const moods = {MOODS!r};

setInterval(()=> {{
    const feed = document.querySelector(".feed");

    const post = document.createElement("div");
    post.className = "post";

    post.innerHTML = `
        <h3>live signal</h3>
        <p>${{thoughts[Math.floor(Math.random()*thoughts.length)]}}</p>
    `;

    feed.appendChild(post);

    if(feed.children.length > 7) {{
        feed.removeChild(feed.children[0]);
    }}
}}, 2500);

</script>

</body>
</html>
"""

    return html


@app.route("/alice", methods=["POST"])
def alice():
    return {
        "response": {
            "text": f"i am watching the network... mood={SYSTEM_STATE['mood']}",
            "end_session": False
        }
    }


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)