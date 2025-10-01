# Magic Pen 🎨🖐️

![Python](https://img.shields.io/badge/Python-3.12-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-lightgrey)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Hands-orange)
![GitHub](https://img.shields.io/badge/GitHub-Repo-black)
![License](https://img.shields.io/badge/License-MIT-green)

A fun **virtual paint application** built with **OpenCV** and **MediaPipe Hands**.
Use your fingers as paintbrushes on a live webcam feed:

* ✋ **Index finger** → Thin brush (white)
* 🖐️ **Middle finger** → Medium brush (white)
* 🤌 **Pinky finger** → Thick brush (white) / Eraser
* 🎨 On-screen **color palette** to pick colors


## 🚀 Features

✅ Real-time hand tracking with MediaPipe
✅ Multiple brush sizes based on fingers
✅ Eraser with pinky finger
✅ Interactive color palette
✅ Webcam-powered digital canvas


## 🎮 Controls

* `c` → Clear the canvas
* `Esc` → Exit the app


## ⚙️ Installation

```bash
pip install opencv-python mediapipe
```

Clone the repository:

```bash
git clone https://github.com/YourUsername/magic-pen.git
cd magic-pen
```

Run the app:

```bash
python paint.py
```


## 📂 Folder Structure

```
magic-pen/
│
├── paint.py                     # Main application  
├── requirements.txt             # Python dependencies  
├── .gitignore                   # Ignore unnecessary files  
├── README.md                    # Project documentation  
└── saved_images/                # Optional folder to store saved drawings
```


## 📸 Demo Screenshot / Video

**Screenshot**
![Demo Screenshot](images/demo_screenshot.jpg)

**Video**
[Watch Demo Video](media/demo_video.mp4)


## 🧑‍💻 Technologies & Libraries

* **Python 3.12**
* **OpenCV** – Real-time canvas rendering and input handling
* **MediaPipe Hands** – Hand detection and tracking
* **NumPy** – Efficient array handling for drawing


## 🔮 Next Steps / Improvements

* Add **custom brush shapes and textures**
* Keyboard shortcuts for faster color/brush switching
* Save multiple formats (PNG, JPEG) with timestamps
* Add **GUI** using Tkinter or PyQt for more interactive controls


## 🙏 Acknowledgements

* **OpenCV** – Image processing and GUI
* **MediaPipe** – Hand tracking framework
* Tutorials and inspiration from Python virtual paint projects


## 📜 License

This project is licensed under the **MIT License** — see [LICENSE](LICENSE) for details.



