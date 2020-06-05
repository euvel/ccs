#!/usr/bin/env python3
""" Commute Control System (CCS)
        This application can help organizations to improve physical security
        and commute controlling.
"""

__author__ = "Mohammadreza Qojavand"
__version__ = "1.0.7"
__license__ = "MIT"

import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import face_recognition
import numpy as np
import os



def main():
    # Check Log file
    log.basicConfig(filename='main.log',level=log.INFO)

    # Get webcam #0
    video_capture = cv2.VideoCapture(0)

    # If webcam not responds
    #while True:
    #    if not video_capture.isOpened():
    #        print('Unable to load camera.')
    #        sleep(5)
    #        pass

    # Get Known Images
    knownImages_path = './imgdset'
    knownImages = []
    for r, d, f in os.walk(knownImages_path):
        for file in f:
            if '.jpg' in file:
                knownImages.append(os.path.join(r, file))

    # Initialize needed variables
    known_face_names = []
    known_face_encodings = []

    # Get known persons name and face encodings
    for img in knownImages:
        img_file = face_recognition.load_image_file(img)
        img_enc = face_recognition.face_encodings(img_file)[0]
        known_face_encodings.append(img_enc)
        known_face_names.append(img.replace("./imgdset/","").replace(".jpg", ""))

    # Initialize needed variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Get a single frame of video
        ret, frame = video_capture.read()

        # Resize frame to 0.25 size for making recognition process faster
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert Opencv RGB to face_recognition RGB
        rgb_small_frame = small_frame[:, :, ::-1]

        # process every frame seporately !
        if process_this_frame:
            # Find faces and faces encodings in the frame
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # Got matches
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                #print(matches)
                name = "Unknown"
                # use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame


        # Make Results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face 0.25 to real
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a fucking box
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 200, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 0, 0), 1)
            # log commute in main.log file
            log.info(" [*] faces: "+str(name)+" at "+str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

        # Show Results
        cv2.imshow('Video', frame)

        # Define `q` to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean Up!
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
