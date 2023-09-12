import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
import matplotlib.pyplot as plt
def make_qrcode(data):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(data)
    img = qr.make_image(image_factory=StyledPilImage,module_drawer=RoundedModuleDrawer())
    # img.save("img/qrcode.png")
    # img = Image.open('img/qrcode.png', 'r')
    plt.imshow(img)
    plt.show()
if __name__=="__main__":
    make_qrcode("http://www.jingshibang.com//uploads//paper//file//1691587263//2023%E5%8C%97%E4%BA%AC%E4%B8%AD%E8%80%83%E7%9C%9F%E9%A2%98%E6%95%B0%E5%AD%A6%EF%BC%88%E6%95%99%E5%B8%88%E7%89%88%EF%BC%89.pdf")