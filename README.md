🎨 Virtual Paint - My first OPENCV Project

Bring your creativity to life with Virtual Paint, a computer vision project that lets you draw in real time using colored objects as your brushes.
This project uses OpenCV and NumPy to track colors in front of a webcam and create digital paintings interactively.

🚀 Features

🖌️ Draw with real objects – Use colored objects (Orange, Purple, Green, Blue) as virtual brushes.

🎯 Color tracking in HSV – Robust detection across varying lighting conditions.

🔗 Continuous strokes – Connects detected points into smooth lines.

🎨 Multiple colors – Switch colors instantly by changing the object.

🔄 Live feed with overlay – See your drawing in real time on the webcam feed.

🧹 (Optional) Clear canvas or extend functionality for erasing.

🛠️ Tech Stack

Language: Python

Libraries: OpenCV, NumPy


🧑‍💻 How It Works

Webcam Capture
Captures live video frames with OpenCV.

Color Detection
Converts the frame to HSV color space and applies masks for defined color ranges.

myColors = [
    [10, 150, 150, 25, 255, 255],   # Orange
    [125, 50, 50, 155, 255, 255],  # Purple
    [40, 50, 50, 80, 255, 255],    # Green
    [100, 150, 50, 140, 255, 255]  # Blue
]


Contour Detection
Finds object contours and determines the center point.

Drawing on Canvas
Stores detected points and draws continuous strokes in the chosen color.

📦 Installation

Clone the repo:

git clone https://github.com/your-username/virtual-paint.git
cd virtual-paint


Install dependencies:

pip install opencv-python numpy


Run the project:

python virtual_paint.py


Press q to exit.

⚙️ Customization

🎨 Add new colors → extend myColors and myColorValues.

✏️ Change stroke thickness → edit cv2.line thickness in drawOnCanvas().

🖼️ Save your drawings → add cv2.imwrite() to capture the final canvas.

🔮 Future Enhancements

🧹 Eraser tool support.

🖼️ Option to save/load drawings.

🎤 Voice commands for switching colors.

✋ Gesture-based controls with Mediapipe.

🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit pull requests for new features, bug fixes, or optimizations.

📜 License

This project is licensed under the MIT License – see the LICENSE
 file for details.

💡 Inspiration

This project is inspired by interactive AR-based drawing applications and OpenCV tutorials. 
