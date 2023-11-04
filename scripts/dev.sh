sudo docker run --rm -p 8888:8888 --entrypoint=/bin/bash --memory-swap=-1 --mount "type=bind,source=$(pwd),target=/src" -it socmed_ml_pipeline

#old shell commands back when i was running tkinter on Linux -- turns out its better to do it on Windows so this is abandoned
# sudo docker run --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -p 8888:8888 --entrypoint=/bin/bash --memory-swap=-1 --mount "type=bind,source=$(pwd),target=/src" -it socmed_ml_pipeline
# sudo docker run --rm -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -p 8888:8888 --entrypoint=/bin/bash --memory-swap=-1 --mount "type=bind,source=$(pwd),target=/src" -it socmed_ml_pipeline
