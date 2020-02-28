# SiameseFC-pytorch
## Introduction

This repo is the expansion work for [SiameseFC](https://github.com/huanglianghua/siamfc-pytorch). Although the origin code is a clear implementation of SiamFC, it does not provide the demo program for us. It is significant to use a demo program to see the tracking result in the arbitrary video. So, I write this repo to provide the expansion demo program. You can set the any target in your video.

The origin paper you can see in [here](https://www.robots.ox.ac.uk/~luca/siamese-fc.html)

## Prepared

This repo need to install those dependencies:

```bash
opencv-python
torch
got10k
```

I recommend the got-10k toolkit for you to implement or evaluate your SOT code, you can go [here](https://github.com/got-10k/toolkit) to know this toolkit.

You can use this code to install those dependencies:

```bash
pip install XXX
```

## Demo

1. Clone this repo in your computer

   ```bash
   git clone https://github.com/NklausMikealson/SiameseFC-pytorch.git
   ```

   

2. Put your video in this repo

3. Run:
   ```bash
   python demo.py [./your/video/path]
   ```


## Evaluate the tracker in dataset

The got-10k toolkit provide 7 tracking datasets  ([OTB (2013/2015)](http://cvlab.hanyang.ac.kr/tracker_benchmark/index.html), [VOT (2013~2018)](http://votchallenge.net), [DTB70](https://github.com/flyers/drone-tracking), [TColor128](http://www.dabi.temple.edu/~hbling/data/TColor-128/TColor-128.html), [NfS](http://ci2cv.net/nfs/index.html) and [UAV123](https://ivul.kaust.edu.sa/Pages/pub-benchmark-simulator-uav.aspx)) to evaluate your code.

in the root directory of repo:

Run:

```
python test.py
```

You can choose the evaluate dataset in test.py

## Training this tracker

1. Download the dataset at `./data/[your-dataset-name]`.

2. Run:

   ```bash
   python train.py
   ```

   

