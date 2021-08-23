"""Converts colored images to greyscale using the method selected by the user.
Install dependencies:
  pip install docopt

Usage:
  main.py <video_path>
  main.py -h | --help

Arguments:
  <video_path>   Input video file path

Options:
  -h, --help  Show this help screen.
"""

import docopt
import cv2 as cv
import os


def main(video_path):
    name, ext = os.path.splitext(video_path)
    name = name + "_grey1"
    gray_video_path = name + ext
    # use extension .avi for xvid
    # gray_video_path = 'output.avi'
    print(gray_video_path)
    cap = cv.VideoCapture(video_path)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'mp4v')   # use xvid for .avi
    # enter appropriate fps and frame size
    out = cv.VideoWriter(gray_video_path, fourcc, 23.98, (1280, 720), False)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #write greyed frame
        out.write(frame)
        # cv.imshow('frame', frame)
        # key = cv.waitKey(1)
        # if key & 0xFF == ord('q'):  #pressing q will exit
            # break
        # if key % 256 == 27:    # pressing escape key will exit
            # break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    main(args['<video_path>'])
