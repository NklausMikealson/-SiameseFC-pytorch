import argparse

import cv2
import torch

from siamfc import TrackerSiamFC


def parse_args():
    """
    args for testing.
    """
    parser = argparse.ArgumentParser(
        description='PyTorch SiamFC Tracking Demo')
    parser.add_argument('--video', dest='video',
                        default='./test.mp4', help='video path')
    parser.add_argument('--model', dest='model',
                        default='pretrained/siamfc/model.pth', help='pretrained model')
    args = parser.parse_args()

    return args


def _x1y1wh_to_xyxy(bbox_x1y1wh):
    x1, y1, w, h = bbox_x1y1wh
    x2 = int(x1+w)
    y2 = int(y1+h)
    return x1, y1, x2, y2


def main(args):
    cap = cv2.VideoCapture(args.video)
    i = 0
    while(cap.isOpened):
        ret, frame = cap.read()
        if ret == True:
            img = frame
            if i == 0:
                # init the target
                # ROI Selection
                cv2.namedWindow("SiamFC", cv2.WND_PROP_FULLSCREEN)
                try:
                    init_rect = cv2.selectROI('SiamFC', img, False, False)
                    x, y, w, h = init_rect
                except:
                    exit()
                init_state = [x, y, w, h]
                trk = TrackerSiamFC(net_path=args.model)
                trk.init(img, init_state)
                i += 1
            else:
                # track the target
                pos = trk.update(img)
                pos = _x1y1wh_to_xyxy(pos)
                pos = [int(l) for l in pos]
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                cv2.rectangle(img, (pos[0], pos[1]),
                              (pos[2], pos[3]), (0, 255, 255), 3)
                # imshow
                cv2.namedWindow("SiamFC", cv2.WND_PROP_FULLSCREEN)
                cv2.imshow("SiamFC", img[:, :, (2, 1, 0)])
                cv2.waitKey(25)
                i += 1

    cap.close()


if __name__ == "__main__":
    args = parse_args()
    main(args)
