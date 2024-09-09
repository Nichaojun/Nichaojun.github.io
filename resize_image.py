from PIL import Image

# 加载本地图片
image_path = "images/1.1.jpg"
img = Image.open(image_path)

# 调整图片大小为320x320
img_resized = img.resize((320, 320))

# 保存调整大小后的图片
resized_image_path = "images/1.2.jpg"
img_resized.save(resized_image_path)

print(f"调整后的图片已保存到 {resized_image_path}")
