

## <div align="center">Yolov5_Dropper_Detect</div>
Dropper detection of rail transit.





## <div align="center">Train Your Dataset</div>

<details open>
<summary>Install requirements</summary>


<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
python=3.7
matplotlib>=3.2.2
numpy>=1.18.5
opencv-python>=4.1.2
Pillow
PyYAML>=5.3.1
scipy>=1.4.1
torch>=1.7.0
torchvision>=0.8.1
tqdm>=4.41.0
tensorboard>=2.4.1
seaborn>=0.11.0
pandas
```

</details>

<details open>
<summary>Data preprocess</summary>
Convert video data into pictures:
<!-- $ sudo apt update && apt install -y libgl1-mesa-glx libsm6 libxext6 libxrender-dev -->

```bash
python data_preprocess/Video_to_picture.py
```

You can use labelimg to label pictures

In order to convert the .xml label marked by labelimg into .txt, you can run:

```bash
python data_preprocess/format_transformation.py
```

</details>



<details open>
<summary>Train on your dataset</summary>

```bash
data/dropper_detect.yaml    #Set your data distribution

models/yolov5_dropper_detect.yaml  #c: set number of classes

python train.py --img 640 --batch 16 --epochs 300 --data ./data/dropper_detect.yaml --cfg ./models/yolov5_dropper_detect.yaml --weights ./weights/yolov5s.pt --device 1 #You can change to a, B and C models. You need to download the pretraining weights yourself.
```





</details>

<details>
<summary>Detect</summary>

```bash
python detect.py --source ./data/images/  --weights ./weights/best.pt --output inference/output/1_img/ --device 1
```



</details>  


