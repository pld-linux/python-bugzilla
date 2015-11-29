Summary:	A Bugzilla library for Python
Summary(pl.UTF-8):	Biblioteka Bugzilli dla Pythona
Name:		python-bugzilla
Version:	0.3
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/python-bugzilla/%{name}-%{version}.tar.gz
# Source0-md5:	c01c9b489220b4fd853a3f6f8df20b01
Patch0:		%{name}-pld.patch
URL:		https://fedorahosted.org/python-bugzilla/
BuildRequires:	python-devel >= 1:2.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Bugzilla library for Python.

%description -l pl.UTF-8
Biblioteka Bugzilli dla Pythona.

%prep
%setup -q
%patch0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bugzilla
%{py_sitescriptdir}/*
