Q 		= @
REPO		= $(shell grep url .git/config)
BOLD   		= $(shell tput bold)
UNDERLINE 	= $(shell tput smul)
NORMAL 		= $(shell tput sgr0)
RED		= $(shell tput setaf 1)
YELLOW	 	= $(shell tput setaf 3)
