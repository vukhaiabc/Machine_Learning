from sklearn import tree
#thu thập dữ liệu
#xu li du lieu
#xay model
#du doan kq
#danh gia model
my_tree = tree.DecisionTreeClassifier()
dac_trung = [[1,3,3,7],
             [5,2,4,6],
             [1,2,4,6],
             [5,4,4,3],
             [1,4,4,7],
             [3,2,3,7],
             [3,3,3,6],
             [5,2,2,7]]
nhan = [0,1,1,0,0,0,0,1]
result_train = my_tree.fit(dac_trung,nhan)
result = result_train.predict([[1,4,3,6],[1,4,3,7],[5,2,2,7]])
print(result)

