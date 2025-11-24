# ElevenLabs Batch Voice Generator

Welcome to the **Batch Voice Generator** for ElevenLabs! 🚀

Ever wanted to turn a spreadsheet of text into a chorus of quirky, poetic, or downright dramatic voices? This Python script is your ticket to audio automation stardom. Whether you need a sweet and friendly Captain Quirk, a poetic Laurent, or a cocky caller, we've got you covered (well, you provide the voices, but the script does the magic).

## What does it do?

- Reads a CSV file with your text, speaker, and desired output filename.
- Talks to the ElevenLabs API to generate audio files for each row.
- Lets you assign fun, fictional voice names to your ElevenLabs voice IDs.
- Skips files that already exist (no double trouble).
- Waits a bit between requests so you don't anger the API gods.

## Setup

1. **Clone this repo** (or just grab the script).
2. **Install dependencies**:
   ```bash
   pip install requests
   ```
3. **Get your ElevenLabs API key** from [elevenlabs.io](https://elevenlabs.io) and set it as an environment variable:
   ```bash
   export ELEVENLABS_API_KEY="your-api-key-here"
   ```
4. **Edit the script**:
   - Replace the `VOICE_IDS` dictionary with your own voice IDs and fun names.
   - Make sure your CSV file is ready (see below).

## CSV Format

Your CSV should have these columns:
- `filename` (where the audio will be saved)
- `text` (what the voice will say)
- `speaker` (the fun name you gave your voice in `VOICE_IDS`)

Example:
```csv
filename,text,speaker
hello_world.mp3,"Hello, world!","captain_quirk"
goodbye.mp3,"Goodbye, cruel world!","poet_laurent"
```

## Running the Script

Just run:
```bash
python generate-voices-elevenlabs.py
```

## Customization

- Add more voices to the `VOICE_IDS` dictionary.
- Change the CSV filename in the script if needed.
- Tweak the voice settings for extra flair.

## Disclaimer

This script is for fun, learning, and batch audio generation. Use responsibly, and don't forget to credit your favorite fictional voice actors!


Happy generating!
