import pandas as pd
import os

# read file from ./hand_joint_data.csv and return the data
def read_hand_joint_data_from_csv(file_path="./hand_joint_data.csv"):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return None
    
test =[0.0, 0.0, 0.3235294117647059, 0.22941176470588234, 0.5941176470588235, 0.4470588235294118, 0.7941176470588235, 0.6235294117647059, 1.0, 0.7470588235294118, 0.6470588235294118, 0.4, 0.8176470588235294, 0.5647058823529412, 0.9058823529411765, 0.6705882352941176, 0.9647058823529412, 0.7235294117647059, 0.48823529411764705, 0.3941176470588235, 0.6529411764705882, 0.5411764705882353, 0.7529411764705882, 0.6058823529411764, 0.8235294117647058, 0.6588235294117647, 0.35294117647058826, 0.3941176470588235, 0.48823529411764705, 0.49411764705882355, 0.5882352941176471, 0.5529411764705883, 0.6470588235294118, 0.611764705882353, 0.23529411764705882, 0.4117647058823529, 0.37058823529411766, 0.4823529411764706, 0.45294117647058824, 0.5117647058823529, 0.49411764705882355, 0.5294117647058824]
print(len(test))
print(type(test))
testlist = list(test)
print(type(testlist))

test2 = [0,0.0,0.0,0.20078740157480315,-0.051181102362204724,0.3661417322834646,-0.18110236220472442,0.484251968503937,-0.30708661417322836,0.594488188976378,-0.38188976377952755,0.2637795275590551,-0.46062992125984253,0.3425196850393701,-0.65748031496063,0.3937007874015748,-0.7834645669291339,0.42913385826771655,-0.9015748031496063,0.14960629921259844,-0.5,0.1968503937007874,-0.7244094488188977,0.23228346456692914,-0.8740157480314961,0.2559055118110236,-1.0,0.03543307086614173,-0.4881889763779528,0.031496062992125984,-0.7047244094488189,0.03543307086614173,-0.8503937007874016,0.03937007874015748,-0.9763779527559056,-0.07480314960629922,-0.42913385826771655,-0.14566929133858267,-0.5787401574803149,-0.18503937007874016,-0.6850393700787402,-0.2204724409448819,-0.7874015748031497]
print(len(test2))