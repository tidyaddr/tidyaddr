import pandas, regex, subprocess
from tidyaddr.utils.match import Match
from tidyaddr.utils.filter import Filter
from tidyaddr.utils.sub import Sub
from tidyaddr.utils import datatools
from tidyaddr.utils import address as addr

def sub_address_fields(series):
    series['sfx'] = Sub.apply_subs(addr.sfx_subs,series['sfx'])
    series['dir'] = Sub.apply_subs(addr.dir_subs,series['dir'])
    return series

def cleanaddress_line(s):
    result = pandas.Series(['?','?','?','?','?'],index=('num','dir','name','sfx','unit'))

    ###STREET SUFFIX -- check the whole string for suffix
    sfx_matches = Match.findall_patterns_in_s(addr.sfx_cases, s)
    sfx_excepts = Match.findall_patterns_in_s(addr.sfx_ignores, s)
    sfx_matches = Filter.does_not_match_any(sfx_excepts,sfx_matches)
    sfx_matches = Filter.rightmost_left_index(sfx_matches)
    sfx_matches = Filter.longest(sfx_matches)
    if len(sfx_matches) == 0: return result
    sfx_m = sfx_matches[0]
    sfx = sfx_m.str
    result['sfx'] = sfx

    ###STREET NUMBER -- check the whole string, as it must occur first
    num_matches = Match.findall_patterns_in_s(addr.num_cases, s)
    sfx_matches = Filter.leftmost_left_index(num_matches)
    sfx_matches = Filter.longest(num_matches)
    if len(num_matches) == 0: return result
    num_m = num_matches[0]
    num = num_m.str
    result['num'] = num

    ###STREET DIRECTION -- check anything that is not the suffix
    dir_matches = Match.findall_patterns_in_s(addr.dir_cases, s)
    dir_excepts = Match.findall_patterns_in_s(addr.dir_ignores, s)
    dir_matches = Filter.does_not_match_any(dir_excepts, dir_matches)
    dir_matches = Filter.is_outside_match(sfx_m,dir_matches)
    #choose the one on the leftside if one found on both sides
    dir_matches = Filter.leftmost_left_index(dir_matches)
    dir_matches = Filter.longest(dir_matches)
    if len(dir_matches) > 0:
        dir_m = dir_matches[0]
        dir = dir_m.str
        result['dir'] = dir
    else:
        dir_m = None
        dir = None
        result['dir'] = ""

    if dir_m is not None and dir_m.left_of(sfx_m):
        name = Match.substring_between_matches(s,dir_m,sfx_m)
        name = name.strip() #remove trailing white space
        unit = Match.substring_rightof_match(s,sfx_m)
        unit = unit.strip()
    elif dir_m is not None and dir_m.right_of(sfx_m):
        name = Match.substring_between_matches(s,num_m,sfx_m)
        name = name.strip()
        unit = Match.substring_rightof_match(s,dir_m)
        unit.strip()
    else:
        name = Match.substring_between_matches(s,num_m,sfx_m)
        name = name.strip()
        unit = Match.substring_rightof_match(s,sfx_m)
        unit = unit.strip()
    result['name'] = name
    result['unit'] = unit

    return result





def cleanaddress(input_file,output_dir):
    chunksize = 1000
    reader = datatools.read_csv(input_file, chunksize)
    output_file = output_dir + "/out.csv"
    include_head = True
    for data in reader:
        #preprocessing
        data = datatools.rm_char("#",data)
        data = datatools.rm_char(",",data)
        data = datatools.rm_char(".",data)
        data = datatools.to_lower(data)
        data = datatools.clean_ws(data)

        new_data = data[0].apply(cleanaddress_line)
        new_data = new_data.apply(sub_address_fields, axis=1,reduce=False)
        new_data["tidy_address"] = new_data.apply(cat_line, axis=1,reduce=True)
        new_data["original"] = data[0]
        #output
        datatools.write_csv(new_data,output_file,"a",header=include_head)
        include_head = False

def cat_line(series):
    tmp = series['num'] + ' ' + series['dir'] + ' ' + series['name'] + ' ' + series['sfx']
    tmp = regex.sub(r"^\s+",r"",tmp)
    tmp = regex.sub(r"$\s+",r"",tmp)
    tmp =  regex.sub(r"\s+",r" ",tmp)
    return tmp
