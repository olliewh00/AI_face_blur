# 👤 Real-Time Face Blur for Privacy

A practical and simple computer vision application built with Python and OpenCV that detects human faces in a live webcam feed and applies a strong Gaussian blur to protect identity in real time.

## ✨ Features

* **Real-Time Processing:** Processes video frames instantly using a live webcam feed.
* **Haar Cascade Detection:** Utilizes OpenCV's highly efficient Haar Cascade Classifiers for accurate and fast frontal face detection.
* **Privacy Protection:** Applies a strong, non-reversible Gaussian blur to the detected Region of Interest (ROI) for privacy.
* **Simple Interface:** Runs in a dedicated OpenCV window and exits cleanly with the press of the 'q' key.

## 🛠️ Prerequisites

Before running the application, ensure you have the following installed on your system:

1. **Python 3.x**
2. **OpenCV (cv2):** This library handles all video input, image manipulation, and face detection.

## 🚀 Installation and Setup

Follow these steps to get your local copy up and running:

### 1\. Clone the Repository

Clone the project repository to your local machine using the following command:

```
git clone https://github.com/olliewh00/AI_face_blur.git
cd face-blur-app
```

### 2\. Install Dependencies

Install the required library using pip:

```
pip install opencv-python
```

### 3\. Locate the Cascade Classifier

The script relies on the pre-trained Haar Cascade XML file, which is usually installed with the `opencv-python` package. The provided script automatically uses the path provided by `cv2.data.haarcascades`. If you encounter an error (e.g., "Could not load face cascade"), you might need to manually verify the path to the `haarcascade_frontalface_default.xml` file on your system.

## 💻 Usage

To start the real-time face blur application, run the script from your terminal:

```
python face_blur.py
```

1. A new window titled `Real-Time Face Blur` will open.
2. The application will automatically attempt to connect to your default webcam (index `0`).
3. Any face detected will instantly appear blurred in the output window.

### Exiting the Application

Press the **`q`** key while the OpenCV window is focused to stop the camera stream and close the program.

## ⚙️ How It Works (The Tech Stack)

1. **Haar Cascade:** The script loads the `haarcascade_frontalface_default.xml` file, which is a machine-learning based approach used for object detection. It is trained to identify specific features (like the edges of eyes, nose, and mouth) that characterize a human face.
2. **Frame Detection:** In the main loop, each incoming frame is converted to grayscale to improve processing speed and detection accuracy.
3. **Bounding Box:** The detector returns a set of coordinates `(x, y, w, h)` defining a rectangular bounding box around each detected face.
4. **Applying the Blur:** This bounding box is used as a Region of Interest (ROI). The `cv2.GaussianBlur()` function is applied to the ROI with a very large kernel size (`99, 99`) and high sigma value (`30`), resulting in a heavy blur that successfully anonymizes the face before the frame is displayed.