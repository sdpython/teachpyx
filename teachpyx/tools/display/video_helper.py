import os
from typing import Any, List, Optional, Tuple


def get_local_folder(file_or_folder, name="temp_video") -> str:
    """
    Creates or cleans a local folder create in the same folder as
    `file_or_folder`.
    """
    if os.path.isfile(file_or_folder):
        file_or_folder = os.path.dirname(file_or_folder)
    fullname = os.path.join(file_or_folder, name)
    if os.path.exists(fullname):
        for n in os.listdir(fullname):
            os.remove(os.path.join(fullname, n))
    else:
        os.mkdir(fullname)
    return fullname


def make_video(
    images: List[str],
    outvid: str,
    fps: int = 5,
    size: Optional[Tuple[int, int]] = None,
    is_color: bool = True,
    format: str = "XVID",
) -> Any:  # VideoWriter
    """
    Creates a video from a list of images with opencv.

    :param outvid: output video
    :param images: list of images to use in the video
    :param fps: frames per second
    :param size: size of each frame
    :param is_color: color
    :param format: see `fourcc <http://www.fourcc.org/codecs.php>`_
    :return: `VideoWriter <https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html>`_

    The function relies on `opencv <https://docs.opencv.org/4.x/>`_.
    By default, the video will have the size of the first image.
    It will resize every image to this size before adding them to the video.
    """
    if len(images) == 0:
        raise ValueError("No image to convert into a video.")
    from cv2 import (
        VideoWriter,
        VideoWriter_fourcc,
        imread,
        resize,
    )  # pylint: disable=E0401

    fourcc = VideoWriter_fourcc(*format)
    vid = None
    for image in images:
        if not os.path.exists(image):
            raise FileNotFoundError(image)
        img = imread(image)
        if vid is None:
            if size is None:
                size = img.shape[1], img.shape[0]
            vid = VideoWriter(outvid, fourcc, float(fps), size, is_color)
        if size[0] != img.shape[1] and size[1] != img.shape[0]:
            img = resize(img, size)
        vid.write(img)
    vid.release()
    return vid
