import pydub
import tempfile
import whisper



def transcribe_audio(audio_file):
    """
    Transcribe audio from the provided file.

    Args:
        audio_file (str): Path to the audio file.

    Returns:
        str: Transcribed text from the audio.
    """
    model = whisper.load_model("base")
    result = model.transcribe(audio_file)
    return result["text"]

def convert_to_mp3(audio_file):
    """
    Convert an audio file to MP3 format.

    Args:
        audio_file (io.BytesIO): Audio data in bytes.

    Returns:
        str: Path to the converted MP3 file.
    """
    audio = pydub.AudioSegment.from_file(audio_file)
    mp3_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp3")
    mp3_file.name = mp3_file.name.replace("\\", "/")
    audio.export(mp3_file.name, format="mp3")
    return mp3_file.name