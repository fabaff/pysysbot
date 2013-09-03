%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           drsbot
Version:        0.0.1
Release:        1%{?dist}
Summary:        A simple python jabber bot for getting system information

Group:          Applications/Internet
License:        GPLv3+
URL:            http://gitorious.org/pysysbot
Source0:        http://files.affolter-engineering.ch/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

Requires:       python-jabberbot


%description
This simple application is able to print/display the song that
is played at the moment on DRS3 (http://www.drs3.ch).  Like a
lot of radio stations in the world DRS3 is publishing the details
about the played song on their website. 


%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install --skip-build --root="%{buildroot}"
# doc files at the wrong place
#rm %{buildroot}%{_defaultdocdir}/%{name}-%{version}/{AUTHORS,ChangeLog,COPYING,README}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/%{name}
%{python_sitelib}/*


%changelog
* Wed Jun 29 2011 Fabian Affolter <fabian@bernewireless.net> - 0.0.1-1
- Initial spec for Fedora
