# Code for converting data from text file to speech using google cloud API

from google.cloud import texttospeech

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Read from file
f=open("out.txt", "r")
out=f.read()
f=open("out_rmse.txt", "r")
out1=f.read()


# Set the text input to be synthesized
synthesis_input = texttospeech.types.SynthesisInput(text="Number of crimes on the last day is "+out+" and RMSE error for last 20 days is "+out1)

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.types.VoiceSelectionParams(
    language_code='en-US',
    ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
    audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request on the text input with the selected voice parameters and audio file type
response = client.synthesize_speech(synthesis_input, voice, audio_config)

with open('output.mp3', 'wb') as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')