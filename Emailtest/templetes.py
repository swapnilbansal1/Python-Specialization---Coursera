import os
def get_templete_path(path):
	file_path = os.path.join(os.getcwd(),path)
	if not os.path.isfile(file_path):
		raise Exception("Not a valid path %s"%(file_path))
	return file_path

file_ = 'desktop\\emailtest\\templetes\\email_message.html'


def get_templete(path):
	file_path=get_templete_path(path)
	return open(file_path).read()

def render_context(templete_string, context):
	return templete_string.format(**context)

context = {
	"name": "Justin",
	"date": None,
	"total": None
}

print(render_context(get_templete(file_),context))
