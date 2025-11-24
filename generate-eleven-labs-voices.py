#!/usr/bin/env python3
import csv
import requests
import time
import os

"""
Example: ElevenLabs Text-to-Speech Batch Generator

This script reads a CSV file containing text, speaker, and output filename columns, then generates audio files using the ElevenLabs API.

Usage:
- Set your ElevenLabs API key in the environment variable ELEVENLABS_API_KEY.
- Update VOICE_IDS with your own voice IDs from ElevenLabs.
- Prepare a CSV file with columns: filename, text, speaker.
"""

# Get your API key from https://elevenlabs.io and set it as an environment variable:
# export ELEVENLABS_API_KEY="your-api-key-here"
API_KEY = os.getenv("ELEVENLABS_API_KEY")

# Replace these with your own voice IDs from ElevenLabs
VOICE_IDS = {
    "captain_quirk": "your_voice_id_1", # sweet and friendly
    "valley_girl": "your_voice_id_2", # unhinged and angry
    "tech_wizard": "your_voice_id_3", # smart guy
    "poet_laurent": "your_voice_id_4", # poetic english accent
    "event_announcer": "your_voice_id_5", # event announcer
    "paranoid_agent": "your_voice_id_6", # paranoid girl
    "random_nice_guy": "your_voice_id_7", # random nice guy announcer
    "pro_announcer": "your_voice_id_8", # professional announcer
    "flirty_spaniard": "your_voice_id_9", # spanish sexy voice
    "serious_docu": "your_voice_id_10", # documentary serious style
    "cocky_caller": "your_voice_id_11", # cocky bad quality phone calls
    "flirty_guy": "your_voice_id_12", # flirty guy
    "the_preacher": "your_voice_id_13", # the preacher
    # Add more voices as needed
}

HEADERS = {
    "xi-api-key": API_KEY,
    "Content-Type": "application/json"
}
URL_TEMPLATE = "https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

def generate_audio(filename, text, speaker):
    voice_id = VOICE_IDS.get(speaker)
    if not voice_id:
        print(f"Unknown speaker: {speaker}")
        return

    if os.path.exists(filename):
        print(f"Skipping: {filename} (already exists)")
        return

    data = {
        "text": text,
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(URL_TEMPLATE.format(voice_id=voice_id), headers=HEADERS, json=data)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Generated: {filename}")
    else:
        print(f"Failed: {filename} ({response.status_code}) - {response.text}")

def main():
    with open("segment-01-elevenlabs.csv", newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            filename = row["filename"]
            text = row["text"]
            speaker = row["speaker"]
            generate_audio(filename, text, speaker)
            time.sleep(1.2)  # slight delay to avoid hitting rate limits

if __name__ == "__main__":
    main()
