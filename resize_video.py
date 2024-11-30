from moviepy.editor import VideoFileClip

# 读取原始视频
video = VideoFileClip("images/recondreamer.mp4")

# 调整视频大小为 320x320
resized_video = video.resize(newsize=(320, 320))

# 保存调整后的视频
resized_video.write_videofile("recondreamer.mp4", codec="libx264")
