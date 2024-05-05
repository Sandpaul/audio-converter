"""This module contains the test suite for `audio_converter()`."""

import glob
import os
import pathlib

import pytest

from src.audio_converter import audio_converter, FromFormatFilesNotFoundError


@pytest.fixture()
def test_files_path():
    return f"{pathlib.Path(__file__).parent.resolve()}/test_files/"


@pytest.mark.describe("audio_converter()")
@pytest.mark.it("should convert multiple audio files and save in same directory")
def test_multiple_audio_files(test_files_path):
    audio_converter(test_files_path, "m4a", "mp3")
    files = glob.glob(f"{test_files_path}/*")
    assert len(files) == 4
    assert f"{test_files_path}test_song_1.mp3" in files
    assert f"{test_files_path}test_song_2.mp3" in files
    os.remove(f"{test_files_path}test_song_1.mp3")
    os.remove(f"{test_files_path}test_song_2.mp3")


@pytest.mark.describe("audio_converter()")
@pytest.mark.it(
    "should raise FromFormatFilesNotFoundError when passed invalid file type"
)
def test_invalid_file_type(test_files_path):
    with pytest.raises(FromFormatFilesNotFoundError):
        audio_converter(test_files_path, "mp3", "mp3")
