import base64
# Open the audio file in binary mode
with open('./assets/Charlie.mp3', 'rb') as audio_file:
    # Read the binary data
    audio_binary = audio_file.read()

# Encode the binary data to base64
audio_base64 = base64.b64encode(audio_binary).decode('utf-8')

# Now, audio_base64 contains the base64-encoded string
print("the")
print(audio_base64)