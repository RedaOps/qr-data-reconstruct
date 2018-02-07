#Author: Tudor Gheorghiu, Prodicode

import argparse;
import qrtools;
import cv2;
import os;
import numpy as np;
import progressbar;
import base64;

parser = argparse.ArgumentParser(description="QR Code data reconstructor - made by Tudor Gheorghiu, Prodicode");
parser.add_argument("video", help="Video file containing QR codes",
                    type=str);
parser.add_argument("output", help="The file to output the data to. (output is in base64)",
                    type=str)
args = parser.parse_args();

cap = cv2.VideoCapture(args.video);
qr = qrtools.QR();

print("""\


 .--. .--.   .---..   ..---.--.--.  .---..--.     .  .---.--.-- .--. .   .
:    :|   )  |     \ / |      |  |    |  |   )   / \   |    |  :    :|\  |
|    ||--'   |---   /  |---   |  |    |  |--'   /___\  |    |  |    || \ |
:  ( ;|  \   |     / \ |      |  |    |  |  \  /     \ |    |  :    ;|  \|
 `--`-'   `  '---''   ''    --'--'---''  '   `'       `'  --'-- `--' '   '

 by Tudor Gheorghiu


""");
print("Processing video frames...");
print("NOTE: This process requires time and resources. Please be patient.");
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1;
print("Processing "+str(total_frames)   +" frames!");
bar = progressbar.ProgressBar(maxval=total_frames, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
currentFrame = 0
tempData = "";
while(currentFrame <= total_frames):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Saves image of the current frame in jpg file
    cv2.imwrite("temp.jpg", frame);
    qr.decode("temp.jpg");
    if (tempData != qr.data):
        tempData = qr.data;
        open(args.output, "a").write(tempData);


    # To stop duplicate images
    bar.update(currentFrame);
    currentFrame += 1

# When everything done, release the capture
bar.finish();
os.remove("temp.jpg");
cap.release()
cv2.destroyAllWindows()
print("Data written to "+args.output);
