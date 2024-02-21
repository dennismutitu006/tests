import cmd

class InteractiveOrCommandline(cmd.Cmd):
	"""Accepts commands via the normal interactive prompt or the command line."""
	def do_greet(self, line):
		print 'hello,', line
	def do_EOF(self, line):
		print
		return True
if __name__ == '__main__':
	import sys
	if len(sys.argv) > 1:
		InteractiveOrCommandline().onecmd(' '.join(sys.argv[1:]))
	else:
		InteractiveOrCommandline().cmdloop()
