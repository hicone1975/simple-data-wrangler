# Author: Ke Ren

import pandas as pd
import numpy as np


class DataWrangler():

    def __init__(self,location):
        # location = raw_input("Please specify the location of the raw data file.")
        self.df = pd.read_csv(location)
        self.generalOperation()

    def generalOperation(self):
        continueOperation = input("Would you like to continue the data wrangling process? (Y/N)")
        if continueOperation == 'Y':
            self.rowindex = 0
            self.colindex = 0
            indexvalidity = False
            while not indexvalidity:
                index = input("Use a paired number separated by space to specify the index to perform operations on").split()
                self.rowindex = int(index[0])
                self.colindex = int(index[1])
                if -1 < self.rowindex < self.df.shape[0] and -1 < self.colindex < self.df.shape[1]:
                    indexvalidity = True
                else:
                    print("Invalid input of either rowindex or colindex, please enter again")
            if self.rowindex == 0 and self.colindex == 0:
                self.sheetOperation()
            elif self.rowindex == 0 and self.colindex > 0:
                self.colOperation()
            elif self.rowindex > 0 and self.colindex == 0:
                self.rowOperation()
            else:
                self.cellOperation()
        else:
            # self.df.to_excel('result.xlsx')
            pass
    def sheetOperation(self):
        # To be added
        self.generalOperation()

    def verifyDataType(self):
        pass

    def cellOperation(self):
        if pd.isnull(self.df.iloc[self.rowindex, self.colindex]):     # If this selected cell is NaN
            print("Option 1: Delete this row")
            self.selectionlist = [1]     # Store all valid operations for this specific cell in a list
            if self.colindex > 0:
                print("Option 2: Fill this empty cell with the left cell")
                self.selectionlist.append(2)
            if self.colindex < self.df.shape[1] - 1:
                print("Option 3: Fill this empty cell with the right cell")
                self.selectionlist.append(3)
            if self.rowindex > 0:
                print("Option 4: Fill this empty cell with the above cell")
                self.selectionlist.append(4)
            if self.rowindex < self.df.shape[0] - 1:
                print("Option 5: Fill this empty cell with the below cell")
                self.selectionlist.append(5)
            self.switcher = {    # Dictionary for storing all possible operations
                1: deteleRow,
                2: fillWithLeft,
                3: fillWithRight,
                4: fillWithAbove,
                5: fillWithBelow
            }
            self.optionSelection()
        else:
            print("Option 1: Verify if the data type of this cell matches the rest of this column")
            self.selectionlist = [1]
            self.switcher = {   # Dictionary for storing all possible operations
                1: verifyDataType
            }
            self.optionSelection()

    def optionSelection(self):   # Used for executing selected operation after receiving user input
        selectionvalidity = False
        while not selectionvalidity:
            self.selection = input("Please specify the option using number")
            if self.selection in self.selectionlist:
                selectionvalidity = True
            else:
                print("You specified an invalid option, please enter again")
        func = self.switcher.get(self.selection)
        func()

    def deteleRow(self):
        self.df = self.df.drop(self.df.index[self.rowindex])
        self.generalOperation()

    def fillWithLeft(self):
        if pd.isnull(self.df.iloc[self.rowindex, self.colindex - 1]) is False:
            self.df.iloc[self.rowindex, self.colindex] = self.df.iloc[self.rowindex, self.colindex - 1]
            self.generalOperation()
        else:
            print("The cell you specified to copy data from is empty")
            self.selectionlist.remove(self.selection)     # Remove this specific operation from the list to prevent selection
            self.optionSelection()

    def fillWithRight(self):
        if pd.isnull(self.df.iloc[self.rowindex, self.colindex + 1]) is False:
            self.df.iloc[self.rowindex, self.colindex] = self.df.iloc[self.rowindex, self.colindex + 1]
            self.generalOperation()
        else:
            print("The cell you specified to copy data from is empty")
            self.selectionlist.remove(self.selection)     # Remove this specific operation from the list to prevent selection
            self.optionSelection()

    def fillWithAbove(self):
        if pd.isnull(self.df.iloc[self.rowindex - 1, self.colindex]) is False:
            self.df.iloc[self.rowindex, self.colindex] = self.df.iloc[self.rowindex - 1, self.colindex]
            self.generalOperation()
        else:
            print("The cell you specified to copy data from is empty")
            self.selectionlist.remove(self.selection)  # Remove this specific operation from the list to prevent selection
            self.optionSelection()

    def fillWithBelow(self):
        if pd.isnull(self.df.iloc[self.rowindex + 1, self.colindex]) is False:
            self.df.iloc[self.rowindex, self.colindex] = self.df.iloc[self.rowindex + 1, self.colindex]
            self.generalOperation()
        else:
            print("The cell you specified to copy data from is empty")
            self.selectionlist.remove(self.selection)  # Remove this specific operation from the list to prevent selection
            self.optionSelection()



# if __main__ == "main":
#     data_df = DataWrangler()


