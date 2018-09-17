



def sheet_data(sheet):

    out = list()

    sheetIndex = 0
    for X in range(1, s.nrows):
        learner = s.row_values(X)
        print(learner)
        average=sum(learner)
