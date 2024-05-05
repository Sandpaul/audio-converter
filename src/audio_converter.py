"""This module contains the definition for `audio_converter()`."""

import glob
import os

from pydub import AudioSegment as convert


def audio_converter(directory_path: str, from_format: str, to_format: str):
    """a function to convert audio files from one format to another.

    Args:
        directory_path (str): path to directory where files to be convertered are stored.
        from_format (str): format of files to be converted.
        to_format (str): format files are to be converted to.

    Raises:
        FromFormatFilesNotFoundError: if no files of given from_format are found in given directory_path.
    """
    songs = glob.glob(f"{directory_path}/*.{from_format}")

    if len(songs) == 0:
        raise FromFormatFilesNotFoundError(
            f"No {from_format} files found in {directory_path}"
        )

    for song in songs:
        song_name = os.path.splitext(song)[0]
        print(f"Converting {song_name.rsplit('/', 1)[-1]} from {from_format} to {to_format}...")
        destination = f"{song_name}.{to_format}"
        song = convert.from_file(song, format=from_format)
        song.export(destination, to_format)
        print(f"{song_name.rsplit('/', 1)[-1]} converted! 🎶")


class FromFormatFilesNotFoundError(Exception):
    """Catches instances where no files of given from_format are found in given directory_path."""
