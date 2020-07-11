from h_generation_based_on_traffic import Traffic
import numpy as np

test = Traffic(5,5)


comrate_list = []
action = np.array([0,1,2,3,4], dtype='int_')
for i in range(50):
    test.reset()
    comrate = 0
    done = False
    while not done:
        observation, reward, done, info = test.step(action, test=1)
        comrate += info['comrate']
    comrate_list.append(comrate)
ave = np.mean(comrate_list)
print('average={0:.4e}'.format(ave))
