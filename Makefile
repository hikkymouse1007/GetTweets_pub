docker-path:
	@echo $(PWD)
path:
	@mkdir ~/command
	@cp ./command/twitter ~/command/twitter
	@ln -si ~/command/twitter /usr/local/bin
	@chmod 777 ~/command/twitter
rm-path:
	@rm -rf ~/command
	@rm /usr/local/bin/twitter 

