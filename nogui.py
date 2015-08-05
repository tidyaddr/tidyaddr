import tidycsv.utils.csv as csv
from tidycsv.utils.address.cleaning import cleanaddress_line
#df = csv.read_csv("/mnt/48126EEF751999DD/docs/work/bnia/tidycsv/tidycsv/__ex/sample_a.csv")
df = csv.read_csv("C:/Users/ID26TT95/bnia/tidycsv/tidycsv/__ex/sample_a.csv")
df = csv.to_lower(df)
df = csv.rm_char("#",df)
df = csv.rm_char(".",df)
df = csv.rm_char(",",df)
df = csv.clean_ws(df)
cleanaddress_line(df.irow(0)[0])
