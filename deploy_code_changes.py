import git

# python -m pip install gitpython

my_repo = git.Repo("https://github.com/isaiahiyede/premuimreal.git")
# my_repo = git.Repo("/Users/iyedeisaiah/Desktop/allfiles2/projects/cdal-main/.git")

def gitTest():
	if my_repo.is_dirty(untracked_files=True):
		print('Changes detected.')
		# Check differences between current files and last commit
		diff = my_repo.git.diff(my_repo.head.commit.tree)
		print(diff)
		# Provide a list of the files to stage
		my_repo.index.add(['.gitignore', 'README.md'])
		# Provide a commit message
		my_repo.git.checkout('main')
		# Pull from main branch
		my_repo.remotes.origin.pull()
	else:
		print("No cahnges found")

gitTest()


