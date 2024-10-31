#Tesseract 사용 케이스 
from PIL import Image
import pytesseract
import cv2
# 이미지 흑백 처리
img = cv2.imread('handwritten_korean.png', cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)



# Tesseract 경로 설정 (Windows 사용자의 경우)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 한글 인식 설정
config = '--oem 3 --psm 6 -l kor'

# 이미지 불러오기
image_path = r"C:\Users\user\OneDrive\바탕 화면\OCRcapstone\IMG_OCR_53_4PO_09605.png"
img = Image.open(image_path)

# OCR 인식
text = pytesseract.image_to_string(img, config=config)
print("인식된 텍스트:")
print(text)

