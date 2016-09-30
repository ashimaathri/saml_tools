SHELL := /bin/bash
MAKEFILE_RULES := $(shell cat Makefile | grep "^[A-Za-z]" | awk '{print $$1}' | sed "s/://g" | sort -u)

.SILENT: help
.PHONY: $(MAKEFILE_RULES)

default: help

check:  ## See if the certs match. If it just says Writing RSA key, then they are good
	diff  <(openssl x509 -in sp.crt -pubkey -noout) <(openssl rsa -in sp.key -pubout)

key:  ## Create a new key
	openssl genrsa -out sp.key 2048

certificate:  ## Create a new ssl cert
	openssl req -new -x509 -key sp.key -out sp.crt -days 1024 -subj "/CN=sp-name.rackspace.com/O=Rackspace/C=US"

keypair:  ## Create a new keypair
	openssl req -x509 -newkey rsa:2048 -keyout sp.key -out sp.crt -days 1024 -subj "/CN=sp-name.rackspace.com/O=Rackspace/C=US"

help:  ## This help dialog.
	echo "    You can run the following commands from this$(MAKEFILE_LIST): "
	IFS=$$'\n' ; \
	help_lines=(`fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sort`) ; \
	for help_line in $${help_lines[@]}; do \
		IFS=$$'#' ; \
		help_split=($$help_line) ; \
		help_command=`echo $${help_split[0]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		help_info=`echo $${help_split[2]} | sed -e 's/^ *//' -e 's/ *$$//'` ; \
		printf "%-30s %s\n" $$help_command $$help_info ; \
	done
