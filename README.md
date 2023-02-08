# Anime Face Detector

This project use pretrained model from repo [hysts/anime-face-detector](https://github.com/hysts/anime-face-detector) to detect faces and landmarks from anime image

## Environments and Libraries

- ~~Python 3.10.9~~ (I try this but got error `No module named 'lib2to3'` because of deprecation on Python 3.10)
- Python 3.9.16

Clone and install repo

``` bash
pip install -r requirements.txt
mim install mmcv-full
mim install mmdet
mim install mmpose

git clone https://github.com/hysts/anime-face-detector.git
cd anime-face-detector
pip install -e . # it take 10+ min to build mmcv-full
cd ..
```

## Inference

Simply run:

``` bash
python infer.py
```

## Inference Result

| Image | Result |
|:---:|:---:|
| ![image](./assets/test.jpg "result") | ![result](./assets/result.jpg "result") |

