# Carrer Pointer

A website that helps students anywhere in the world:
1. **Find their stream** with a short quiz (Science, Medicine, Business, Arts, Design, Law)
2. **Explore careers** in that stream
3. **Find colleges in different countries** that fit their **yearly budget**

Built with beginner-friendly tools: **Python (Flask)**, **HTML** and **CSS**.

---

## 1. What's in this folder

All files sit together in one folder:

```
carre pointer/
├── app.py            ← the brain: decides which page to show and does the filtering
├── data.py           ← the toy box: streams, careers, colleges, quiz questions
├── requirements.txt  ← the shopping list of tools Python needs (just Flask)
├── base.html         ← the picture frame every page sits inside (top bar + footer)
├── index.html        ← home page
├── quiz.html         ← the quiz
├── result.html       ← quiz result + matching careers
├── careers.html      ← all careers, filter by stream
├── colleges.html     ← college finder (country + stream + budget)
├── style.css         ← the paint box: minimal, modern look with automatic dark mode
└── README.md         ← this guide
```

### How the pieces talk to each other (the 5-year-old version)
- The **visitor** knocks on a door, like `/colleges`.
- **app.py** hears the knock, looks in the **toy box (data.py)**, and picks the right toys.
- It hands the toys to an **HTML page**, which lays them out.
- **style.css** paints everything so it looks pretty.
- The finished page goes back to the visitor's screen.

---

## 2. Run it on your computer (Windows)

1. **Install Python**: go to https://www.python.org/downloads/ and install the latest Python 3.
   On the first install screen, **tick "Add python.exe to PATH"**.
2. **Install VS Code** (you already have it) and the **Python** extension.
3. Open the **carre pointer** folder in VS Code, then open a terminal (**Terminal → New Terminal**) and type these one at a time:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

They make a private space for this project's tools, step into it, install Flask, and start the website.

4. Open **http://127.0.0.1:5000** in your browser. 🎉

> If PowerShell says scripts are disabled, run this once:
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`

---

## 3. About the languages

| Language | What it does in Carrer Pointer | Why it's a good choice |
|---|---|---|
| **HTML** | The skeleton: titles, buttons, forms, cards | Easiest place to start; you see results instantly |
| **CSS** | The clothes: colours, spacing, dark mode, phone layout | Makes it look minimal and modern |
| **Python + Flask** | The brain: quiz scoring, filtering colleges by budget | Reads almost like English; huge community |
| **Java** | *Not used yet.* | See below |

**Java vs JavaScript:** they're two different languages with similar names.
- **Java** is great for big company back-ends (with a framework called Spring Boot) and Android apps, but it's harder for beginners than Python. You could rebuild the back end in Java later; it isn't needed now.
- **JavaScript** runs inside the browser and makes pages interactive without reloading. You don't need it for version 1. Add it later for things like live search, college comparison and charts.

---

## 4. Step-by-step plan (roadmap)

### Phase 0: Set up (Week 1)
- [ ] Install Python, VS Code, Git
- [ ] Create a free GitHub account and put this project on it (learn `git add`, `git commit`, `git push`)
- [ ] Run the site locally (section 2)

### Phase 1: Learn the basics (Weeks 1–6, about 1 hour a day)
- [ ] HTML + CSS basics, then rebuild one page of this site from scratch yourself
- [ ] Python basics: variables, lists, dictionaries, loops, functions
- [ ] Flask basics: routes, templates, forms
- [ ] Read through `app.py` and change something small, like adding a quiz question

### Phase 2: Grow the starter (Weeks 6–10)
- [ ] Add more colleges and careers in `data.py` (aim for 100+ colleges in 15+ countries)
- [ ] Add **living costs** next to tuition (rent + food), because the real budget is tuition **plus** living
- [ ] Add a **local currency** option: show fees in INR, EUR, NGN and so on, not only USD
- [ ] Add more quiz questions (8–12 makes for a better match)

### Phase 3: Real database (Weeks 10–14)
- [ ] Move data from `data.py` into **SQLite** (built into Python) using **Flask-SQLAlchemy**
- [ ] Build a simple admin page so your team can add or edit colleges without touching code
- [ ] Keep a "last checked" date on every fee, because fees change every year

### Phase 4: Accounts and saving (Weeks 14–18)
- [ ] Student sign-up and login (**Flask-Login**)
- [ ] "Save to my list" for colleges and careers
- [ ] Compare up to 3 colleges side by side

### Phase 5: Go live (Weeks 18–20)
- [ ] Put it online with **GitHub + Render** (see "Put it online" below)
- [ ] Buy a domain (for example `carrerpointer.com`) and connect it
- [ ] Add a privacy policy (required if you collect emails, especially from under-18s)

### Put it online (free)
1. **GitHub:** sign up at github.com, click **New repository**, name it `carrer-pointer`, set it to Public and create it.
   Click **uploading an existing file** and drag in every file from this folder **except** `.venv` and `__pycache__`, then click **Commit changes**.
2. **Render:** sign up at render.com with your GitHub account. Click **New → Web Service** and pick the `carrer-pointer` repo.
   - Language: **Python 3**
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
   - Instance Type: **Free**

   Click **Deploy**. After 2–3 minutes your site is live at `https://carrer-pointer.onrender.com` (or similar).
