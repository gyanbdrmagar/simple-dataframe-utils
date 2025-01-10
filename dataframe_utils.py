# A collection of utility functions for pandas DataFrames

def un(df, col):
    return print('unique values: \n', df[col].unique())

def nun(df, col):
    return print('unique counts: \n', df[col].nunique())

def v_p(df, col, top=100):
    print('\nplease enter the df, col, top number, else default set to top 100\n ')
    return print('values in prec: \n', df[col].value_counts(normalize=True).nlargest(top) * 100)

def v_c(df, col):
    return print('values counts : \n', df[col].value_counts())

def d_l(df1, df2):
    df1, _ = df1.shape; df2, _ = df2.shape
    return print(f'data loss from {df1} to {df2} is {df1 - df2}')

def min_max(df, col):
    return print(f'{col} max value is {df[col].max()} and the min value is {df[col].min()}')

def n_v(df, col):
    return print(f'{col} null/blank value {df[col].isnull().sum()}')
