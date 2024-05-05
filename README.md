# audio-converter

A function to convert multiple audio files from one format to another. (e.g. m4a to mp3).

Converted files will be saved in the same directory as the files to be converted.

## Setup

To deploy this project locally:

1. Run the following command to set up your virtual environment and install required dependencies:

```
make requirements
```

2. Activate the virtual environment:

```
source venv/bin/activate
```

3. Install ffmpeg:

```
brew install ffmpeg
```