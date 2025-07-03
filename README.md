# ⏱️ Screen Time Tracker (Python)

A Python script to **track your real-time screen usage**, detect idle time, and generate a **per-app screen time summary**.

Built using `pygetwindow`, `pynput`, and `time`.

---

## 📦 Features

- 🎯 Tracks time spent on each application window
- 💤 Ignores idle time if no input is detected for 10+ seconds (unless a video is playing)
- 📺 Smart detection for video apps (YouTube, Netflix, Hotstar, etc.)
- 🧠 Lightweight & runs in the terminal
- 🛑 Exit cleanly by pressing **ESC** inside **Visual Studio Code**
- 📊 Prints a readable time summary at the end

---

## 🚀 How to Run

### 1. Install required libraries

```bash
pip install pygetwindow pynput
