'''
Creator: Scott Wigle
         Qubify Labs
Date: 03/07/19
Purpose:
This script is to build a source of fake network data to build a social network graph.
'''

import numpy as np
import pandas as pd

class Fill(object):
    def __init__(self,user_num, wo_num, loc_num):
        self.USER_NUM = user_num
        self.WO_NUM = wo_num
        self.LOC_NUM =loc_num
        self.user_list = []
        self.wo_list = []
        self.loc_list = []
        self.df = pd.DataFrame([])
        self.df_filled = False

    def make(self, clear_data = False):
        if clear_data:
            self.user_list = []
            self.wo_list = []
            self.loc_list = []
            self.df_filled = False
        if self.df_filled:
            print('Data already created. Access the fill objects data in classes df.')
            print('If you would like to rebuild the data pass clear_data = True into the make() method. ')
        else:
            self._fake_user_creation()
            self._fake_wo_creation()
            self._fake_loc_creation()
            self._fill_user_data()

        return self.df


    def _fake_wo_creation(self):
        for wo in range(self.WO_NUM):
            self.wo_list.append(wo)


    def _fake_loc_creation(self):
        for loc in range(self.LOC_NUM):
            self.loc_list.append(loc)


    def _fake_user_creation(self):
        for user in range(self.USER_NUM):
            self.user_list.append(user)


    def _fill_user_data(self):
        fill_1 = np.random.randint(2, size=len(self.wo_list))
        for i in range(len(self.user_list)-1):
            fill_2 = np.random.randint(2, size=len(self.wo_list))
            fill_1 = np.vstack((fill_1,fill_2))

        loc = np.random.randint(len(self.loc_list), size = len(self.user_list))

        df = pd.DataFrame(fill_1, columns = self.wo_list)
        df['users'] = self.user_list
        df['loc'] = loc

        self.df = df
        self.df_filled = True


if __name__ == '__main__':
    fill = Fill(50,200,51)

    fill.make()
    print(fill.df.shape)

    fill.USER_NUM = 25
    fill.make(clear_data = True)
    print(fill.df.shape)
