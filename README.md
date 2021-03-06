# hazard-labelling

Python GUI-based driving hazard video labelling.

This labelling tool will allow a user to label "hazardous" frames in videos, similar to how it is done in the [UK Hazard Perception Test](https://www.gov.uk/theory-test/hazard-perception-test).

This is an early prototype used primarily for myself in my research and therefore is in a perpetual state of being "in-dev", provided as is.

![screenshot](/docs/screenshot.png)

## Pre-Usage

It's fairly simple and lightweight.

1. Clone this repo into a location of your choosing
2. Install the dependencies in `requirements.txt`, either globally or in a virtual environment

## Usage

The labelling tool can operate in three ways: files, folder or default.

1. The default mode is run by executing the script with no arguments : `python main.py`. This opens the GUI with no pre set video and allows you to choose a video somewhere on your file system.

2. In files mode, video filepath(s) are passed at the command line and is loaded sequentially: `python main.py --filepath /path/to/file [/path/to/file2 ...]`. After the sequence has terminated, you can choose another video via the GUI.

3. Folder mode is similar to the above except that a path to a folder is given, and the tool recursively searches down this folder for all videos. This is the prefered mode. Run by: `python main.py --folder /path/to/folder`.

To flag a hazard, simply press the `Enter` key, or click anywhere on the video.

## Saving

The labels are saved as `.csv` files at the location of the video if the `Save labels` button is pressed. Otherwise, you can click `Export` at the bottom of the timeline and choose.

## Notes

The timeline has an upper limit of frames, so flags won't appear visually past this time, though **labelling is still happening**. This is about 300k frames, so it only occurs when labelling long-ish videos.

Currently, 60 frames after a hazard has been flagged is also flagged. This corresponds to 2 seconds for a 30fps video, and is because hazards are expected to last longer than 1 video frame.

When `Next video` is pressed, flags are saved at the video location.

The timeline can be undocked form the window by dragging.
