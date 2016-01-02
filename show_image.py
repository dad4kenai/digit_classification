import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import sys

Training=pd.DataFrame.from_csv("/home/user/train.csv")

index = int(sys.argv[1])
images = np.array(Training).reshape((-1,28,28)).astype(np.uint8)  # Reshape for image presentaion

plt.imshow(images[index], cmap=cm.binary)  # draw the image
plt.show()
