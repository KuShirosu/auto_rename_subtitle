import os
from natsort import natsorted

path = r"E:\videos\PingPong" + "\\"


def get_file_names():
    file_names = os.listdir(path)
    return file_names


def get_video_names():
    video_names = []
    file_names = get_file_names()
    for file_name in file_names:
        if file_name.endswith(".mkv"):
            video_names.append(file_name)
    video_names = natsorted(video_names)
    return video_names


def get_subtitle_names():
    subtitle_names = []
    file_names = get_file_names()
    for file_name in file_names:
        if file_name.endswith(".ass"):
            subtitle_names.append(file_name)
    subtitle_names = natsorted(subtitle_names)
    return subtitle_names


def rename_subtitle(path, video_names, subtitle_names):
    video_names_with_subtitle_ext = []
    for video_name, subtitle_name in zip(video_names, subtitle_names):
        video_base = os.path.splitext(video_name)[0]
        subtitle_ext = os.path.splitext(subtitle_name)[1]
        video_names_with_subtitle_ext.append(video_base + subtitle_ext)
    for video_name_with_subtitle_ext, subtitle_name in zip(
        video_names_with_subtitle_ext, subtitle_names
    ):
        os.rename(path + subtitle_name, path + video_name_with_subtitle_ext)


def show_both_names(video_names, subtitle_names):
    for video_name, subtitle_name in zip(video_names, subtitle_names):
        print(f"비디오 이름: {video_name}, 자막 이름: {subtitle_name}")


video_names = get_video_names()
subtitle_names = get_subtitle_names()
show_both_names(video_names, subtitle_names)

print()

rename_subtitle(path, video_names, subtitle_names)


video_names = get_video_names()
subtitle_names = get_subtitle_names()
show_both_names(video_names, subtitle_names)

print()

for video_name, subtitle_name in zip(video_names, subtitle_names):
    if os.path.splitext(video_name)[0] == os.path.splitext(subtitle_name)[0]:
        print("좋음!")
    else:
        print("조졌네..")
