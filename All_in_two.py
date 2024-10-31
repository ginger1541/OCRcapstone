#easyOCR라이브러리 사용케이스

import easyocr
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 설정
font_path = "C:/Windows/Fonts/malgun.ttf"  # Windows의 맑은 고딕 폰트 경로
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

# 경고 제거
plt.rcParams['axes.unicode_minus'] = False

# EasyOCR Reader 객체 생성 (한글 인식 설정)
reader = easyocr.Reader(['ko'], gpu=True)  # GPU 사용 가능하면 gpu=True로 설정

# OCR을 수행할 이미지 파일 경로
image_path = r"C:\Users\user\Allimege\IMG_OCR_53_4PO_09605.png"

# OCR 수행
results = reader.readtext(image_path)

# 인식된 텍스트 출력
for bbox, text, confidence in results:
    print(f"텍스트: {text}, 신뢰도: {confidence}")

# 이미지와 인식 결과를 함께 시각화
def display_image_with_text(image_path, results):
    # 이미지 열기
    img = Image.open(image_path)
    plt.imshow(img)
    ax = plt.gca()

    # 인식된 텍스트 표시
    for bbox, text, confidence in results:
        (top_left, top_right, bottom_right, bottom_left) = bbox
        ax.plot(
            [top_left[0], top_right[0], bottom_right[0], bottom_left[0], top_left[0]],
            [top_left[1], top_right[1], bottom_right[1], bottom_left[1], top_left[1]],
            'r', linewidth=2
        )
        ax.text(top_left[0], top_left[1] - 10, text, fontsize=12, color='blue', bbox=dict(facecolor='yellow', alpha=0.5))
    plt.show()

# 인식 결과 시각화
display_image_with_text(image_path, results)
