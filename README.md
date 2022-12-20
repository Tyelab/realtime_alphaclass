# Realtime AlphaClass Raspberry Pi Implementation

This is a repository for an experiment Caroline Jia, an MD/PhD student in the Tye Lab, is running in her FOMO task.

The goal is to use Aneesh Bal's AlphaClass for real time detection and manipulation of behavioral motifs through a Raspberry Pi
and head node computer which will have the data streamed to it and written to file.

Aneesh has successfully gotten AlphaClass running on a Pi and has used the [imagezmq](https://github.com/jeffbass/imagezmq) library
for streaming `opencv` frames over a network layer for writing data to disk.

This `README` will outline some of the basic steps that are required for a successful implementation of this project.

## Raspberry Pi Setup

Caroline is currently using my (Jeremy) Pi 4B with 8GB RAM running the basic 64bit raspbian OS. My understanding of what's needed is as follows:

- Install specific version of PyTorch to the mamba installed conda environment that AlphaClass requires

## AlphaClass Deployment on the Pi

Aneesh has successfully deployed a set of code for AlphaClass using the Pi before. There's notes I have that will fill out this part of the README
with additional steps we need to do. We also have a copy of an implementation of AlphaClass that Aneesh provided for this purpose and will be
adding it to the repository.

Once we have it installed to the Pi successfully and running, we should have an environment file created for easy installation/reproducability and
some docs about what we did put here.

## `imagezmq` Deployment

Including the `imagezmq` library into the code appears simple. The second piece of having it running concurrently with the pi sounds like it should
be similarly simple. Some initial thoughts about what is needed for this:

- Secondary environment that can be used for the head node streaming the video to file

I have more notes I'll fill this in later.

## MedPC Triggers

There's additional notes I have about what to do for this/overall structure of what it could look like with receiving triggers from the MedPC box.

## Overall workflow

I think the steps could look something like this:

1. Start streaming process on head node running MedPC commands.
2. Once stream is successfully started/waiting for camera, send signal to Pi to start waiting for a GPIO pin to rise.
3. Tell MedPC box to start. We'll have to have a TTL pulse be given the moment the recording begins.
4. On rising trigger from MedPC, start collecting data/running inference.
5. Each frame grabbed is run through AlphaClass model on pi and then sent via `zmq` to head node.
6. Head node receives frame and outputs to `opencv` video writer via H264 encoding
7. After a set number of frames is collected (time of recording/MedPC script length or whatever), send signal to pi to kill process
8. With successfull killing of Pi process, send signal back that things have closed successfully and finish writing video to disk/clean up.

Cooler implementation would be to use something like `skvideo.io` ffmpeg wrapper in `6.` so it's encoded as SLEAP prefers things at runtime.

See [here](https://github.com/Tyelab/bruker_control/blob/27c77181e0d7dfe2d77912b16c37db769b02857a/main/video_utils.py#L393) for how simple it is!

Imagine collecting data that's clean at runtime and doesn't need any post-processing. We could transfer to the server and immediately run through a
SLEAP model all through some simple shell scripting similar to what the [bruker_pipeline](https://github.com/Tyelab/bruker_pipeline) can do. Would be neat.
