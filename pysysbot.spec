name:           pysysbot
Version:        0.1
Release:        1%{?dist}
Summary:        A simple python jabber bot for getting system information

License:        GPLv3+
URL:            http://affolter-engineering.ch/software-development/jabber-bots/
Source0:        http://files.affolter-engineering.ch/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  systemd

Requires:         python-jabberbot
Requires:         pystatgrab
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
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root="%{buildroot}"
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
%doc AUTHORS ChangeLog COPYING README
%{_mandir}/man*/%{name}*.*
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_unitdir}/%{name}.service
%{python_sitelib}/*

%changelog
* Tue Sep 03 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.1-1
- Simplified configuration file handling
- Updated to new upstream release 0.1

* Tue Sep 03 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.5-1
- man page added
- systemd macros added
- Updated to new upstream release 0.0.5

* Thu May 30 2013 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.4-1
- Spec file updated
- Updated to new upstream release 0.0.4

* Wed Jun 29 2011 Fabian Affolter <mail@fabian-affolter.ch> - 0.0.1-1
- Initial spec for Fedora
