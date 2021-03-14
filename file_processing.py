'''
Created on 2021/01/25

@author: Kelly

'''
import os,shutil,sys,re
import pathlib,subprocess

pattern1=r'\*.\w*'                 #*.txt
pattern2=r'\w*\*.\w*'			   #a*.txt
pattern3=r'\*\w*.\w*'			   #*a.txt
pattern4=r'\w+\*.\*'               #ab*.*
pattern5=r'\*\w+.\*'               #*ab.*

#os, shutil, pathlib 
class file_processing(object):

	def __init__(self):
		'''
		Constructor
		'''		
		pass

	def _deletefile(self, file_name):
		try:
			file=pathlib.Path(file_name)
			file.unlink()
		except:
			pass

	def _deletefolder(self, folder_name):
		try:
			shutil.rmtree(folder_name)
		except:
			pass

	def _keyword_file(self,folder,key):
		global file_list
		folder_filename=[]
		file_list=[]
		for file in os.listdir(folder):
			folder_filename.append(file)
		for name in folder_filename:
			if name.find(key)!=-1:
				file_list.append(name)

	def make_folder_set(self, folder_name):
		self._deletefolder(folder_name)
		os.system("mkdir " + folder_name)

#####################delete#####################
	def _filetype_deletefile(self,file_name,*args):           #"*.txt"
		key=file_name.split("\\")[-1].split("*")[-1]
		folder=file_name.strip(file_name.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		if len(file_list)==0:
			print("No {} file in folder".format(key))
		for filename in file_list:	
			file=pathlib.Path(folder+filename)
			file.unlink()
		try:
			if args[0]=="debug":
				print("delete the file:{}".format(file_list))
		except:
			pass

	def _filetype_startswith_deletefile(self,file_name,*args):       #"a*.txt"
		key=file_name.split("\\")[-1].split("*")[-1]
		folder=file_name.strip(file_name.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.find(file_name.split("\\")[-1].split("*")[0])!=-1:          #key:a存在
				if filename.startswith(file_name.split("\\")[-1].split("*")[0]):	#以a開頭
					_list.append(filename)
					file=pathlib.Path(folder+filename)
					file.unlink()
				else:
					nokeywd_list.append(filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("delete the file:{}".format(_list))
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(file_name.split("\\")[-1]))			

	def _filetype_endswith_deletefile(self,file_name,*args):      #"*a.txt"
		key=file_name.split("\\")[-1].split(".")[-1]
		folder=file_name.strip(file_name.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.find(file_name.split("\\")[-1].split("*")[1].split(".")[0])!=-1:    #a存在      
				if filename.split(".")[0].endswith(file_name.split("\\")[-1].split("*")[1].split(".")[0]):	
					_list.append(filename)
					file=pathlib.Path(folder+filename)
					file.unlink()
				else:
					nokeywd_list.append(filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("delete the file:{}".format(_list))
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(file_name.split("\\")[-1]))		

	def _startswith_deletefile(self, file_name,*args):        #"a*.*"
		key=file_name.split("\\")[-1].split("*")[0]
		folder=file_name.strip(file_name.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.startswith(key):
				_list.append(filename)
				if os.path.isfile(folder+filename)==True:
					file=pathlib.Path(folder+filename)
					file.unlink()
				else:#folder
					shutil.rmtree(folder+filename)	
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("delete the file or folder:{}".format(_list))		
		except:
			pass	
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(file_name.split("\\")[-1]))		

	def _endswith_deletefile(self, file_name,*args):       #"*a.*"
		key=file_name.split("\\")[-1].split("*")[1].strip(".")
		folder=file_name.strip(file_name.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.split(".")[0].endswith(key):
				_list.append(filename)
				if os.path.isfile(folder+filename)==True:
					file=pathlib.Path(folder+filename)
					file.unlink()
				else:#folder
					shutil.rmtree(folder+filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("delete the file or folder:{}".format(_list))	
		except:
			pass		
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(file_name.split("\\")[-1]))		

	def delete_file_set(self, file_name,*args):
		# file=pathlib.Path(file_name)
		# file.unlink()
		if "*" in file_name:
			if re.fullmatch(pattern1,file_name.split("\\")[-1]):   #"*.txt"
				self._filetype_deletefile(file_name,*args)				
			elif re.fullmatch(pattern2,file_name.split("\\")[-1]):   #"a*.txt"  
				self._filetype_startswith_deletefile(file_name,*args)				
			elif re.fullmatch(pattern3,file_name.split("\\")[-1]):   #"*a.txt"  
				self._filetype_endswith_deletefile(file_name,*args)	
			elif re.fullmatch(pattern4,file_name.split("\\")[-1]):   #"ab*.*"
				self._startswith_deletefile(file_name,*args)
			elif re.fullmatch(pattern5,file_name.split("\\")[-1]):   #"*ab.*"
				self._endswith_deletefile(file_name,*args)
			else:
				print("Error file name")
		else:
			file=pathlib.Path(file_name)
			file.unlink()
			try:
				if args[0]=="debug":
					print("delete the file {}".format(file_name))
			except:
				pass	

	def _allthefile_deletefolder(self, folder_name,*args):
		global filename
		folder=folder_name.strip("*.*")
		if len(os.listdir(folder))== 0:
			print("No file in folder")
		try:
			if args[0]=="debug":
				print("delete the file in folder:{}".format(os.listdir(folder)))
		except:
			pass
		for filename in os.listdir(folder):
			if os.path.isfile(folder+filename)==True:
				file=pathlib.Path(folder+filename)
				file.unlink()
			else: #folder
				shutil.rmtree(folder+filename)		


	def delete_folder_set(self, folder_name,*args):
		# shutil.rmtree(folder_name)
		if "*" in folder_name:
			if folder_name.split("\\")[-1]=="*" or folder_name.split("\\")[-1]=="*.*":  #對資料夾中所有內容做複製
				self._allthefile_deletefolder(folder_name,*args)
			else:
				print("Error folder name") 		
		else:
			shutil.rmtree(folder_name)
			try:
				if args[0]=="debug":
					print("delete the folder:{}".format(folder_name))
			except:
				pass
#####################move#####################
	def _filetype_movefile(self, from_file, to_file,*args):   #"*.txt"
		key=from_file.split("\\")[-1].split("*")[-1]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		if len(file_list)==0:
			print("No {} file in folder".format(key))
		for filename in file_list:
			self._deletefile(to_file+"\\"+filename)
			shutil.move(folder+filename,to_file)			
		try:
			if args[0]=="debug":
				print("move the file:{} to {}".format(file_list,to_file))
		except:
			pass

	def _filetype_startswith_movefile(self, from_file, to_file,*args):        #"a*.txt"
		key=from_file.split("\\")[-1].split("*")[-1]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.find(from_file.split("\\")[-1].split("*")[0])!=-1:  #key:a存在
				if filename.startswith(from_file.split("\\")[-1].split("*")[0]):
					_list.append(filename)
					self._deletefile(to_file+"\\"+filename)
					shutil.move(folder+filename,to_file)
				else:
					nokeywd_list.append(filename)
			else:
				nokeywd_list.append(filename)	
		try:
			if args[0]=="debug":
				print("move the file:{} to {}".format(_list,to_file))
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))	

	def _filetype_endswith_movefile(self, from_file, to_file,*args):      #"*a.txt"
		key=from_file.split("\\")[-1].split(".")[-1]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.find(from_file.split("\\")[-1].split("*")[1].split(".")[0])!=-1:     #key:a存在
				if filename.split(".")[0].endswith(from_file.split("\\")[-1].split("*")[1].split(".")[0]):
					_list.append(filename)
					self._deletefile(to_file+"\\"+filename)
					shutil.move(folder+filename,to_file)
				else:
					nokeywd_list.append(filename)
			else:
				nokeywd_list.append(filename)	
		try:
			if args[0]=="debug":
				print("move the file:{} to {}".format(_list,to_file))
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))	

	def _startswith_movefile(self, from_file, to_file,*args):        #"a*.*"
		key=from_file.split("\\")[-1].split("*")[0]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.startswith(key):
				_list.append(filename)
				if os.path.isfile(folder+filename)==True:
					self._deletefile(to_file+"\\"+filename)
					shutil.move(folder+filename,to_file)						
				else:#folder
					self._deletefolder(to_file+"\\"+filename)
					shutil.move(folder+filename,to_file)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("move the file or folder:{} to {}".format(_list,to_file))		
		except:
			pass	
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))		

	def _endswith_movefile(self, from_file, to_file,*args):           #"*a.*"
		key=from_file.split("\\")[-1].split("*")[1].strip(".")
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.split(".")[0].endswith(key):
				_list.append(filename)
				if os.path.isfile(folder+filename)==True:
					self._deletefile(to_file+"\\"+filename)
					shutil.move(folder+filename,to_file)						
				else:#folder
					self._deletefolder(to_file+"\\"+filename)
					shutil.move(folder+filename,to_file)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("move the file or folder:{} to {}".format(_list,to_file))	
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))	

	def move_file_set(self, from_file,to_file,*args):
		# shutil.move(from_file, to_file)
		if "*" in from_file:
			if re.fullmatch(pattern1,from_file.split("\\")[-1]):   #"*.txt"
				self._filetype_movefile(from_file,to_file,*args)
			elif re.fullmatch(pattern2,from_file.split("\\")[-1]):   #"a*.txt"
				self._filetype_startswith_movefile(from_file,to_file,*args)
			elif re.fullmatch(pattern3,from_file.split("\\")[-1]):   #"*a.txt"
				self._filetype_endswith_movefile(from_file,to_file,*args)
			elif re.fullmatch(pattern4,from_file.split("\\")[-1]):   #"a*.*"
				self._startswith_movefile(from_file,to_file,*args)
			elif re.fullmatch(pattern5,from_file.split("\\")[-1]):   #"*a.*"
				self._endswith_movefile(from_file,to_file,*args)
			else:
				print("Error from_file")		
		else:
			try:
				if args[0]=="debug":
					print("move the file:{} to {}".format(from_file,to_file))
			except:
				pass
			try:
				shutil.move(from_file,to_file)
			except:
				fname=from_file.split("\\")[-1]
				self._deletefile(to_file+"\\"+fname) 
				shutil.move(from_file,to_file)


	def _allthefile_movefolder(self, from_folder, to_folder,*args):
		folder=from_folder.strip("*.*")
		if len(os.listdir(folder))== 0:
			print("No file in folder")
		try:
			if args[0]=="debug":
				print("move the file:{} to {}".format(os.listdir(folder),to_folder))
		except:
			pass
		for filename in os.listdir(folder):	
			if os.path.isfile(folder+filename)==True:			
				self._deletefile(to_folder+"\\"+filename)	
				shutil.move(folder+filename,to_folder)
			else:	
				self._deletefolder(to_folder+"\\"+filename)		
				shutil.move(folder+filename,to_folder)		


	def move_folder_set(self, from_folder, to_folder,*args):
		# shutil.move(from_folder, to_folder)
		if "*" in from_folder:
			if from_folder.split("\\")[-1]=="*" or from_folder.split("\\")[-1]=="*.*":
				self._allthefile_movefolder(from_folder, to_folder,*args)
			else:
				print("Error from_file") 							
		else:                                  
			shutil.move(from_folder, to_folder)  
			try:
				if args[0]=="debug":
					print("move the folder {} to {}".format(from_folder,to_folder))
			except:
				pass
