from flask import Flask, render_template, request

app = Flask(__name__)

DESTINATIONS = {
    "東京": {
        "intro": "定番スポットと食べ歩きを楽しむ東京プランです。",
        "spots": [
            ("浅草・浅草寺", "歴史ある街並みを散策し、仲見世で食べ歩き。", "午前"),
            ("上野公園", "公園や美術館でゆったり過ごす。", "昼"),
            ("渋谷・原宿", "ショッピングやカフェ巡りを楽しむ。", "午後"),
            ("東京スカイツリー", "展望台から東京の景色を眺める。", "夕方"),
        ],
        "food": "もんじゃ焼き、寿司、ラーメン"
    },
    "京都": {
        "intro": "お寺や町並みを巡り、和の雰囲気を楽しむ京都プランです。",
        "spots": [
            ("清水寺", "京都らしい景色と参道の散策を楽しむ。", "午前"),
            ("祇園", "伝統的な町並みを歩き、写真を撮る。", "昼"),
            ("錦市場", "京都の食べ物を少しずつ食べ歩く。", "午後"),
            ("伏見稲荷大社", "朱色の鳥居が続く参道を散策する。", "夕方"),
        ],
        "food": "湯豆腐、抹茶スイーツ、京料理"
    },
    "大阪": {
        "intro": "観光とグルメを満喫する、友達とのにぎやかな大阪プランです。",
        "spots": [
            ("大阪城公園", "大阪城を見学し、公園を散策する。", "午前"),
            ("道頓堀", "有名な看板の前で写真を撮る。", "昼"),
            ("心斎橋", "ショッピングやカフェを楽しむ。", "午後"),
            ("新世界", "串カツなど大阪グルメを味わう。", "夕方"),
        ],
        "food": "たこ焼き、お好み焼き、串カツ"
    },
    "北海道": {
        "intro": "自然とおいしい食べ物を楽しむ北海道プランです。",
        "spots": [
            ("大通公園", "街の中心で散歩や写真撮影を楽しむ。", "午前"),
            ("札幌市時計台", "札幌の定番スポットを見学する。", "昼"),
            ("白い恋人パーク", "お菓子の世界観やスイーツを楽しむ。", "午後"),
            ("すすきの", "夜ごはんや街歩きを楽しむ。", "夕方"),
        ],
        "food": "海鮮丼、味噌ラーメン、ジンギスカン"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    plan = None
    if request.method == "POST":
        destination = request.form.get("destination", "東京")
        days = max(1, min(int(request.form.get("days", 1)), 5))
        budget = request.form.get("budget", "節約")
        interests = request.form.getlist("interests")
        companions = request.form.get("companions", "友達")
        info = DESTINATIONS.get(destination, DESTINATIONS["東京"])
        spots = info["spots"]
        itinerary = []
        for day in range(days):
            daily_spots = spots[day % len(spots):] + spots[:day % len(spots)]
            itinerary.append({
                "day": day + 1,
                "spots": daily_spots[:3],
                "note": f"{companions}と{destination}を楽しむ日です。"
            })
        tips = []
        if budget == "節約":
            tips.append("交通費を抑えるため、近い場所をまとめて回りましょう。")
            tips.append("事前に割引チケットや一日乗車券を確認すると便利です。")
        elif budget == "普通":
            tips.append("食事や体験に少し予算を使い、移動は公共交通機関がおすすめです。")
        else:
            tips.append("人気のお店は予約し、移動にタクシーを使うとゆったり過ごせます。")
        if interests:
            tips.append("興味のあること：" + "、".join(interests))
        plan = {
            "destination": destination, "days": days, "budget": budget,
            "companions": companions, "intro": info["intro"],
            "food": info["food"], "itinerary": itinerary, "tips": tips
        }
    return render_template("index.html", destinations=DESTINATIONS.keys(), plan=plan)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(os.environ.get("PORT", 5000)), debug=False)
