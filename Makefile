
deploy-micropython:
	wget https://micropython.org/resources/firmware/rp2-pico-20220618-v1.19.1.uf2 -O deps/micropython.uf2
	cp deps/micropython.uf2 /Volumes/RPI-RP2

config-pico:
	cp deps/pimoroni-pico-v1.19.6-micropython.uf2 /Volumes/RPI-RP2

env:
	workon pimorini && pip3 install adafruit-ampy

clean:
	ampy --port /dev/tty.usbmodem2101 rm main.py

deploy:
	 ampy --port /dev/tty.usbmodem2101 put src/main.py
	 ampy --port /dev/tty.usbmodem2101 put src/rgb_keyboard.py