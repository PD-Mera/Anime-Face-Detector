import cv2

def draw_one_point(img, landmark_point_data, thres = 0.5):
    if landmark_point_data[2] >= thres:
        img = cv2.circle(img, (int(landmark_point_data[0]), int(landmark_point_data[1])), radius=2, color=(0, 0, 255), thickness=2)
    return img

def draw_bbox(img, bbox_data, thres = 0.5):
    if bbox_data[4] >= thres:
        img = cv2.rectangle(img, (int(bbox_data[0]), int(bbox_data[1])), (int(bbox_data[2]), int(bbox_data[3])), color=(255, 0, 0), thickness=2)
    return img