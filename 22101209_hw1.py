import cv2 as cv
import numpy as np


def main():
    video = cv.VideoCapture(0)
    if not video.isOpened():
        print("카메라를 이용할 수 없습니다.")
        return

    # 프레임 너비, 높이, FPS 정보 가져오기
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv.CAP_PROP_FPS)
    if fps == 0.0:
        fps = 24.0  # FPS를 가져오지 못할 경우 기본값 24.0 적용
    wait_msec = int(1 / fps * 1000)

    # cv.VideoWriter를 이용해 동영상 파일 생성
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    out = cv.VideoWriter('output.mp4', fourcc, fps, (width, height))

    is_recording = False

    is_flipped = False
    # 영상 녹화중, 상하 반전 여부 확인을 위해 False 값으로 변수 선언

    brightness = 0
    brightness_level = 10
    # 영상 상하 반전 및 밝기 조절 기능

    print("=== Video Recorder 시작 ===")
    print("[ESC]: 프로그램 종료")
    print("[SPACE]: Preview / Record 모드 변환")
    print("['f']: 영상 상하 반전")
    print("[ [ ] : 밝기 감소")
    print("[ ] ] : 밝기 증가")

    while True:
        val, frame = video.read()
        if not val:
            print("프레임을 읽을 수 없습니다.")
            break

        if is_flipped:
            frame = cv.flip(frame, 0)  # 0: 상하 반전

        if brightness != 0:
            frame_tran = 1.0 * frame + brightness

            frame_tran[frame_tran < 0] = 0
            frame_tran[frame_tran > 255] = 255
            # 밝기의 범위 밖인 경우에 대비

            frame = frame_tran.astype(np.uint8)

        if is_recording:
            out.write(frame)

        display_frame = frame.copy()

        if is_recording:
            cv.circle(display_frame, (width - 50, 50), 20, (0, 0, 255), -1)
            cv.putText(display_frame, "REC", (width - 120, 60),
                       cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 0, 255), 2)
        else:
            cv.putText(display_frame, "Preview", (width - 130, 60),
                       cv.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 2)

        cv.imshow('Video Recorder', display_frame)

        key = cv.waitKey(wait_msec)

        if key == 27:  # ESC 키로 프로그램 종료
            break
        elif key == ord(' '):  # Space 키로 모드 변환
            is_recording = not is_recording
            if is_recording:
                print("녹화 시작")
            else:
                print("녹화 중지")
        elif key == ord('f') or key == ord('F'):
            is_flipped = not is_flipped
            print(f"상하 반전 모드: {'ON' if is_flipped else 'OFF'}")
            # f 키를 이용하여 상하 반전

        elif key == ord('['):
            brightness -= brightness_level
            print(f"현재 밝기: {brightness}")
        elif key == ord(']'):
            brightness += brightness_level
            print(f"현재 밝기: {brightness}")
            # [, ] 키를 이용하여 밝기 조절

    video.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()