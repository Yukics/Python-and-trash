# Waller

This light python script simply set a gif as wallpaper with feh utility, i am using it on bspwm like this.

## Dependencies

```bash
$apt install feh
```

## Installation

Just copy paste the python script after installing feh then add execution permission and execute in the bg:

```bash
$chmod +x waller.py
$./waller.py /home/yuki/images/something.gif &
```

If you want to add it on bspwmrc you can simply:
```bash
$echo "/location_of_script/./waller.py /gif_location/hello.gif &" >> /bspwmrc_location/bspwmrc
```
