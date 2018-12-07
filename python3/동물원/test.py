import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
from matplotlib import style

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
style.use('ggplot')

industry = ['Insect', 'Reptile', 'Aquatic', 'Bird', 'Mammal']
fluctuations = [3, 3, 5, 4, 2]

fig = plt.figure(figsize=(8, 4))
ax = fig.add_subplot(111)

ypos = np.arange(5)
rects = plt.barh(ypos, fluctuations, align='center', height=0.5)
plt.yticks(ypos, industry)



plt.xlabel('등락률')
plt.show()