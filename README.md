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

For collect known faces run:
```
python3 collect.py
```
Type person name and wait to get capture of known face, press 's' to save and exit.


### Running

Run :

```
python3 main.py
```

press 'q' to exit.

On other terminal you can see logs:
```
tail -f main.log
```

## Built With

* [face_recognition](https://pypi.org/project/face-recognition/) - Recognize and manipulate faces
* [OpenCV](https://pypi.org/project/opencv-python/) - Unofficial pre-built OpenCV packages for Python

## Authors

* **Mohammadreza Qojavand** - [Euvel](https://github.com/euvel)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
