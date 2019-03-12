

# Date: 25 Oct 18
# Sai Nudurupati & Erkan Istanbulluoglu
# This script will help create GIFs of files that start with
# 'startswith' and ends with 'endswith' in the folders at
# 'fldr_pth + fldrs'. 
# Using moviepy that uses imageio in the background
# This file is self-contained - no supporting files.


import moviepy.editor as mpy
import os

# Enter the path at which the folders are
fldr_pth = 'E:/Research_UW_Sai_PhD/2018_CATGraSS_SpDist/output_fire_return_period/output/'
fps = 3
# Define the files that you want to include in the GIF with information
# on filenames
startswith = "vegtype"
endswith = ".png"
# Enter the folders for which you want to create GIFs - a GIF will
# be created for the defined filetypes in each folder. Note that you
# just specify only one folder.
fldrs = ['ch_68_tr', 'ch_69_sh', 'ch_70_tr_sh',
         'ch_71_tr', 'ch_72_sh', 'ch_73_tr_sh']

# Run the loop.
for fldr in fldrs:
    os.chdir(fldr_pth + '/' + fldr)
    file_names = sorted((fn for fn in os.listdir('.') 
        if fn.endswith(endswith) and fn.startswith(startswith)))
    clip = mpy.ImageSequenceClip(file_names, fps=fps)
    clip.write_gif('{}.gif'.format(fldr), fps=fps)