3. **Your own domain (optional, about $10/year):** buy one at Cloudflare Registrar, Namecheap or GoDaddy.
   In Render open your service, go to **Settings → Custom Domains → Add**, type your domain, and copy the DNS records Render shows into your domain seller's DNS settings. HTTPS is set up for you.
4. **Updating the site:** upload the changed files to GitHub again. Render redeploys automatically.

Note: on the free plan the site goes to sleep after 15 minutes with no visitors, and the next visit takes about a minute to wake it. The paid plan ($7/month) stays awake.

### Phase 6: Make it great (after launch)
- [ ] Pick ideas from section 6
- [ ] Ask 10 real students to use it and watch where they get confused
- [ ] Add JavaScript for smoother, no-reload filtering

---

## 5. Courses (all free unless marked)

### Start here
| Topic | Course | Where |
|---|---|---|
| Everything (big picture) | **CS50x: Introduction to Computer Science** (Harvard) | cs50.harvard.edu/x |
| HTML & CSS | **Responsive Web Design** certification | freecodecamp.org |
| HTML & CSS | **Learn Web Development** guides | developer.mozilla.org (MDN) |
| HTML, CSS, Git | **The Odin Project: Foundations** | theodinproject.com |
| CSS that looks good | **Kevin Powell** YouTube channel | youtube.com/@KevinPowell |

### Python
| Course | Where |
|---|---|
| **CS50P: Introduction to Programming with Python** (Harvard) | cs50.harvard.edu/python |
| **Python for Everybody** (Dr. Chuck) | py4e.com, or Coursera |
| **Automate the Boring Stuff with Python** (free book) | automatetheboringstuff.com |

### Flask (the web part of Python)
| Course | Where |
|---|---|
| **Official Flask Tutorial** | flask.palletsprojects.com |
| **The Flask Mega-Tutorial** (Miguel Grinberg) | blog.miguelgrinberg.com |
| **CS50x Week 9: Flask** | cs50.harvard.edu/x |

### Java (optional, for later)
| Course | Where |
|---|---|
| **Java Programming MOOC** (University of Helsinki) | java-programming.mooc.fi |
| **Spring Boot** guides (Java web back ends) | spring.io/guides |

### Also useful
| Topic | Course | Where |
|---|---|---|
| Databases / SQL | **SQLBolt** (interactive) | sqlbolt.com |
| Git & GitHub | **GitHub Skills** | skills.github.com |
| JavaScript (later) | **javascript.info** | javascript.info |
| Design basics | **Figma Learn** | help.figma.com |
| Design (paid) | **Refactoring UI** | refactoringui.com |

---

## 6. Ideas to add

**Money and budget**
- 💰 **True cost calculator**: tuition + rent + food + visa + flights = total per year
- 🎓 **Scholarship finder**: filter by country, stream, merit or need
- 💱 **Currency switcher**: see every price in your own currency
- 🧑‍💼 **Part-time work rules**: how many hours students may work in each country

**Getting in**
- 📝 **Exam guide**: which exams each country needs (SAT, IELTS/TOEFL, JEE, NEET, GRE, Gaokao, and others)
- 📅 **Deadline calendar**: application dates with email reminders
- 🛂 **Visa checklist** per country
- ✅ **Eligibility checker**: enter your marks and see which colleges you might qualify for

**Careers**
- 🗺️ **Career roadmaps**: Class 10 → stream → degree → first job, as a simple timeline
- 📊 **Salary and job demand** by country
- 🎥 **"A day in the life"**: short videos or stories from people in each job
- 🤝 **Mentor connect**: chat with university students or professionals

**Smart features**
- 🤖 **AI career counsellor**: a chatbot that asks questions and suggests streams
- ⚖️ **Compare colleges** side by side
- ⭐ **Student reviews** of colleges (with moderation)
- 🌍 **Multi-language site** (Hindi, Spanish, Arabic, French and more), since students are worldwide
- 👪 **Parent mode**: a simple summary for parents with costs and safety info
- ♿ **Accessibility**: large-text mode, screen-reader friendly, high contrast

**Where to get real college data**
- USA: **College Scorecard API** (free, official) at collegescorecard.ed.gov
- Germany: **DAAD international programmes database** at daad.de
- UK: **UCAS** course search
- Always link to the official college page, and show a "last checked" date on fees.
  Ranking sites (QS, THE) have licensing rules, so don't copy their data without permission.

---

## 7. Important notes
- The fees in `data.py` are **rough starting estimates** in USD per year for international undergraduates. They change every year and differ by course, so check each college's official site before you show them to real students.
- `debug=True` in `app.py` is for building only. Turn it off before going live.
