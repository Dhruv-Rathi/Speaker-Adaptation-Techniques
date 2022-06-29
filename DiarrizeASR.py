#!/usr/bin/env python
# coding: utf-8

# In[6]:


from resemblyzer import preprocess_wav, VoiceEncoder
from pathlib import Path

#give the file path to your audio file
audio_file_path = '/home/dhruv04/Downloads/ASR.wav'
wav_fpath = Path(audio_file_path)

wav = preprocess_wav(wav_fpath)
encoder = VoiceEncoder("cpu")
_, cont_embeds, wav_splits = encoder.embed_utterance(wav, return_partials=True, rate=16)
print(cont_embeds.shape)


# In[7]:


from spectralcluster import RefinementOptions
from spectralcluster import SpectralClusterer

refinement_operations = RefinementOptions(
    p_percentile=0.90,
    gaussian_blur_sigma=1
)

clusterer = SpectralClusterer(
    min_clusters=2,
    max_clusters=100,
    refinement_options=refinement_operations
)

labels = clusterer.predict(cont_embeds)


# In[8]:


def create_labelling(labels,wav_splits):
    from resemblyzer import sampling_rate
    times = [((s.start + s.stop) / 2) / sampling_rate for s in wav_splits]
    labelling = []
    start_time = 0
    for i,time in enumerate(times):
        if i>0 and labels[i]!=labels[i-1]:
            temp = [str(labels[i-1]),start_time,time]
            labelling.append(tuple(temp))
            start_time = time
        if i==len(times)-1:
            temp = [str(labels[i]),start_time,time]
            labelling.append(tuple(temp))

    return labelling
labelling = create_labelling(labels,wav_splits)


# In[9]:


print(labelling)


# In[10]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()
y = []
x = []

for element in labelling:
    y.append(1+int(element[0]))
    y.append(1+int(element[0]))
    x.append(element[1])
    x.append(element[2])

ax.plot(x, y)
ax.set_ylim(0, 5)

def animate(frame):
   ax.set_xlim(left=frame, right=frame+5)

ani = animation.FuncAnimation(fig, animate)

from IPython.display import HTML
HTML(ani.to_jshtml())


