skype-rpm
=========

## Download Skype tarball

Go to http://www.skype.com/products/skype/linux/ and select "Dynamic" in "Choose your distribution" field.

## Download skype.spec

`$ wget --no-check-certificate https://raw.github.com/mopsfelder/skype-rpm/master/skype.spec`

## Build the rpm

`$ setarch i386 rpmbuild --define "_topdir $(pwd)" --define "_sourcedir $(pwd)" -ba skype.spec`

The resulting package will be created under `./RPMS/i686`.

## Install the rpm

On RHEL, CentOS, Fedora:

`$ sudo yum localinstall ./RPMS/i686/skype-*.rpm`
