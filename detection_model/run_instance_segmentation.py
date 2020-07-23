
def run(input_data):
    """
    为generetor，调用方法为：
    gen = run(input_data)
    box_result1, seg_result1 = next(gen)
    box_result2, seg_result2 = next(gen)
    ...
    调用一次next输出一帧图像的计算结果。其中的box_result为list类型数据,输出目标检测结果
    [[左下角第一维坐标，左下角第二维坐标，右上角第一维坐标，右上角第二维坐标, 目标类型],
    [左下角第一维坐标，左下角第二维坐标，右上角第一维坐标，右上角第二维坐标，目标类型]...]

    seg_result为语义分割结果

    :param input_data: 三维的numpy.ndarray数据，第一维为时间，第二，三维为图像的高和宽
    """
    pass