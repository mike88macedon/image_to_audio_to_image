import cv2
import numpy as np
import scipy.io.wavfile


def start_video(cam_num):
    cap = cv2.VideoCapture(cam_num)
    while True:
        # grab frames
        ret, frame = cap.read()
        # get numpy array
        img_vector = np.asarray(frame)
        # write image pixels to audio
        scale_to_audio(img_vector)
        # continuous image render from camera
        cv2.imshow("CAMERA WINDOW", frame)
        # wait for keyboard interrupt
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()


def scale_to_audio(data):
    # create vector from image matrix
    flatten_arr = data.flatten()
    # persist the vector uint8 pixel data to wav format
    scipy.io.wavfile.write('test.wav', 44100, flatten_arr)
    # read persisted data from the wav back to numpy array
    rate, data_wav = scipy.io.wavfile.read('test.wav')
    # reshape the vector to 640x480 matrix with 3 channels [[1,2,3],[1,3,4]] (reconstructing the image from audio data)
    reshaped_arr = np.reshape(data_wav, (480, 640, 3))
    # display the reconstructed image
    cv2.imshow("RECREATED IMAGE FROM SOUND", reshaped_arr)


if __name__ == "__main__":
    start_video(0)
