"""GPU 확인 스크립트"""
import subprocess
import sys


def check_gpu():
    """nvidia-smi로 GPU 상태 확인"""
    try:
        result = subprocess.run(
            ["nvidia-smi"],
            capture_output=True,
            text=True,
            check=True
        )
        print("GPU 감지됨:")
        print(result.stdout)
        return True
    except FileNotFoundError:
        print("nvidia-smi를 찾을 수 없음 (GPU 드라이버 미설치)")
        return False
    except subprocess.CalledProcessError as e:
        print(f"nvidia-smi 실행 실패: {e}")
        return False


if __name__ == "__main__":
    has_gpu = check_gpu()
    sys.exit(0 if has_gpu else 1)
