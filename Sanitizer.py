import os, sys
import random
import hashlib
import time
import shutil

hash_val = hashlib.sha1()
hash_val.update(str(time.time()).encode('utf-8'))

GAMES_DIR = "Games"
SPOILERS_DIR = "Spoilers"
SPOILERS_EXT = ".txt"
DIRECTORY_DELIMITER = "\\"
BACKUP_DIR = "Back-Up"
TEST = False

def run_sanitization(working_path):
	games_path = working_path + DIRECTORY_DELIMITER + GAMES_DIR
	if not os.path.exists(games_path):
		print("Could not find games path: " + games_path)
		return False
	spoilers_path = working_path + DIRECTORY_DELIMITER + SPOILERS_DIR
	spoilers_valid = True
	if not os.path.exists(spoilers_path):
		print("Could not find spoiler path: " + spoilers_path)
		print("Continue without spoiler directory? Y/N")
		response = sys.stdin.readline()
		input_valid = False
		while not input_valid:
			if response == "N\n":
				input_valid = True
				return False
			elif response == "Y\n":
				print("Proceeding without a valid spoiler directory.")
				input_valid = True
				spoilers_valid = False
			else:
				print("Please respond with only Y or N.")
				print("Continue without spoiler directory? Y/N")
				response = sys.stdin.readline()

	valid_spoilers_list = []
	
	if spoilers_valid:
		spoilers_list = os.listdir(spoilers_path)
		print("Spoiler Files Found: ")
		for spoiler in spoilers_list:
			print(spoiler)
			spoiler_name, spoiler_ext = os.path.splitext(spoiler)
			if spoiler_ext == ".txt":
				valid_spoilers_list.append(spoiler_name)

	games_list = os.listdir(games_path)
	if len(games_list) == 0:
		print("Could not find any games at this path: " + games_path)
		return False
	print("\n--------------\n\nGames Found: ")

	for game in games_list:
		game_name, game_ext = os.path.splitext(game)
		if game_name in valid_spoilers_list:
			print(game + " | Spoiler: Yes")
		else:
			print(game + " | Spoiler: No")

	print("Confirm sanitization? Y/N:")
	response = sys.stdin.readline()
	while True:
		if response == "Y\n":
			print("Creating back ups...")
			os.makedirs(working_path + DIRECTORY_DELIMITER + BACKUP_DIR + DIRECTORY_DELIMITER + hash_val.hexdigest()[:10] + DIRECTORY_DELIMITER + GAMES_DIR, 777, True)
			for game in games_list:
				shutil.copyfile(games_path + DIRECTORY_DELIMITER + game, working_path + DIRECTORY_DELIMITER + BACKUP_DIR + DIRECTORY_DELIMITER + hash_val.hexdigest()[:10] + DIRECTORY_DELIMITER + GAMES_DIR + DIRECTORY_DELIMITER + game)
			os.makedirs(working_path + DIRECTORY_DELIMITER + BACKUP_DIR + DIRECTORY_DELIMITER + hash_val.hexdigest()[:10] + DIRECTORY_DELIMITER + SPOILERS_DIR, 777, True)
			for spoiler in spoilers_list:
				shutil.copyfile(spoilers_path  + DIRECTORY_DELIMITER + spoiler, working_path + DIRECTORY_DELIMITER + BACKUP_DIR + DIRECTORY_DELIMITER + hash_val.hexdigest()[:10] + DIRECTORY_DELIMITER + SPOILERS_DIR + DIRECTORY_DELIMITER + spoiler)
			print("Back ups can be found in: " + working_path + DIRECTORY_DELIMITER + BACKUP_DIR + DIRECTORY_DELIMITER + hash_val.hexdigest()[:10] + DIRECTORY_DELIMITER)
			print("Sanitizing.\nShuffling game order...")
			random.shuffle(games_list)

			index = 1
			print("Renaming files...")
			for game in games_list:
				game_name, game_ext = os.path.splitext(game)
				new_name = "Game " + str(index) + "_" + hash_val.hexdigest()[:10]
				index += 1
				if TEST:
					print("Test run, not renaming " + game + " to " + new_name + game_ext)
				else:
					os.rename(games_path + DIRECTORY_DELIMITER + game, games_path + DIRECTORY_DELIMITER + new_name + game_ext)
					print("Created file " + new_name + game_ext)
				if game_name in valid_spoilers_list:
					if TEST:
						print("Test run, not renaming " + game_name + SPOILERS_EXT + " to " + new_name + SPOILERS_EXT)
					else:
						os.rename(spoilers_path + DIRECTORY_DELIMITER + game_name + SPOILERS_EXT, spoilers_path + DIRECTORY_DELIMITER + new_name + SPOILERS_EXT)
						print("Created file " + new_name + SPOILERS_EXT)
			return True
		elif response == "N\n":
			return False
		else:
			print("Input not recognized. Please input exactly Y or N.")
			print("Confirm sanitization? Y/N:")
			response = sys.stdin.readline()

if __name__ == "__main__":
	print("Current working directory: " + os.getcwd())
	print("Input path for sanitizer operation:")
	working_path = sys.stdin.readline().removesuffix("\n")
	
	success = run_sanitization(working_path)
	if success:
		print("Sanitization complete.  Good luck...")
	else:
		print("Sanitization cancelled.")