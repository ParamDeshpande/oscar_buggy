"""yolo v3 opencv implementation
input image shape( add here)
resize the image to (608,608,3)"""


'''todo: optimize the function, instead of calling readNet for each frame, pass it to function'''
'''todo: filter objects bases on labels'''
'''to run code, uncomment cv2.imshow and comment return function'''

import numpy as np
import cv2

def yolo_v3_opencv(frame):
    size = (608,608)
    confidence_threshold = 0.5
    nms_threshold = 0.6
    class_ids = []
    confidences = []
    boxes = []
    area = []
    centers = []
    labels = []
    classes = []
    net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg')
    with open(os.getcwd() + 'coco_classes.txt', 'r') as f:
        classes = [line.strip() for line in f.readlines()]
    layer_names = net.getLayerNames()
    outputLayers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
    img = frame
    img = cv2.resize(img, size)
    height, width, channels = img.shape
    blob = cv2.dnn.blobFromImage(img,1/255,size,(0,0,0),True,crop = False)
    net.setInput(blob)
    outs = net.forward(outputLayers)
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                # cv2.circle(img,(center_x,center_y),10,(0,255,0),2)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                # cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, score_threshold=confidence_threshold, nms_threshold= nms_threshold)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            area.append((w * h) / (width * height))
            label = str(classes[class_ids[i]])
            labels.append(label)
            # color = colors[i]
            centers.append([x, y])
            #cv2.rectangle(img, (x, y), (x + w, y + h), 2)  # color,2)
            #cv2.putText(img, label, (x, y + 30), font, 1, (255, 255, 255), 2)
    return area, centers, labels
    #cv2.imshow("Image", img)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
if __name__ == '__main__':
    pass
