%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           pysysbot
Version:        0.0.2
Release:        1%{?dist}
Summary:        A simple python jabber bot for getting system information

Group:          Applications/Internet
License:        GPLv3+
URL:            http://gitorious.org/pysysbot
Source0:        http://cloud.github.com/downloads/fabaff/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:       python-jabberbot
Requires:       pystatgrab


%description
This python jabber (XMPP) bot is based on the jabberbot framework 
(http://thpinfo.com/2007/python-jabberbot/).  The bot is capable to
display details about the system it is running on.  If you don't
want or can stay connected through SSH all the time this is an easy
way to get information about the remote system.


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}"
install -Dp -m 0644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
#doc files at the wrong place
rm %{buildroot}%{_defaultdocdir}/%{name}-%{version}/{AUTHORS,ChangeLog,COPYING,README}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_mandir}/man*/*.1*
%{_bindir}/%{name}
%{python_sitelib}/*


%changelog
* Thu Nov 11 2010 Fabian Affolter <fabian@bernewireless.net> - 0.0.2-1
- Updated to new upstream version 0.0.2

* Sat Dec 27 2009 Fabian Affolter <fabian@bernewireless.net> - 0.0.1-1
- Initial spec for Fedora
