import os
import glob # needed for listing sources files

NUMBER_OF_LINES_FOR_CONTRACT_CHECKED = 5

def clean_string(to_clean):
  to_clean = to_clean.replace(" ","")
  to_clean = to_clean.replace("\t","")

def framadoc_read_config_files():
  includes_config_file = open("includes", "r")
  includes = includes_config_file.read()
  includes_config_file.close()
  i_dir = includes.split("\n")
  
  sources_config_file = open("sources", "r")
  sources = sources_config_file.read()
  sources_config_file.close()
  s_dir = sources.split("\n")
  
  return [i_dir, s_dir]


def framadoc_get_source_files():
  source_list = []
  [inc_dir, src_dir] = framadoc_read_config_files()
  
  for s in src_dir:
    source_list = source_list + glob.glob(s + "/*.c")

  for i in range(len(source_list)):
    source_list[i] = source_list[i].replace("\\","/")
    
  return source_list

def framadoc_get_list_of_modules():
  s_lst = framadoc_get_source_files()
  ret = []
  
  for i in range(len(s_lst)):
    arr = s_lst[i].split("/")
    ret.append(arr[-1])
    
  return ret

def framadoc_get_modules_dictionary():
  src_files = framadoc_get_source_files()
  ret_dic = {}
  for i in range(len(src_files)):
    s = src_files[i]
    current_source_file = open(s)
    content = current_source_file.read()
    current_source_file.close()
    content = content.split("\n")
    list_of_functions_in_module=[]
    for i in range(len(content)):
      line = content[i]
      clean_string(line)
      if line == "{":
        func_name = content[i-1]
        split_func_name = func_name.split("(")
        split_func_name = split_func_name[0].split(" ")
        func_name = split_func_name[-1]
        list_of_functions_in_module.append(func_name)
    arr = s.split("/")
    arr = arr[-1]
    arr = arr.split(".")
    arr = arr[0]
    ret_dic[arr] = list_of_functions_in_module
  return ret_dic

#if not os.path.exists(module_dir):
#      os.makedirs(module_dir)

def framadoc_check_if_there_is_contract(func_signature_line, content):
  global NUMBER_OF_LINES_FOR_CONTRACT_CHECKED
  for i in range(NUMBER_OF_LINES_FOR_CONTRACT_CHECKED):
    line = content[func_signature_line-i-1]
    clean_string(line)
    if "*/" in line:
      return func_signature_line-i-1
  return -1
    

def framadoc_get_function_contract(source_path, func_name):
  f = open(source_path, "r")
  content = f.read()
  f.close()

  ret = ""

  content = content.split("\n")
  for i in range(len(content)):
    line = content[i]
    clean = line.replace(" ","")
    clean = clean.replace("\t","")
    if clean == "{":
      if func_name in content[i-1]:
        contract_end_line = framadoc_check_if_there_is_contract(i-1,content)
        if contract_end_line > 0:
          for k in range(contract_end_line-1):
            if "/*@" in content[contract_end_line-k-1]:
              contract_begin_line = contract_end_line-k-1
              return content[contract_begin_line:contract_end_line]
        else:
          return "no_contract"

def framadoc_get_path_of_module(module_name):
  src_files = framadoc_get_source_files()
  for path in src_files:
    splited = path.split("/")
    if module_name in splited[-1]:
      return path
  return "no_path"

def framadoc_generate_html_files():
  mod_dic = framadoc_get_modules_dictionary()

  index_path = "index.html"
  f = open(index_path,"w+")
  f.write("<h1>Framadoc</h1>\n")
  f.write("<h2>Liste des modules : </h2>\n")
  f.write("<ul>\n")
  for module_name in mod_dic.keys():
    f.write("<li><a href = 'modules/{}.html'>{}</a></li>".format(module_name, module_name))
  f.write("</ul>\n")
  f.close()
  
  for module_name, func_lst in mod_dic.items():
    new_html_path = "modules/{}.html".format(module_name)
    f = open(new_html_path,"w+")
    f.write("<h1>Liste des fonctions du module '{}'</h1>\n".format(module_name))
    f.write("<ul>\n")
    for func in func_lst:
      f.write("\t<li>{}:</li>\n".format(func))
      path = framadoc_get_path_of_module(module_name)
      if path != "no_path":
        func_contract = framadoc_get_function_contract(path,func)
        if func_contract != "no_contract":
          for line in func_contract:
            f.write("{}<br/>\n".format(line))
    f.write("</ul>\n")
    f.write("\n<br/><a href = '../index.html'>retour</a>\n")
    f.close()

def framadoc_generate_all():
  framadoc_generate_html_files()

framadoc_generate_all()
