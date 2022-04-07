import pandas as pd

file = pd.read_csv(r'/home/eunju/Downloads/Y_axis_plus_straight_final_02.csv')
new_txt_file = file.to_csv('/home/eunju/Downloads/Y_axis_plus_straight_final_02.txt', sep=' ', index=False)