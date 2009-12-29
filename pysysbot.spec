%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pysysbot
Version:        0.0.1
Release:        1%{?dist}
Summary:        A simple python jabber bot for getting system information

Group:          Applications/Internet
License:        GPLv3+
URL:            http://github.com/fabaff/pysysbot
Source0:        http://cloud.github.com/downloads/fabaff/%{name}/%{name}-%{version}.tar.bz2
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
#%{_mandir}/man*/*.*
%{_bindir}/%{name}
%{python_sitelib}/pysysbot/
%{python_sitelib}/pysysbot*.egg-info


%changelog
* Sat Dec 27 2008 Fabian Affolter <fabian@bernewireless.net> - 0.0.1-1
- Initial spec for Fedora
