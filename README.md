# QR Data Reconstructor

## Description
This program was designed for Hak5's community latest QR Optical Exfiltration payloads, to ease the process of reconstructing the data.

## Installation
To install all dependencies, I have made a simple bash script to do it. It works with ```pip```. To download and install, first run ```su``` and then:
```
git clone https://github.com/Prodicode/qr-data-reconstruct.git
cd qr-data-reconstruct
chmod a+x setup.sh
./setup.sh
 ```

Then, you can just run it using python. Use the ```-h``` argument for help: ```python decoder.py -h```. Usage example:
```
python decoder.py input_video.mp4 output_data.txt
```
