import os
from PIL import Image

def create_exact_size_image(input_img, output_img, target_mb):
    target_bytes = target_mb * 1024 * 1024
    
    current_size = os.path.getsize(input_img)
    source_img = input_img
    temp_img = "temp_kucuk.jpg"
    
    if current_size > target_bytes:
        img = Image.open(input_img)
        img.save(temp_img, "JPEG", quality=25)
        source_img = temp_img 
            
    with open(source_img, 'rb') as f:
        data = f.read()
            
    padding = b'\x00' * (target_bytes - len(data))
    
    with open(output_img, 'wb') as f:
        f.write(data)
        f.write(padding)
        
    if source_img == temp_img and os.path.exists(temp_img):
        os.remove(temp_img)
        
    print(f"{output_img} başarıyla oluşturuldu! Tam Boyut: {os.path.getsize(output_img):,} bayt")

orijinal_dosya = "original_image.jpg" 

create_exact_size_image(orijinal_dosya, "image_1mb.jpg", 1)
create_exact_size_image(orijinal_dosya, "image_5mb.jpg", 5)
create_exact_size_image(orijinal_dosya, "image_10mb.jpg", 10)