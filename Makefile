NAME = pysysbot

all: update-po archive
VERSION := $(shell awk '/Version:/ { print $$2 }' $(NAME).spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' $(NAME).spec | sed 's|%{?dist}||g')
TAG=$(NAME)-$(VERSION)-$(RELEASE)

tag:
	@git tag -a -f -m "Tag as $(TAG)" -f $(TAG)
	@echo "Tagged as $(TAG)"

archive: tag
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD > $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created" 
	@sha1sum $(NAME)-$(VERSION).tar.bz2 > $(NAME)-$(VERSION).sha1sum
	@echo "$(NAME)-$(VERSION).sha1sum created" 
	@echo "Everything done.  All files are ready to upload." 

clean:
	rm -f *~ *bz2 *sha1sum
