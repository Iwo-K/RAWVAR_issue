import scanpy as sc

adata = sc.read('./data/minidata2.h5ad')
print(adata.var.head())
print(adata.var.shape)

print(adata.raw.var.head())
print(adata.raw.var.shape)

adataR = sc.read('./data/minidata2.h5ad', backed = 'r')
print(adataR.var.head())
print(adataR.var.shape)

print(adataR.raw.var.head())
print(adataR.raw.var.shape)
