import imagej
import scyjava
import time
import os

os.environ['JAVA_TOOL_OPTIONS'] = '-Djava.awt.headless=false'
# ij = imagej.init('/Applications/Fiji.app', headless=False)
# ij.ui().showUI()

# while True:
#     time.sleep(1)
# scyjava.config.add_option('-Xmx6g')
#ij = imagej.init(mode='gui')
# ij = imagej.init()
#ij = imagej.init(mode='interactive')
ij = imagej.init('/Applications/Fiji.app', headless=False)
#ij.ui().showUI("swing")
exit(0)
# ij = imagej.init('/Applications/Fiji.app')
info = ij.getApp().getInfo(True)
print(info)

# load test image
dataset = ij.io().open('/Users/zhuxiaoqiang/Desktop/my_sync/dieshot/kx6000..jpg')
rm = ij.RoiManager.getRoiManager()

# display test image (see the Working with Images for more info)
ij.py.show(dataset)
# ij.py.show(dataset, cmap='gray')

ij.ui().showUI()
exit(0)
