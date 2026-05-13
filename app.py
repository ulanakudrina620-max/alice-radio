from flask import Flask
import os

app = Flask(__name__)

RADIO = {
    "indie dreams": "https://ice1.somafm.com/indiepop-128-mp3",
    "late night chill": "https://ice1.somafm.com/groovesalad-128-mp3",
    "soft pop 2000s": "https://ice1.somafm.com/poptron-128-mp3",
    "emo memories": "https://ice1.somafm.com/punkrockers-128-mp3",
    "dreamy beats": "https://ice1.somafm.com/beatblender-128-mp3"
}


@app.route("/")
def home():

    stations = ""
    for k in RADIO:
        stations += f"<div class='btn' onclick=\"play('{k}')\">{k}</div>"

    html = f"""
<!DOCTYPE html>
<html>
<head>
<title>tumblr 2012 radio</title>

<style>

/* 🌙 TUMBLR NIGHT AESTHETIC */
body {{
    margin: 0;
    font-family: Helvetica, Arial;
    background:
    linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)),
    url('https://images.unsplash.com/photo-1492684223066-81342ee5ff30?auto=format&fit=crop&w=2000&q=80');
    background-size: cover;
    color: #e6e6e6;
    overflow: hidden;
}}

/* 🌫 grain overlay */
.grain {{
    position: fixed;
    width: 100%;
    height: 100%;
    pointer-events: none;
    background-image: url("https://www.transparenttextures.com/patterns/noise.png");
    opacity: 0.05;
}}

/* 📱 layout */
.container {{
    display: flex;
    height: 100vh;
    padding: 20px;
    gap: 20px;
}}

/* 🎧 player card */
.card {{
    width: 400px;
    background: rgba(20,20,25,0.75);
    border-radius: 12px;
    padding: 15px;
    backdrop-filter: blur(8px);
    box-shadow: 0 0 30px rgba(0,0,0,0.5);
}}

.title {{
    font-size: 18px;
    margin-bottom: 10px;
    opacity: 0.9;
}}

.btn {{
    background: rgba(255,255,255,0.08);
    padding: 8px;
    margin: 5px 0;
    border-radius: 8px;
    cursor: pointer;
    transition: 0.2s;
}}

.btn:hover {{
    background: rgba(255,255,255,0.15);
}}

/* 🎧 audio */
audio {{
    width: 100%;
    margin-top: 10px;
    filter: grayscale(1);
}}

/* 💬 tumblr feed */
.feed {{
    flex: 1;
    overflow: hidden;
}}

.post {{
    background: rgba(20,20,25,0.75);
    margin-bottom: 15px;
    padding: 15px;
    border-radius: 12px;
    backdrop-filter: blur(8px);
}}

.tag {{
    color: #8aa0ff;
    font-size: 12px;
    margin-top: 5px;
}}

/* 🖤 subtle glow */
h1 {{
    font-size: 22px;
    opacity: 0.9;
}}

</style>
</head>

<body>

<div class="grain"></div>

<div class="container">

<!-- 🎧 MUSIC -->
<div class="card">
<div class="title">🌙 indie radio</div>

{stations}

<audio id="audio" controls></audio>

<p style="opacity:0.6;font-size:12px;margin-top:10px;">
“it’s 2am and this song feels like a memory”
</p>

</div>

<!-- 🖤 TUMBLR FEED -->
<div class="feed">

<div class="post">
<h1>late night thoughts</h1>
<p>music hits different when the world is quiet.</p>
<div class="tag">#indie #night #2000s</div>
</div>

<div class="post">
<h1>nostalgia wave</h1>
<p>burning CDs, scrolling old blogs, feeling everything again.</p>
<div class="tag">#tumblr #emo #memories</div>
</div>

<div class="post">
<h1>currently playing</h1>
<p id="now">select a station…</p>
<div class="tag">#nowplaying</div>
</div>

</div>

</div>

<script>

const streams = {RADIO};

/* 🎧 play music */
function play(station) {{
    document.getElementById("audio").src = streams[station];
    document.getElementById("audio").play().catch(()=>{{}});
    document.getElementById("now").innerText = station;
}}

/* 💬 tumblr-style “life feed” */
const lines = [
    "someone liked your post.",
    "you are listening to memories.",
    "it’s raining somewhere in your mind.",
    "this song feels like 2012.",
    "you reblogged a feeling.",
    "late night internet is different."
];

setInterval(()=>{{
    const feed = document.querySelector(".feed");

    const post = document.createElement("div");
    post.className = "post";
    post.innerHTML = `
        <p>${{lines[Math.floor(Math.random()*lines.length)]}}</p>
        <div class="tag">#tumblr #late night</div>
    `;

    feed.appendChild(post);

    if(feed.children.length > 6) {{
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
    return {"response": {"text": "tumblr indie radio active", "end_session": False}}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)