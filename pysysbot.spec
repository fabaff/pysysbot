name:           pysysbot
Version:        0.1.3
Release:        1%{?dist}
Summary:        A simple python jabber bot for getting system information

License:        BSD
URL:            http://affolter-engineering.ch/pysysbot
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  systemd

Requires:         python-jabberbot
Requires:         python-psutil
Requires(post):   systemd
Requires(preun):  systemd
Requires(postun): systemd

%description
This python jabber (XMPP) bot is based on the jabberbot framework. The bot
is capable to display details about the system it is running on. If you don't
want or can stay connected through SSH all the time this is an easy way to
get information about the remote system.

%prep
%setup -q
rm -rf *.egg-info

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root="%{buildroot}"
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
%doc AUTHORS ChangeLog COPYING README.rst
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/
%{_unitdir}/%{name}.service
%{python2_sitelib}/*

%changelog
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
