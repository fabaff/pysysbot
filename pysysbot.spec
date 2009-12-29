%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pysysbot
Version:        0.1
Release:        2%{?dist}
Summary:        A simple python jabber bot for getting system information

Group:          Applications/Internet
License:        GPLv3+
URL:            https://developer.berlios.de/projects/pythonwifi/
Source0:        http://download.berlios.de/pythonwifi/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

Requires:       python-jabberbot

%description
This python jabber (XMPP) bot is based on the jabberbot framework 
(http://thpinfo.com/2007/python-jabberbot/).  The bot is capable to
display details about the system it is running on. 


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}"


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_mandir}/man*/*.*
%{_bindir}/
%{python_sitelib}/pysysbot/
%{python_sitelib}/pysysbot*.egg-info


%changelog
* Thu Dec 24 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5.0-2
- Removed the convert to utf-8 part 
- Added license for examples
- Fixed tarball URL
- Added man pages

* Wed Dec 23 2009 Fabian Affolter <fabian@bernewireless.net> - 0.5.0-1
- Updated docs
- Updated BR
- Updated to new upstream version 0.5.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 18 2009 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-2
- Changes acc. to bug #478300

* Sat Dec 27 2008 Fabian Affolter <fabian@bernewireless.net> - 0.3.1-1
- Initial spec for Fedora
