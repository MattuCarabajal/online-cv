import qrcode
import qrcode.image.svg

def create_vcard():
    vcard_data = '''BEGIN:VCARD
    VERSION:4.0
    N:Maretto;Matías;
    FN:Matías Ezequiel Maretto
    TITLE:Automation Developer Engineer / Python Developer
    TEL;TYPE=home,voice;VALUE=uri:tel:+54-11-3118-3146
    URL:https://matias-maretto.herokuapp.com/
    EMAIL:matias.maretto@gmail.com
    BDAY:19921227
    REV:20220801T220000Z
    END:VCARD
    '''

    factory = qrcode.image.svg.SvgPathImage
    factory.QR_PATH_STYLE = {
        'fill': '#b0b0b0',
        'fill-opacity': '1',
        'fill-rule': 'nonzero',
        'stroke': 'none'
    }
    svg_img = qrcode.make(
        vcard_data,
        image_factory=factory,
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        border=2
    )
    svg_img.save('src/static/images/qr_add_me.svg')


if __name__ == '__main__':
    create_vcard()

# from qrcode.image.styledpil import StyledPilImage
# from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
# from qrcode.image.styles.colormasks import SolidFillColorMask

# print('Starting png qr')
# qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H,
#                    border=1,
#                    box_size=50)
# qr.add_data(vcard_data)
# qr.make(fit=True)
# print('Data added')

# print('About to save png')
# img_1 = qr.make_image(image_factory=StyledPilImage,
#                       module_drawer=RoundedModuleDrawer(),
#                       color_mask=SolidFillColorMask(back_color=(34,35,39),
#                                                     front_color=(176,176,176)))
# img_1.save("src/static/images/qr_1.png")
# print('PNG saved')
