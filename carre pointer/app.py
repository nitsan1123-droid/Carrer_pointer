import os
import random

from flask import Flask, redirect, render_template, request, send_from_directory, url_for

from data import CAREERS, COLLEGES, QUIZ, STREAM_COLORS, STREAMS

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, template_folder=BASE_DIR, static_folder=None)


@app.context_processor
def stream_styles():
    return {"colors": STREAM_COLORS}


@app.route("/style.css")
def stylesheet():
    return send_from_directory(BASE_DIR, "style.css")


def read_answers(text):
    answers = []
    if not text:
        return answers
    for number, part in enumerate(text.split(".")):
        if number >= len(QUIZ) or not part.isdigit() or int(part) >= len(QUIZ[number]["answers"]):
            break
        answers.append(int(part))
    return answers


def join_answers(answers):
    return ".".join(str(answer) for answer in answers)


@app.route("/")
def home():
    stream_counts = {}
    for stream in STREAMS:
        stream_counts[stream] = 0
    for career in CAREERS:
        stream_counts[career["stream"]] += 1

    counts = {
        "careers": len(CAREERS),
        "colleges": len(COLLEGES),
        "countries": len(set(college["country"] for college in COLLEGES)),
    }

    return render_template("index.html", streams=STREAMS, stream_counts=stream_counts, counts=counts)


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    answers = []

    if request.method == "POST":
        answers = read_answers(request.form.get("answers", ""))

        if "back" in request.form:
            answers = answers[:-1]
        else:
            picked = request.form.get("answer", "")
            step = len(answers)
            if step < len(QUIZ) and picked.isdigit() and int(picked) < len(QUIZ[step]["answers"]):
                answers.append(int(picked))

        if len(answers) == len(QUIZ):
            return redirect(url_for("result", a=join_answers(answers)))

    step = len(answers)
    options = list(enumerate(QUIZ[step]["answers"]))
    random.shuffle(options)

    return render_template(
        "quiz.html",
        step=step,
        total=len(QUIZ),
        question=QUIZ[step]["question"],
        options=options,
        answers=join_answers(answers),
        progress=round(step * 100 / len(QUIZ)),
    )


@app.route("/result")
def result():
    answers = read_answers(request.args.get("a", ""))
    if len(answers) != len(QUIZ):
        return redirect(url_for("quiz"))

    scores = {}
    for stream in STREAMS:
        scores[stream] = 0

    chosen = []
    for number, picked in enumerate(answers):
        text, stream = QUIZ[number]["answers"][picked]
        scores[stream] += 1
        chosen.append({"question": QUIZ[number]["question"], "text": text, "stream": stream})

    total = len(QUIZ)
    ranking = sorted(scores.items(), key=lambda pair: pair[1], reverse=True)
    best = ranking[0][0]

    percents = {}
    for stream, points in scores.items():
        percents[stream] = round(points * 100 / total)

    slices = []
    start = 0
    for stream, points in ranking:
        if points == 0:
            continue
        end = start + points * 100 / total
        slices.append(STREAM_COLORS[stream] + " " + format(start, ".2f") + "% " + format(end, ".2f") + "%")
        start = end
    pie = ", ".join(slices)

    matches = []
    for career in CAREERS:
        if career["stream"] == best:
            matches.append(career)

    return render_template(
        "result.html",
        best=best,
        ranking=ranking,
        scores=scores,
        percents=percents,
        total=total,
        pie=pie,
        chosen=chosen,
        matches=matches,
    )


@app.route("/careers")
def careers():
    chosen = request.args.get("stream", "All")
    query = request.args.get("q", "").strip()

    shown = []
    for career in CAREERS:
        if chosen != "All" and career["stream"] != chosen:
            continue
        searchable = " ".join([career["name"], career["about"], career["stream"]] + career["skills"]).lower()
        if query and query.lower() not in searchable:
            continue
        shown.append(career)

    return render_template("careers.html", careers=shown, streams=STREAMS, chosen=chosen, query=query)


@app.route("/colleges")
def colleges():
    country = request.args.get("country", "All")
    stream = request.args.get("stream", "All")
    budget_text = request.args.get("budget", "")

    try:
        budget = int(budget_text)
    except ValueError:
        budget = None

    results = []
    for college in COLLEGES:
        if country != "All" and college["country"] != country:
            continue
        if stream != "All" and stream not in college["streams"]:
            continue
        if budget is not None and college["fee_usd"] > budget:
            continue
        results.append(college)

    results.sort(key=lambda college: college["fee_usd"])

    countries = sorted(set(college["country"] for college in COLLEGES))
    max_fee = max(college["fee_usd"] for college in COLLEGES)

    return render_template(
        "colleges.html",
        results=results,
        countries=countries,
        streams=STREAMS,
        country=country,
        stream=stream,
        budget=budget_text,
        max_fee=max_fee,
    )


if __name__ == "__main__":
    app.run(debug=True)
