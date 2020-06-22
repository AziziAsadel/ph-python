#!/bin/python
#Recoded By Azizi Asadel
#jkt48zee @ Telegram

try :
     import requests,re,os,sys,re,json,subprocess
except:
    os.system("pip install requests;pip install bs4")

inp=None

kontol = """
\t\t                        ___________________
\t\t ____                  | _           _     |
\t\t|  _ \ ___  _ __ _ __  || |__  _   _| |__  |
\t\t| |_) / _ \| '__| '_ \ || '_ \| | | | '_ \ |
\t\t|  __/ (_) | |  | | | ||| | | | |_| | |_) ||
\t\t|_|   \___/|_|  |_| |_|||_| |_|\__,_|_.__/ |
\t\t                       |___________________|
\t\t        Downloader Pyhton Version
"""

# sys version
def _input_url(string):
	if sys.version_info.major>2:return input(str(string))
	else:return raw_input(string)

# download
class download:
	def __init__(self):
		pass
	@staticmethod
	def get_download_list(url=None):
		try:
			_req = requests.get(url,
				headers =
					{
						"User-Agent":"Mozilla/5.0 (Linux; Android 10; Pixel 4 XL)"
					}
			)
			if _req.status_code == 200:
				_json = json.loads(
					list(re.findall('var qualityItems_([0-9])*\s\S\s(.*?);',_req.text).pop()).pop()
				);return {"result":_json, "message":"success"}
			else:return {"result":[],"message":"error","error_message":"bad url"}
		except Exception as _e:return {"message":"error","error_message":"%s"%_e}

	@staticmethod
	def _input_url_to_download(json=None,show=True):
		global inp
		_list=[]
		_count=0
		_banner="\n\tSelect Resolution\n{}"
		for i in json:
			if i["url"]=="":continue
			_count+=1
			_list.append("\n  %s. Resolution %s"%(_count,i["text"]))

		if show==True:
			print(_banner.format("".join(_list)))
			print("  %s. Input url again\n"%str(_count+1))
		while True:
			try:
				c = _input_url("[!] >>> ")
				if c==str(_count+1):
					start()
			except Exception as e:
				print("[!] Error : %s"%e)
			download().ask_before_download(url=json[int(c)-1]["url"], json=json)

	@staticmethod
	def _tanya(output=None):
		print("[!] Saved as : %s"%output)
		g=_input_url("[?] View [Y/N] > ")
		if g=="y":
			subprocess.Popen(["am","start","file://"+output]).wait()
			print("\n[OK] Finisned");start()
		else:exit("\n[OK] Finisned");_input_url("[!] Press enter to again...");start()

	@staticmethod
	def ask_before_download(url=None, json=None):
		global inp
		print("[?] (S)ee video\n    (D)ownload\n    (B)ack?\n")
		c = _input_url("[!] >>> ").lower()
		if c=="d":
			subprocess.Popen([
				"curl","-o",
					inp.split("/").pop().replace("view_video.php?viewkey=","")+".mp4",url]).wait()
			f=os.getcwd()+"/"+inp.split("/").pop().replace("view_video.php?viewkey=","")+".mp4"
			download()._tanya(output=f)
		elif c=="b":
			download()._input_url_to_download(json=json)
		else:
			subprocess.Popen(["am","start",url],
				stdout=subprocess.PIPE,
					 stdin=subprocess.PIPE,stderr=subprocess.PIPE).wait()
			download().ask_before_download(url=url, json=json)


def start():
	global inp
	print(kontol)
	print("[R] Recoded : Azizi Asadel / jkt48.zee \n[E] Example : https://www.pornhub.com/view_video.php?viewkey=xxxxxxxx\n")
	while True:
		inp=_input_url("[URL] >>> ")
		if (inp==""):continue
		json=download().get_download_list(url=inp)
		if json["message"]=="error":
			print("[!] Error : %s"%json["error_message"])
		else:
			download()._input_url_to_download(
				json=download().get_download_list(url=inp)["result"])
			break	

if __name__=="__main__":
	start()

