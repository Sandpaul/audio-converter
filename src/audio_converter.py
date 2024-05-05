from pydub import AudioSegment as convert

import glob
import os

def audio_converter(directory_path: str, from_format: str, to_format: str):

    songs = glob.glob(f"{directory_path}/*.{from_format}")

    for song in songs:
        song_name = os.path.splitext(song)[0]
        print(f"Converting {song_name} from {from_format} to {to_format}...")
        destination = f"{song_name}.{to_format}"
        song = convert.from_file(song, format=from_format)
        song.export(destination, to_format)
        print(f"{song_name} converted! 🎶")
