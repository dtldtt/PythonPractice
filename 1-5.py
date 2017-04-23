diameter=input('请输入球的直径：')
diameter=float(diameter)/100
volume=3.1415926*((diameter/2.0)**3)*4/3
weight=volume*11340
print('%.6f'%weight)
