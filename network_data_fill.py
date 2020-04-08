'''
Creator: Scott Wigle
         Qubify Labs
Date: 03/07/19
Purpose:
This script is to build a source of fake network data to build a social network graph.
'''

import numpy as np
import pandas as pd

class fill(object):
    def __init__(self,user_num, wo_num, loc_num):
        self.user_list = user_num
        self.wo_list = wo_num
        self.loc_list = loc_num

    def make(self):
        self.fake_user_creation(self.user_list)
        self.fake_wo_creation(self.wo_list)
        self.fake_loc_creation(self.loc_list)
        self.fill_user_data(self.user_list, self.wo_list, self.loc_list)

    def fake_wo_creation(self, num):
        wo_list = []
        for wo in range(num):
            wo_list.append(wo)

        self.wo_list = wo_list

    def fake_loc_creation(self, num):
        loc_list = []
        for loc in range(num):
            loc_list.append(loc)

        self.loc_list = loc_list

    def fake_user_creation(self, num):
        user_list = []
        for user in range(num):
            user_list.append(user)

        self.user_list = user_list

    def fill_user_data(self, user_list, wo_list, loc_list):
        fill_1 = np.random.randint(2, size=len(wo_list))
        for i in range(len(user_list)-1):
            fill_2 = np.random.randint(2, size=len(wo_list))
            fill_1 = np.vstack((fill_1,fill_2))

        loc = np.random.randint(len(loc_list), size = len(user_list))

        df = pd.DataFrame(fill_1, columns = wo_list)
        df['users'] = user_list
        df['loc'] = loc

        self.df = df


if __name__ == '__main__':
    fi = fill(50,200,51)

    fi.make()

    df = fi.df
