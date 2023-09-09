from PIL import Image


images = [
    Image.open("Users/Nabizzle/Desktop/images" + f)
    for f in ["image(0).jpg", "image(1).jpg", "image(2).jpg", "image(3).jpg", "image(4).jpg", "image(5).jpg", "image(6).jpg"]


]
pdf_path = "Users/Nabizzle/Desktop/images/WSL_Setup.pdf"

images[0].save(pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=[0:6])
