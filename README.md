skype-rpm
=========

## Download Skype tarball

Go to http://www.skype.com/products/skype/linux/ and select "Dynamic" in "Choose your distribution" field.

## Build the rpm

`$ setarch i386 rpmbuild --define "_topdir $(pwd)" --define "_sourcedir $(pwd)" -ba skype.spec`

The resulting package will be created under `./RPMS/i686`.

## Install the rpm

On RHEL, CentOS, Fedora:

`$ sudo yum localinstall ./RPMS/i686/skype-*.rpm`
