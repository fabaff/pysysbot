name:           pysysbot
Version:        0.3.0
Release:        1%{?dist}
Summary:        A simple python jabber bot for getting system information

License:        BSD
URL:            http://affolter-engineering.ch/pysysbot
Source0:        https://github.com/fabaff/pysysbot/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  systemd

Requires:         python3-slixmpp
Requires:         python3-psutil
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
This python jabber (XMPP) bot is based on the jabberbot framework. The bot
is capable to display details about the system it is running on. If you don't
want or can stay connected through SSH all the time this is an easy way to
get information about the remote system.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install
install -Dp -m 0644 data/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m 0644 data/%{name}.conf %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -Dp -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
rm -rf %{buildroot}%{_defaultdocdir}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%doc AUTHORS ChangeLog README.rst
%license COPYING
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/
%{_unitdir}/%{name}.service
%{python3_sitelib}/%{name}-*.egg-info/
%{python3_sitelib}/%{name}/

%changelog
* Wed May 08 2019 Fabian Affolter <mail@fabian-affolter.ch> - 0.3.0-1
- Remove Python 2 deps (rhbz#1701945)
- Update to new upstream release 0.3.0

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Jan 22 2014 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.3-1
- License update
- Update to new upstream release 0.1.3

* Tue Sep 17 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.2-1
- Update requirements
- License update
- Update to new upstream release 0.1.2

* Sun Sep 15 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.1.1-1
- New download location
- Update to new upstream release 0.1.1

* Tue Sep 03 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-1
- Simplified configuration file handling
- Update to new upstream release 0.1

* Tue Sep 03 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- Man page added
- Add systemd macros
- Update to new upstream release 0.0.5

* Thu May 30 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Update spec file
- Update to new upstream release 0.0.4

* Wed Jun 29 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-1
- Initial spec for Fedora