import cv2

def Cut_img():
    img = cv2.imread("img2.jpg")

    height, width = img.shape[:2]

    quentity_row = int(input('Quentity row: '))

    hight_el = round(height / quentity_row)
    sr, sc = 0, 0

    for i in range(quentity_row):
        el = img[sr:sr+hight_el, sc:width]
        cv2.imwrite(f'temp/{i}.png', el)
        sr = sr+hight_el
    return quentity_row

if __name__ == "__main__":
    Cut_img()