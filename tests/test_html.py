import sys
from imu.video import *
from imu.io import writeTxt

def test_shot_detection():
    fn = '../biomed/umb/'
    out = html_shot(frame_name = 'im_every1/%04d.png',\
                   file_result = './shot.js', frame_fps=1)
    writeTxt(fn + 'shot_detection.html', out.getHtml())


if __name__ == "__main__":
    # python tests/test_html.py 0
    opt = sys.argv[1]
    if opt == '0':
        test_shot_detection()
