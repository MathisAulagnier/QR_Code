import qrcode
import argparse

def generateQR(URL='https://github.com/MathisAulagnier/QR_Code', bcol='white', size = 10):
    print('Génération du QR Code...')
    qr = qrcode.QRCode(
        version=1,
        box_size=size,
        border=5
    )
    print('loading...')

    qr.add_data(URL)
    qr.make(fit=True)
    img = qr.make_image(fill='black' , back_color=bcol)
    img.save('qr.png')
    print('Success !')
    print('QR Code généré !')

    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.set_defaults(url='https://github.com/MathisAulagnier/QR_Code', bcol='white', size=10)
    
    parser.add_argument("--url", type=str, help="URL à encoder dans le QR Code")
    parser.add_argument("--bcol", type=str, help="Couleur de fond du QR Code")
    parser.add_argument("--size", type=int, help="Taille du QR Code")
    
    args = parser.parse_args()
    generateQR(args.url, args.bcol, args.size)
