%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-oauth
Version:        1.0.1
Release:        3.ius%{?dist}
Summary:        Library for OAuth version 1.0a

Group:          Development/Languages
License:        MIT
URL:            http://code.google.com/p/oauth/
Source0:        http://pypi.python.org/packages/source/o/oauth/oauth-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

%description
Library for OAuth version 1.0a.


%prep
%setup -q -n oauth-%{version}


%build
python setup.py build


%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --skip-build --root $RPM_BUILD_ROOT

 
%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE.txt
%{python_sitelib}/*


%changelog
* Mon Jun 27 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0.1-3.ius
- Rebuilding for EL

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Oct 06 2009 Sebastian Dziallas <sebastian@when.com> - 1.0.1-1
- initial packaging
