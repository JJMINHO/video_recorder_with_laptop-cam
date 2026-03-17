# video_recorder_with_laptop-cam
This is a vedio record tool using your laptop camera. Also, You can use a rtsp address!

# My Video Recorder 🎥

OpenCV를 활용하여 제작한 파이썬 기반의 간단한 비디오 레코더 프로그램입니다.

## 📌 프로그램 개요
이 프로그램은 컴퓨터의 웹캠 또는 외부 IP 카메라(CCTV)의 스트리밍 주소를 입력받아 실시간으로 화면에 출력하고, 사용자의 조작에 따라 원하는 구간을 `.mp4` 동영상 파일로 녹화하여 저장하는 기능을 제공합니다.

## ✨ 주요 기능

### 1. 필수 기능 (Essential Features)
* **다양한 소스 지원:** 터미널 입력을 통해 기본 웹캠(`0`)뿐만 아니라 외부 네트워크 카메라(RTSP/HTTP 등) 영상도 불러올 수 있습니다.
* **Preview / Record 모드 지원:** 영상을 단순히 확인만 하는 Preview 모드와 실제 파일로 기록되는 Record 모드를 분리하였습니다.
* **UI 피드백:** Record 모드 진입 시 화면 우측 상단에 붉은색 원과 `REC` 텍스트가 표시되어 녹화 상태를 직관적으로 확인할 수 있습니다.
* **동영상 저장:** 녹화된 영상은 `mp4v` 코덱을 사용하여 `output.mp4` 파일로 안전하게 저장됩니다.

### 2. 추가 기능 (Extra Features)
강의에서 다룬 기하학적 편집(Geometric editing)과 광도 편집(Photometric editing) 기법을 활용하여 **두 가지 실시간 필터 기능**을 추가로 구현했습니다.

* **상하 반전 필터 (Flip):** * `f` 키를 누르면 OpenCV의 `cv.flip()` 함수를 이용하여 영상이 상하로 즉각 반전됩니다.
* **소프트웨어 밝기 조절 (Intensity Transformation):** * `[` 와 `]` 키를 눌러 영상의 밝기 값을 동적으로 조절할 수 있습니다. 
  * 변환 공식 $I^{\prime}= 1.0 \times I + \beta$ 을 소프트웨어적으로 적용하였으며, 연산 과정에서 발생할 수 있는 오버플로우/언더플로우 방지(Saturate values) 로직을 포함하여 값이 $0 \sim 255$를 벗어나지 않도록 안전하게 구현했습니다.

## ⌨️ 단축키 및 조작 방법 (Controls)

| 단축키 | 기능 설명 |
| :---: | :--- |
| `SPACE` | **녹화 시작 / 중지** (Preview ↔ Record 모드 전환) |
| `ESC` | **프로그램 완전 종료** 및 파일 저장 |
| `f` 또는 `F` | **[추가 기능]** 영상 상하 반전 (Toggle) |
| `[` | **[추가 기능]** 영상 밝기 감소 (-10) |
| `]` | **[추가 기능]** 영상 밝기 증가 (+10) |

## 📸 실행화면 및 결과 (Screenshots)

저장소의 output.mp4 파일이 결과물입니다!

## 🚀 실행 방법 (How to Run)
1. Python 환경에 OpenCV 라이브러리가 설치되어 있어야 합니다.
   ```bash
   pip install opencv-python numpy
