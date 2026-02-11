%global module wcwidth

Name:		python-wcwidth
Version:	0.6.0
Release:	1
Summary:	Measures number of Terminal column cells of wide-character codes
Group:		Development/Python
License:	MIT
URL:		https://github.com/jquast/wcwidth
Source0:	https://pypi.io/packages/source/w/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
# Obsolete old python2 module this packages used to provide
Obsoletes: python2-wcwidth < %{version}-%{release}

%description
This API is mainly for Terminal Emulator implementors, or those writing 
programs that expect to interpreted by a terminal emulator and wish to 
determine the printable width of a string on a Terminal.

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
