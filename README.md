# Commute Control System (CCS)

This application can help organizations to improve physical security and commute controlling. CCS can recognize, log and store commutes from a camera real-time.

## Getting Started

Clone to Repo:
```
git clone https://github.com/euvel/ccs.git
```
### Prerequisites
Install requirements:

```
pip3 install -r requirements.txt
```
Put your Known persons Images on **imgdset** folder

### Running

Run :

```
python3 main.py
```
on other terminal you can see logs:
```
tail -f main.log
```

## Built With

* [face_recognition](https://pypi.org/project/face-recognition/) - Recognize and manipulate faces
* [OpenCV](https://pypi.org/project/opencv-python/) - Unofficial pre-built OpenCV packages for Python

## Authors

* **Mohammadreza Qojavand** - [Euvel](https://github.com/euvel)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details

