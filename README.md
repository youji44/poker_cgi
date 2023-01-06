# poker_cgi

install: xampp CGI config

- Last line in httpd.conf

AddHandler cgi-script .cgi .pl .py
ScriptInterpreterSource Registry-Strict

- DirectoryIndex: sets the file that Apache will serve if a directory is requested.
