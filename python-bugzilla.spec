Summary:	A Bugzilla library for Python
Name:		python-bugzilla
Version:	0.2
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	http://wwoods.fedorapeople.org/python-bugzilla/tarballs/%{name}-%{version}.tar.gz
# Source0-md5:	5253b8ba6bcc819def1184012e0f422a
URL:		http://wwoods.fedorapeople.org/python-bugzilla/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Bugzilla library for Python.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bugzilla
%{py_sitescriptdir}/*