#####################copy#####################
	def _filetype_copyfile(self, from_file, to_file,*args):           #"*.txt"
		key=from_file.split("\\")[-1].split("*")[-1]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		if len(file_list)==0:
			print("No {} file in folder".format(key))
		for filename in file_list:
			shutil.copy(folder+filename,to_file)
		try:
			if args[0]=="debug":
				print("copy the file:{} to {}".format(file_list,to_file))
		except:
			pass	

	def _filetype_startswith_copyfile(self, from_file, to_file,*args):        #"a*.txt"
		key=from_file.split("\\")[-1].split("*")[-1]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.find(from_file.split("\\")[-1].split("*")[0])!=-1:          #key:a存在就copy
				if filename.startswith(from_file.split("\\")[-1].split("*")[0]):	#以a開頭
					_list.append(filename)
					shutil.copy(folder+filename,to_file)
				else:
					nokeywd_list.append(filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("copy the file:{} to {}".format(_list,to_file))
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))	

	def _filetype_endswith_copyfile(self, from_file, to_file,*args):           #"*a.txt"
		key=from_file.split("\\")[-1].split(".")[-1]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.find(from_file.split("\\")[-1].split("*")[1].split(".")[0])!=-1:    #a存在      
				if filename.split(".")[0].endswith(from_file.split("\\")[-1].split("*")[1].split(".")[0]):	
					_list.append(filename)
					shutil.copy(folder+filename,to_file)
				else:
					nokeywd_list.append(filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("copy the file:{} to {}".format(_list,to_file))
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))		

	def _startswith_copyfile(self, from_file, to_file,*args):        #"a*.*"
		key=from_file.split("\\")[-1].split("*")[0]
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.startswith(from_file.split("\\")[-1].split("*")[0]):
				_list.append(filename)
				if os.path.isfile(folder+filename)==True:
					shutil.copy(folder+filename,to_file)
				else:#folder
					self._deletefolder(to_file+"\\"+filename)
					shutil.copytree(folder+filename,to_file+"\\"+filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("copy the file or folder:{} to {}".format(_list,to_file))		
		except:
			pass		
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))

	def _endswith_copyfile(self, from_file, to_file,*args):           #"*a.*"
		key=from_file.split("\\")[-1].split("*")[1].strip(".")
		folder=from_file.strip(from_file.split("\\")[-1])+"\\"
		self._keyword_file(folder,key)
		nokeywd_list=[]
		_list=[]
		for filename in file_list:
			if filename.split(".")[0].endswith(key):
				_list.append(filename)
				if os.path.isfile(folder+filename)==True:
					shutil.copy(folder+filename,to_file)
				else:#folder
					self._deletefolder(to_file+"\\"+filename)
					shutil.copytree(folder+filename,to_file+"\\"+filename)
			else:
				nokeywd_list.append(filename)
		try:
			if args[0]=="debug":
				print("copy the file or folder:{} to {}".format(_list,to_file))	
		except:
			pass
		if len(nokeywd_list)==len(file_list):
			print("No {} file in folder".format(from_file.split("\\")[-1]))

	def copy_file_set(self, from_file, to_file,*args):  #cover   
		# shutil.copy(from_file, to_file)
		if "*" in from_file:
			if re.fullmatch(pattern1,from_file.split("\\")[-1]):   #"*.txt"
				self._filetype_copyfile(from_file, to_file,*args)		
			elif re.fullmatch(pattern2,from_file.split("\\")[-1]):   #"a*.txt"  
				self._filetype_startswith_copyfile(from_file, to_file,*args)	
			elif re.fullmatch(pattern3,from_file.split("\\")[-1]):   #"*a.txt"  
				self._filetype_endswith_copyfile(from_file, to_file,*args)	
			elif re.fullmatch(pattern4,from_file.split("\\")[-1]):   #"a*.*"
				self._startswith_copyfile(from_file, to_file,*args)
			elif re.fullmatch(pattern5,from_file.split("\\")[-1]):   #"*a.*"
				self._endswith_copyfile(from_file, to_file,*args)
			else:
				print("Error from_file")
		else:
			shutil.copy(from_file, to_file)
			try:
				if args[0]=="debug":
					print("copy the file:{} to {}".format(from_file,to_file))
			except:
				pass			

	def _allthefile_copyfolder(self, from_folder, to_folder,*args):
		folder=from_folder.strip("*.*")
		if len(os.listdir(folder))== 0:
			print("No file in folder")
		for filename in os.listdir(folder):
			if os.path.isfile(folder+filename)==True:
				shutil.copy(folder+filename,to_folder)
			else: #folder
				self._deletefolder(to_folder+"\\"+filename) 
				shutil.copytree(folder+filename,to_folder+"\\"+filename) 
		try:
			if args[0]=="debug":
				print("copy the file:{} to {}".format(os.listdir(folder),to_folder))
		except:
			pass			

	def copy_folder_set(self, from_folder, to_folder,*args):  #to_folder:path+foldername
		# shutil.copytree(from_folder, to_folder)
		if "*" in from_folder:
			if from_folder.split("\\")[-1]=="*" or from_folder.split("\\")[-1]=="*.*":  
				self._allthefile_copyfolder(from_folder, to_folder,*args)
			else:
				print("Error from_folder") 		
		else:       
			shutil.copytree(from_folder, to_folder)     #to_folder:path+foldername
			try:
				if args[0]=="debug":
					print("copy the folder {} to {}".format(from_folder,to_folder))
			except:
				pass
