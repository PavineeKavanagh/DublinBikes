import pickle as pkl

model = 'rfc_single.pkl'
pkl_rfc = pkl.load(open(model, 'rb'))

predict = staionsId
print(pkl_rfc)