# Helmet Detection System using YOLOv5 & FastAPI

A real-time helmet detection web application using **YOLOv5**, **FastAPI**, and **React**. This project detects helmets in images uploaded by users and returns detection results with bounding boxes and class labels.

## Project Overview

This project uses a **YOLOv5** model trained to detect helmets in motorcycle rider images. The backend is built with **FastAPI** for quick image processing, and the frontend is built with **React** to handle user interactions, image uploads, and display detection results.

### Key Features:
- 🚀 **Real-time Helmet Detection** using YOLOv5.
- 🌐 **Frontend** built with React to upload images and display results.
- 🔥 **FastAPI Backend** to handle inference and return results.
- 📦 **Bounding Boxes** drawn on the uploaded image with detection confidence.

## Tech Stack

- **Backend**: FastAPI (for handling image uploads and inference)
- **Model**: YOLOv5 (Custom trained helmet detection model)
- **Frontend**: React (for building a user-friendly UI)
- **Libraries**: PyTorch, OpenCV, Pillow, etc.
- **Deployment**: Local development (can be deployed to any cloud platform like AWS, Heroku, etc.)

## Setup Instructions

### Prerequisites

1. **Python 3.13.3** (for the backend)
2. **Node.js 14+** (for the frontend)

Slow Detection
The detection process may be slow, especially on CPU. For faster performance, consider running the model on GPU.

Future Enhancements
Add confidence filtering to ignore low-confidence predictions.

Allow multiple image uploads and batch processing.

Deploy the app to the cloud (AWS, Heroku, etc.).

Add helmet safety tips using AI/LLM based on the detection results.

Integrate with webhooks for automated actions based on helmet detection.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
YOLOv5: A state-of-the-art object detection model.

FastAPI: A modern, fast (high-performance) web framework for building APIs with Python.

React: A JavaScript library for building user interfaces.
