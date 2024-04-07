# Speaker-Adaptation & Diarization-Techniques
This repository contains different Research papers which talk about Speaker Adaptive Speech Recognition.
It also contains code implementation of a Diarization Model which could partition an audio stream with
multiple people into homogeneous segments associated with each individual.

# Speaker Adaptation & Diarization

## Speaker Adaptation:
Speaker adaptation refers to the technology whereby a speech recognition system is adapted to the acoustic features of a specific user using an extremely small sample of utterances when the system is operated.


## Speaker Diariztion:
Speaker diarization is the process of partitioning an audio stream with multiple people into homogeneous segments associated with each individual. It is an important part of speech recognition systems and a well-known open problem.

### Steps for speaker diarization:
- Speech detection
- Speech Segmentation
- Embedding Extraction
- Clustering

### Technologies used:
1. Resemblyzer: It is an open-source repository which performs the 1st 3 tasks of speaker diarization.


2. spectralclusterer: open-source implementation of Spectral Clustering by Quan Wang, one of the original authors of the paper we are implementing, who has been generous enough to provide us with the code.



### Milestones
1. I explored various state-of-the-art techniques used for speaker adaptive speech recognition and diarization.


2. I implemented a Speaker Diarization Model using Spectral Clustering which could partition an audio stream with multiple people into homogeneous segments associated with each individual in both Hindi and English.


## References
1. [SPEAKER DIARIZATION USING DEEP NEURAL NETWORK EMBEDDINGS](2017_icassp_diarization_embeddings.pdf)
2. [Speaker Adaptive Model for Hindi Speech using Kaldi Speech Recognition toolkit](2017_SpeakerAdaptiveModelforHindiSpeechusingKaldiSpeechRecognitiontoolkit_IMPACT_2107.pdf)
3. [Bayesian Learning for Deep Neural Network Adaptation](BayesianLearnigDNNAdaptation.pdf)
4. [On Speaker-Independent, Speaker-Dependent, and Speaker-Adaptive Speech Recognition](icassp.1991.150478.pdf)
5. [SPEAKER ADAPTIVE TRAINING USING MODEL AGNOSTIC META-LEARNING](satmaml.pdf)
6. [Speaker Adaptive Training of Deep Neural Network Acoustic Models using I-vectors](tasl_sat.pdf)

