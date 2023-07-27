import cv2

from anime_face_detector import create_detector

from utils import draw_bbox, draw_one_point

detector = create_detector('yolov3')
image = cv2.imread('/home/data2/dongtrinh/DATASET/animeface256cleaner/animefaces256cleaner_Filtered_Set0/000000.jpg')
preds = detector(image)

for face in preds:
    image = draw_bbox(image, face['bbox'])
    for landmark in face['keypoints']:
        image = draw_one_point(image, landmark)

cv2.imwrite('save.jpg', image)