import time

# color scheme

bright_color_code  = "36"
bright = "\033[0m\033[1;" + bright_color_code + "m"
bold = "\033[1m"
tag = "\033[0;33m"
note = "\033[0;92m"
warning = "\033[1;33m"
module = "\033[3;31m"
error = "\033[1;31m"
point = "\033[1;96m"
item = "\033[1;92m"
end = "\033[0m"

# errors

error_module_not_found = point + "[~]" + error + bold + " ERROR! Module Not Found! You can your own python3 module in ./modules" + end
error_ip_not_set = point + "[~]" + error + " ERROR!  IP not set!" + end
error_unable_to_fetch_data = point + "[~]" + error + " ERROR! Unable to fetch data!" + end
error_result_not_found = point + "[~]" + error + " Error! No results Found!" + end
error_integer_expected = point + "[~]" + error + " Error! This is not a number!" + end
error_one_or_more_field_required = point + "[~]" + error + " ERROR! One more field required with location to run the search." + end
error_first_last_name_cannot_be_empty = point + "[~]" + error + " ERROR! First or Last name can not be empty." + end
error_atleast_one_field_required = point + "[~]" + error + " ERROR! Atleast one field is required to run the search." + end

# warnings

warning_incorrect_command = point + "[~]" + warning + " WARNING! Incorrect command! Type 'help' to get a list of commands." + end
warning_poor_connection = point + "[~]" + warning + " WARNING! Poor Connection!" + end
warning_rate_limit = point + "[~]" + warning + " WARNING! Rate Limit per IP Exceeded! A workaround to this is changing your IP." + end
warning_atleast_one_field_required = point + "[~]" + warning + " WARNING! Atleast one field is required to run the search!" + end

# tags

cmd_tag = tag + "<plasma> " + end

# banners

def banner():
	print ("\n" + bright)
	print ("                      _____                                  ")
	print ("                     /  _  \ __                              ")
	print ("                    /  / / // /____ _ _____ ____ ___   ____ _")
	print ("                   /  /_/ // // __ `// ___// __ `__ \ / __ `/")
	print ("                  /  ____// // /_/ /(__  )/ / / / / // /_/ / ")
	print ("                 /  /    /_/ \__,_//____//_/ /_/ /_/ \__,_/  ")
	print ("                /__/                                         ")
	print ("                        []", end="\r")
	created_by ="                        [Plasma v0.1, Ahmad M. Khan"
	for pointer in range(24,53):
		print (created_by[0:pointer] + "]", end="\r")
		time.sleep(0.05)
	print ("\n\n")
	return True

def help_banner():
	print (note + "\n--------------------------------------------------------------------------------")
	print ("                                   HELP MENU ")
	print ("--------------------------------------------------------------------------------\n")
	return True

def info_banner():
	print (note + "\n--------------------------------------------------------------------------------")
	print ("                                   INFORMATION ")
	print ("--------------------------------------------------------------------------------\n")
	return True

def recon_banner():
	print (note + "\n--------------------------------------------------------------------------------")
	print ("                                  Recon Modules                                 ")
	print ("--------------------------------------------------------------------------------\n")
	return True