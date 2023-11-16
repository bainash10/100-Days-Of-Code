#Writing a program to pronounce list of names using win32 API.
import win32com.client as wincl
l=["Sristi","Abiral","Sayam"]
speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice") #It interacts with the Microsoft Speech SDK to speak what you type in from the keyboard. 
vcs = spk.GetVoices() #returns a list of SpeechSynthesisVoice objects representing all the available voices on the current device.
SVSFlag = 1
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)
spk.Speak(f"Shoutout to {l[0]}")
spk.Speak(f"Shoutout to {l[1]}")
spk.Speak(f"Shoutout to {l[2]}")