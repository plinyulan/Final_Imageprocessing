from PIL import Image

# 1. ระบุชื่อไฟล์ภาพที่คุณต้องการครอป
image_path = 'FinalDIP67.bmp'
# 2. ระบุชื่อไฟล์ที่จะบันทึกภาพที่ครอปแล้ว
cropped_image_path = 'rectifyandcrop.bmp'

# 3. เปิดไฟล์ภาพ
try:
    img = Image.open(image_path)
except FileNotFoundError:
    print(f"ไม่พบไฟล์: {image_path}")
    exit()

# ดูขนาดเดิมของภาพ (กว้าง, สูง)
width, height = img.size
print(f"ขนาดภาพต้นฉบับ: กว้าง {width} พิกเซล, สูง {height} พิกเซล")

# 4. กำหนดพิกัดสำหรับครอป 
left = width // 5      
upper = height // 4    
right = 3 * width // 4  
lower = 3 * height // 4 


# crop_box = (100, 50, 400, 300) 
# จะครอปภาพจากพิกัด (100, 50) ถึง (400, 300)

crop_box = (left, upper, right, lower)
print(f"พิกัดครอป (left, upper, right, lower): {crop_box}")

# 5. ใช้ฟังก์ชัน .crop() เพื่อครอปภาพ
cropped_img = img.crop(crop_box)

# 6. บันทึกภาพที่ครอปแล้ว
cropped_img.save(cropped_image_path)

print(f"ครอปภาพเสร็จสมบูรณ์ และบันทึกเป็น: {cropped_image_path}")

