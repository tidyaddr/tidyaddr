import pandas, regex

def read_csv(full_file_name,chunk_size=None):
    print("CALLED READ")
    return pandas.read_csv(full_file_name,header=None,chunksize=chunk_size)

def write_csv(df,full_file_name,mode="w"):
    return df.to_csv(full_file_name,mode=mode)

def rm_char(char, df):
    return df.applymap(lambda x: x.replace(char,''))

def to_lower(df):
    return df.applymap(lambda x: x.lower())

def clean_ws(df):
    df = df.applymap(lambda x: regex.sub(r"^\s+",r"",x))
    df = df.applymap(lambda x: regex.sub(r"$\s+",r"",x))
    df = df.applymap(lambda x: regex.sub(r"\s+",r" ",x))
    return df
