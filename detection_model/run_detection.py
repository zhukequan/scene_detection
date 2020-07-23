
def run(input_data):
    """
    为generetor，调用方法为：
    gen = run(input_data)
    result1 = next(gen)
    result2 = next(gen)
    ...
    调用一次next输出一帧图像的计算结果。其中的result为list类型数据.
    [[左下角第一维坐标，左下角第二维坐标，右上角第一维坐标，右上角第二维坐标, 目标类型],
    [左下角第一维坐标，左下角第二维坐标，右上角第一维坐标，右上角第二维坐标，目标类型]...]

    :param input_data: 三维的numpy.ndarray数据，第一维为时间，第二，三维为图像的高和宽
    """

    pass