from flask import Flask, render_template
app = Flask(__name__)


videos={
    "1":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/CIfGUiICf8U?autoplay=1&mute=1" title="ＭＩＮＥＣＲＡＦＴ　ＬＯＦＩ　＆　ＣＨＩＬＬ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":"Minecraft Lofi",
        },
    "2":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/WDXPJWIgX-o?autoplay=1&mute=1" title="anime lofi hip hop radio - 24/7 chill lofi remixes of anime" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Anime Lofi'
        },
    "3":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/2GjPQfdQfMY?autoplay=1&mute=1" title="Lo-fi for Ghosts (Only)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Lofi For Ghosts Only'
        },
    "4":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/kgx4WGK0oNU?autoplay=1&mute=1" title="jazz/lofi hip hop radio🌱chill beats to relax/study to [LIVE 24/7]" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Lofi Guy'
        },
    "5":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/s3LXEbREa4g?autoplay=1&mute=1" title="💤 Aalsi by Advait (Full Album)" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Aalsi By Advait'
        },
    "6":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/NxSDNogkKX0?autoplay=1&mute=1" title="Just wanna stay here forever ~ lofi hip hop mix" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Just Wanna Stay Here Forever'
        },
    "7":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/ceqgwo7U28Y?autoplay=1&mute=1" title="ＣＨＩＬＬ　ＲＡＤＩＯ ２４／７" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Adventure Time Lofi'
        },
    "8":{
        "link":'<iframe class="responsive-frame" width="974" height="548" src="https://www.youtube.com/embed/jfKfPfyJRdk?autoplay=1&mute=1" title="lofi hip hop radio - beats to relax/study to" allow="autoplay" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>',
        "title":'Lofi Girl'
    },}

@app.route("/")
def home():
    return render_template("index.html",videos=videos)


@app.route("/<video_id>")
def play_song(video_id):
    video_link=videos[video_id]["link"]
    video_title=videos[video_id]["title"]
    return render_template("player.html",video_link=video_link,video_title=video_title)
    
if __name__=="__main__":
    app.run()
