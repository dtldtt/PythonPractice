outerDiameter=float(input('请输入球的外直径：'))/100
innerDiameter=float(input('请输入球的内直径：'))/100
volume=4/3.0*3.1415926*((outerDiameter/2)**3-(innerDiameter/2)**3)
weight=11340*volume
print("此空心球的重量为：%.6f"%weight,"kg")
