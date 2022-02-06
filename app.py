import os
import random
import matplotlib.pyplot as plt
import glob
import numpy as np
from PIL import Image as Image

image_count = input(f'how many NFTs you want to generate? ')
DATA_DIR = 'C:/Users/ajafa/Workspace/NFTgenerator/pic'
L1 = os.listdir(DATA_DIR)

IMG = np.zeros((512, 512, 4), dtype='float32')

for j in range(int(image_count)):
    for i in L1:
        pic_root = 'C:/Users/ajafa/Workspace/NFTgenerator/pic' + '/' + i
        cp = glob.glob(f'{pic_root}/*.png')
        targets = random.choices(cp)
        img = plt.imread(targets[0])
        for k in range(512):
            for v in range(512):
                for t in range(4):
                    if img[k, v, t] != 0:
                        IMG[k, v, t] = img[k, v, t]
    fig = plt.figure(figsize=(8, 8))
    plt.imshow(IMG)
    K = '#' + str(j) + '.png'
    plt.axis('off')
    # plt.savefig(K, bbox_inches='tight')
    fig.savefig('output/'+K , bbox_inches='tight')
    IMG = np.zeros((512, 512, 4), dtype='float32')
