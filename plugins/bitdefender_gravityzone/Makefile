VERSION=2.0.0
NAME=bitdefender_gravityzone_comprehensive
VENDOR=custom
PKG=$(VENDOR)-$(NAME)-$(VERSION).tar

default: tarball

tarball:
	rm -rf build *.tar *.tar.gz
	mkdir -p build/$(NAME)
	rsync -av . build/$(NAME) --exclude=build --exclude=*.tar --exclude=*.tar.gz --exclude=venv --exclude=.git --exclude=.DS_Store
	cp plugin.spec.yaml build/
	cd build && COPYFILE_DISABLE=1 tar -cvf ../$(PKG) plugin.spec.yaml $(NAME)
	rm -rf build