# convert_video

## Convert video to ProRes to us in da vinci resolve

Take as input a video and output a ProRes video.

```bash
ffmpeg -i input.mov -c:v prores_ks -profile:v 4 -c:a pcm_s16l -pix_fmt yuva444p10le  output.mov
```