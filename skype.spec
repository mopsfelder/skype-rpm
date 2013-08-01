%global debug_package %{nil}

Name:           skype
Version:        4.2.0.11
Release:        1%{?dist}
Summary:        Skype is a free Internet telephony from Microsoft

License:        Commercial
URL:            http://www.skype.com/products/skype/linux/
Source0:        %{name}-%{version}.tar.bz2

Requires:       alsa-lib(x86-32) >= 1.0.23
Requires:       glibc(x86-32)
Requires:       libgcc(x86-32)
Requires:       libpng(x86-32)
Requires:       libX11(x86-32)
Requires:       libXext(x86-32)
Requires:       libXScrnSaver(x86-32)
Requires:       libXv(x86-32)
Requires:       libstdc++(x86-32)
Requires:       qt(x86-32) >= 4.6
Requires:       qt-x11(x86-32)
Requires:       qtwebkit(x86-32)

ExcludeArch:    x86_64
AutoReqProv:    no


%description
Skype is a free Internet telephony from Microsoft.


%prep
%setup -q


%build


%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_datadir}/applications
%{__mkdir_p} %{buildroot}%{_datadir}/%{name}
%{__mkdir_p} %{buildroot}%{_sysconfdir}/dbus-1/system.d

%{__cp} %{name} %{buildroot}%{_bindir}
%{__cp} %{name}.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d
%{__cp} %{name}.desktop %{buildroot}%{_datadir}/applications

# Resources
for DIR in avatars lang sounds; do
    %{__cp} -r $DIR %{buildroot}%{_datadir}/%{name}
done

# Icons
for SIZE in 16 24 32 48 64 96 128 256; do
    %{__mkdir_p} %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps
    %{__cp} icons/SkypeBlue_${SIZE}x${SIZE}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${SIZE}x${SIZE}/apps/%{name}.png
done


%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%defattr(0644,root,root,0755)
%{_sysconfdir}/dbus-1/system.d/%{name}.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/avatars/*
%{_datadir}/%{name}/lang/*
%{_datadir}/%{name}/sounds/*
%{_datadir}/icons/*
%dir %{_datadir}/%{name}/avatars
%dir %{_datadir}/%{name}/lang
%dir %{_datadir}/%{name}/sounds
%dir %{_datadir}/%{name}
%doc LICENSE README third-party_attributions.txt


%changelog
* Wed Jul 31 2013 Murilo Opsfelder Araujo <mopsfelder@gmail.com> 4.2.0.11-1
- Initial version
