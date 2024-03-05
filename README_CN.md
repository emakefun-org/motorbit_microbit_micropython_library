# Motorbit Microbit Micropython 库

## 概述

该仓库提供了Motorbit的MicroPython的库文件和示例文件，展示了如何控制Motorbit板子上的电机接口和舵机接口，仅支持Microbit MicroPython。

## 库文件

| 文件路径 |
| --- |
| [pca9685.py](pca9685.py) |
| [motorbit.py](motorbit.py) |

使用前，请将以上库文件全部上传到运行了MicroPython的Microbit上。

## 示例文件

| 文件路径 | 示例说明 |
| --- | --- |
| [examples/dc_speed/main.py](examples/dc_speed/main.py) | Motorbit M1 ~ M4 端口驱动电机 |
| [examples/servo/main.py](examples/servo/main.py) |  Motorbit S1 ~ S8 端口驱动普通舵机，如SG90 |
| [examples/geek_servo/main.py](examples/geek_servo/main.py) |  Motorbit S1 ~ S8 端口驱动普通积木舵机 |

详情请参考示例源码

## 许可证

MIT

## 联系方式

若有任何问题，请通过邮箱联系我：<arex@null-lab.com>。
